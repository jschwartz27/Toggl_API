import os
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders


def send(data, pdf_attach: bool, CREDENTIALS) -> None:
    pdf_names = ["summary-report.pdf", "detailed-report.pdf", "weekly-report.pdf"]
    fromaddr = CREDENTIALS["username"]
    toaddr   = CREDENTIALS["recipients"]
    password = CREDENTIALS["password"]

    msg = MIMEMultipart()
    msg['From'] = fromaddr 
    # here TO needs to be ", ".join(recipients)
    msg['To'] = ", ".join(toaddr)   
    msg['Subject'] = data["subject"]
    # msg.attach(MIMEText(data["body"], 'plain'))
    msg.attach(MIMEText(data["body"], 'html'))

    if pdf_attach:
        for filename in pdf_names: 
            attachment = open(filename, "rb") 
            p = MIMEBase('application', 'octet-stream') 
            # To change the payload into encoded form 
            p.set_payload((attachment).read()) 
            encoders.encode_base64(p) 
            header = 'toggl_data', "attachment; filename={}".format(filename)
            p.add_header(header)
            msg.attach(p) 

    s = smtplib.SMTP('smtp.gmail.com', 587)     # creates SMTP session 
    s.starttls()                                # start TLS for security 
    s.login(fromaddr, password)  # Authentication    
    text = msg.as_string()       # Converts the Multipart msg into a string
    s.sendmail(fromaddr, toaddr, text)
    s.quit()

    # ? can this be done before email sent since already attached?
    if pdf_attach:
        for filepath in pdf_names:
            os.remove(filepath)
