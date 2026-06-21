param(
  [Parameter(Mandatory=$true)]
  [string]$Path,

  [string]$Name,

  [ValidateSet("multi-task", "specialized")]
  [string]$WorkspaceKind = "multi-task",

  [switch]$Specialized,

  [switch]$Overwrite,

  [switch]$InitGit
)

$ErrorActionPreference = "Stop"
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$pythonScript = Join-Path $scriptDir "new_workspace.py"

$argsList = @($pythonScript, $Path)
if ($Name) { $argsList += @("--name", $Name) }
if ($Specialized) {
  $argsList += "--specialized"
} else {
  $argsList += @("--workspace-kind", $WorkspaceKind)
}
if ($Overwrite) { $argsList += "--overwrite" }
if ($InitGit) { $argsList += "--init-git" }

python @argsList
