import pytest
import os
import tempfile
from pathlib import Path

from gltest.direct import loader
from gltest.direct.loader import deploy_contract


@pytest.fixture(autouse=True)
def _enable_pickling_validation(direct_vm, monkeypatch):
    """Make Direct Mode catch storage serialization bugs."""
    direct_vm.check_pickling = True

    original_warp = direct_vm.warp

    def warp_and_refresh_raw_message(timestamp):
        original_warp(timestamp)
        import sys

        gl_module = sys.modules.get("genlayer.gl")
        if gl_module is not None and isinstance(getattr(gl_module, "message_raw", None), dict):
            gl_module.message_raw["datetime"] = timestamp

    monkeypatch.setattr(direct_vm, "warp", warp_and_refresh_raw_message)
    yield


@pytest.fixture
def direct_deploy(direct_vm, monkeypatch):
    """Pin the Direct Mode SDK to the latest official stable GenVM release.

    Letting genlayer-test select its implicit "latest" can silently cross into
    prerelease SDK artifacts. v0.2.16 is the verified non-prerelease artifact
    that contains the contract's declared py-genlayer hash.
    """
    def windows_safe_message_injection(vm):
        """Work around genlayer-test unlinking fd 0 before Windows releases it."""
        from genlayer.py import calldata
        from genlayer.py.types import Address

        sender = Address(vm.sender) if isinstance(vm.sender, bytes) else vm.sender
        contract = Address(vm._contract_address) if isinstance(vm._contract_address, bytes) else vm._contract_address
        origin = Address(vm.origin) if isinstance(vm.origin, bytes) else vm.origin
        message = {
            "contract_address": contract,
            "sender_address": sender,
            "origin_address": origin,
            "stack": [],
            "value": vm._value,
            "datetime": vm._datetime,
            "is_init": False,
            "chain_id": vm._chain_id,
            "entry_kind": 0,
            "entry_data": b"",
            "entry_stage_data": None,
        }
        encoded = calldata.encode(message)
        fd, path = tempfile.mkstemp()
        os.write(fd, encoded)
        os.lseek(fd, 0, os.SEEK_SET)
        vm._original_stdin_fd = os.dup(0)
        os.dup2(fd, 0)
        os.close(fd)
        vm._stablematch_temp_stdin_path = path

    monkeypatch.setattr(loader, "_inject_message_to_fd0", windows_safe_message_injection)

    def deploy(contract_path, *args, **kwargs):
        try:
            return deploy_contract(
                Path(contract_path), direct_vm, *args, sdk_version="v0.2.16", **kwargs
            )
        finally:
            original = getattr(direct_vm, "_original_stdin_fd", None)
            if original is not None:
                os.dup2(original, 0)
                os.close(original)
                del direct_vm._original_stdin_fd
            temp_path = getattr(direct_vm, "_stablematch_temp_stdin_path", None)
            if temp_path is not None:
                os.unlink(temp_path)
                del direct_vm._stablematch_temp_stdin_path

    return deploy
