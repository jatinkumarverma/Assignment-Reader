import smtplib
import datetime as dt
import time

def send_email(receiver, msg):
    
    conn = smtplib.SMTP('smtp.gmail.com', 587)
    
    type(conn)
    
    conn.ehlo()
    
    conn.starttls()
    
    conn.login('*****@gmail.com', '*****')
    
    conn.sendmail('*****@gmail.com', receiver, msg)
    
    conn.close()
    
today = dt.date.today()

messages = []

default = f"Subject: Upload Assignment-%d for %s \nHello Jatin It's a '''reminder''' to upload the assignment-%d for %s"

if (str(today) == '2020-07-19'):
    subject = "IWP"
    number = 1
    messages.append(default %(number, subject, number, subject))
    
    subject = "PDC"
    number = 1
    messages.append(default %(number, subject, number, subject))

elif (str(today) == '2020-07-18'):
    subject = "IWP"
    number = 1
    messages.append(default %(number, subject, number, subject))

else:
    messages.append("Subject: No upload today \nNo need to upload")
    
for i in messages:
    send_email('jatin760verma@gmail.com', i)
    print("Sent email")
