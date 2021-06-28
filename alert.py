import smtplib
from email.message import EmailMessage

def email_alert(subject,body,to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    
    user = "krishnamsettyraju@gmail.com"
    msg['from'] = user
    password = "nvyuxedfkttwhrta" 
    
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)
    print("sucess")
    server.quit()


#email_alert("Hey","hello world","dawnreddy1111@gmail.com")  

from datetime import datetime,time
import time as tm

# Calling now() function
today = datetime.now()
print(datetime.now())
#tm.sleep(50)
print("Current date and time is", today)
name=input("plzz enter your name")
email=input("please enter your email")
tasks = {}
check=input("press y to enter the task and n to exit")
while check=="y":
    year=input("enter year")
    month=input("enter month")
    day=input("enter day")
    hour=input("enter hour")
    minutes=input("enter minutes")
    #day = input("enter day")
    #month = input("enter month")
    task=input("enter the task")
    Time=str(datetime(int(year),int(month),int(day),int(hour),int(minutes)))
    Timezero=Time.split(" ")
    Timeone=Timezero[1].split(":")
    Timethree=Timezero[0].split("-")
    Timetwo="".join(Timeone)
    Timefour="".join(Timethree)
    Timetwo=Timefour+Timetwo
    #print(Timetwo)
    tasks[str(Timetwo)]=task
    #print(tasks)
    #tm.sleep(60)
    check=input("press y to add another task n to quit")
while True:
    today=datetime.now()
    hourandminutes=str(today).split(" ")
    dateanday = hourandminutes[0].split("-")
    hourandminutesone=hourandminutes[1].split(":")
    finalhourandminutes=str(dateanday[0])+str(dateanday[1])+str(dateanday[2])+str(hourandminutesone[0])+str(hourandminutesone[1])+"00"
    print(finalhourandminutes)
    if finalhourandminutes in tasks :
        greetings="HI {}".format(name)
        print(greetings,tasks[finalhourandminutes],email)
        email_alert(greetings,tasks[finalhourandminutes],email)
        print("success")
        tm.sleep(60)
