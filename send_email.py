#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib, ssl
import getpass
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

sender_mail = "caso.alerts@gmail.com"
receiver_mail = input("Adresse destinataire: \n")

subject = "Mail sent from my Terminal"
body = input("Contenu du message : \n")

port = 465 #SSL
password = getpass.getpass(prompt="MDP de boite mail pour envoi du mail: \n")

#Creation du mail et headers
message = MIMEMultipart()
message["From"] = sender_mail
message["To"] = receiver_mail
message["Subject"] = subject
message["Bcc"] = receiver_mail

#Corps du mail
message.attach(MIMEText(body, "plain"))

if len(sys.argv) > 1:
	for item in sys.argv[1:]:
		#Gestion de la pj
		filename = item
		with open(filename, "rb") as attachment:
			part = MIMEBase("application", "octet-stream")
			part.set_payload(attachment.read())

		#Encodage pj et ajout info dans headers du mail
		encoders.encode_base64(part)
		part.add_header("Content-Disposition", f"attachment; filename= {filename}")

		#Ajout pj au mail
		message.attach(part)
		print(f"Pièce jointe {item} correctement ajoutée au message")

#Conversion message en caractere
text = message.as_string()


#Creation context SSL secure
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
	server.login(sender_mail, password)
	server.sendmail(sender_mail, receiver_mail, text)

print(f"Message correctement envoyé à {receiver_mail}")