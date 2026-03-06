# oh-my-opencode (Windows) quick setup

Because this environment cannot access GitHub directly, this repo includes a PowerShell helper that reads the **official installation guide** and runs the first PowerShell installation block from it.

## 1) Open PowerShell as your normal user

Use **PowerShell 7+** if possible.

## 2) Allow script execution for your user (one-time)

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

## 3) Run the helper in dry-run mode first

```powershell
pwsh -File .\scripts\install-oh-my-opencode-windows.ps1
```

This prints the install block detected from:

- <https://raw.githubusercontent.com/code-yeongyu/oh-my-opencode/refs/heads/dev/docs/guide/installation.md>

## 4) Execute the detected install block

```powershell
pwsh -File .\scripts\install-oh-my-opencode-windows.ps1 -Execute
```

## 5) Finish any post-install config from the guide

If the guide has additional manual steps (profile, aliases, prompt theme, etc.), apply them after the script finishes.

## Notes

- If your network blocks `raw.githubusercontent.com`, open the guide in a browser with your normal network and run its commands manually.
- The helper intentionally executes only the **first PowerShell code block** from the guide to avoid guessing other steps.
