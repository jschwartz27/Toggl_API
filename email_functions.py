import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders


def send(, , CREDENTIALS) -> None:

    quit()
    fromaddr = CREDENTIALS["username"] + "@gmail.com"
    toaddr   = CREDENTIALS["username"] + "@gmail.com"

    msg = MIMEMultipart()  # instance of MIMEMultipart 
    # storing the senders and receivers email address   
    msg['From'] = fromaddr  
    msg['To'] = toaddr 
    # storing the subject  
    msg['Subject'] = "HEY BITCH!!!"
    # string to store the body of the mail 
    body = "yeah you!"
    
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 

    # open the file to be sent  
    #filename = "File_name_with_extension"
    #attachment = open("Path of the file", "rb") 
    
    # instance of MIMEBase and named as p 
    # p = MIMEBase('application', 'octet-stream') 
    # To change the payload into encoded form 
    # p.set_payload((attachment).read()) 
    
    # encode into base64 
    # encoders.encode_base64(p) 
    
    # p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    
    # attach the instance 'p' to instance 'msg' 
    # msg.attach(p) 

    s = smtplib.SMTP('smtp.gmail.com', 587)     # creates SMTP session 
    s.starttls()                                # start TLS for security 
    s.login(fromaddr, CREDENTIALS["password"])  # Authentication    
    text = msg.as_string()         # Converts the Multipart msg into a string
    s.sendmail(fromaddr, toaddr, text)          # sending the mail 
    s.quit()
