import smtplib

to= input(" Enter the email of recipient: \n")
subject= input("Enter the subject of email: \n")
content= input("Enter the content for email: \n")

def sendEmail(to,subject,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your@email','yourpassword')
    message=f"Subject:{subject}\n\n{content}"
    server.sendmail('your@email',to,message)
    server.close()

sendEmail(to,subject,content)