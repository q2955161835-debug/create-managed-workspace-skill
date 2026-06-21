param(
  [Parameter(Mandatory=$true)]
  [string]$Path,

  [string]$Name,

  [switch]$Overwrite,

  [switch]$InitGit
)

$ErrorActionPreference = "Stop"
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$pythonScript = Join-Path $scriptDir "new_workspace.py"

$argsList = @($pythonScript, $Path)
if ($Name) { $argsList += @("--name", $Name) }
if ($Overwrite) { $argsList += "--overwrite" }
if ($InitGit) { $argsList += "--init-git" }

python @argsList
