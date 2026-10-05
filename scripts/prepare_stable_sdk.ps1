$ErrorActionPreference = 'Stop'

$stableGenVm = 'v0.2.16'
$contractPath = Join-Path $PSScriptRoot '..\contracts\stablematch.py'
$contractPath = (Resolve-Path $contractPath).Path
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$toolingRoot = Join-Path $repoRoot '.tooling\genvm'
$stdDestination = Join-Path $toolingRoot 'runners\py-lib-genlayer-std\src'

$setupOutput = & genvm-lint setup --version $stableGenVm --contract $contractPath --json
if ($LASTEXITCODE -ne 0) {
    throw "genvm-lint setup failed for stable GenVM $stableGenVm"
}
$setup = ($setupOutput -join "`n") | ConvertFrom-Json
if (-not $setup.ok -or $setup.version -ne $stableGenVm) {
    throw "Expected stable GenVM $stableGenVm SDK; received '$($setup.version)'"
}

$stdPath = $setup.extraPaths | Where-Object { $_ -match '[\\/]py-lib-genlayer-std[\\/]' } | Select-Object -First 1
if (-not $stdPath -or -not (Test-Path (Join-Path $stdPath 'genlayer'))) {
    throw 'Stable py-lib-genlayer-std SDK was not found in the linter setup result'
}

New-Item -ItemType Directory -Force -Path $stdDestination | Out-Null
Copy-Item -Path (Join-Path $stdPath '*') -Destination $stdDestination -Recurse -Force
$env:GENVMROOT = $toolingRoot

Write-Output "Prepared stable GenVM SDK $stableGenVm at $toolingRoot"
& genvm-lint check --json $contractPath
if ($LASTEXITCODE -ne 0) {
    throw 'GenVM lint or semantic validation failed'
}
