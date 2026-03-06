param(
    [string]$GuideUrl = "https://raw.githubusercontent.com/code-yeongyu/oh-my-opencode/refs/heads/dev/docs/guide/installation.md",
    [switch]$Execute
)

$ErrorActionPreference = 'Stop'

Write-Host "Downloading installation guide from:`n$GuideUrl" -ForegroundColor Cyan
$guide = Invoke-WebRequest -Uri $GuideUrl -UseBasicParsing

if (-not $guide.Content) {
    throw "Installation guide is empty."
}

$pattern = '(?s)```powershell\s*(.*?)\s*```'
$matches = [regex]::Matches($guide.Content, $pattern)

if ($matches.Count -eq 0) {
    throw "No PowerShell installation block was found in the guide. Open the guide and follow it manually: $GuideUrl"
}

$installScript = $matches[0].Groups[1].Value.Trim()

Write-Host "Detected PowerShell install block:" -ForegroundColor Green
Write-Host "---------------------------------"
Write-Host $installScript
Write-Host "---------------------------------"

if (-not $Execute) {
    Write-Host "Dry run complete. Re-run with -Execute to run the detected command block." -ForegroundColor Yellow
    exit 0
}

Write-Host "Executing install block..." -ForegroundColor Cyan
Invoke-Expression $installScript

Write-Host "\nInstall command completed." -ForegroundColor Green
Write-Host "If the guide includes extra configuration sections (shell theme, aliases, or profile updates), apply those now:" -ForegroundColor Yellow
Write-Host $GuideUrl -ForegroundColor Yellow
