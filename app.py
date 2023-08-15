import smtplib
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time, random

load_dotenv()

remitente=os.getenv('user')
destinatario=''
asunto='ESTIMADO/A PROFESIONAL DEL DERECHO'

correo=MIMEMultipart()
correo['Subject']=asunto
correo['From']=remitente
correo['To']=''


dir_archivo= "venv/correo.html"
correos=open('venv/enviar_a.txt', 'r')


with open(dir_archivo,'r', encoding='utf-8') as archivo:
    html=archivo.read()

correo.attach(MIMEText(html,'html'))    

server=smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(remitente, os.getenv('pass'))
    
for m in correos:
        
    try:        
        server.sendmail(remitente,m,correo.as_string())
        f = open ('mailsenviados.txt','a')
        f.write(str(m))
        f.close()
                    
    except:
        continue

    time.sleep(random.randrange(1,10))
    
server.quit()
print("Proceso de envío de mails finalizado exitosamente")

