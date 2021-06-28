import sqlite3
#from alert import email_alert
from datetime import datetime, time
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
#c.execute("SELECT name FROM sqlite_master WHERE type='table';")
# print(c.fetchall())
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
while True:
    today = datetime.now()
    hourandminutes = str(today).split(" ")
    dateanday = hourandminutes[0].split("-")
    hourandminutesone = hourandminutes[1].split(":")
    finalhourandminutes = str(dateanday[0])+str(dateanday[1])+str(
        dateanday[2])+str(hourandminutesone[0])+str(hourandminutesone[1])
    #print(finalhourandminutes)
    c.execute("SELECT * FROM main_mainmodule")
    results = c.fetchall()
    for i in results:
        print(finalhourandminutes,i[4])
        if(i[4])==finalhourandminutes:
            greetings="hi"+i[1]
            email_alert(greetings,i[3],i[2])
            sql = "DELETE FROM main_mainmodule WHERE id = {}".format(i[0])
            c.execute(sql)
            conn.commit()




    #if finalhourandminutes in tasks:
        #greetings = "HI {}".format(name)
        #print(greetings, tasks[finalhourandminutes], email)
        #email_alert(greetings, tasks[finalhourandminutes], email)
        #print("success")
        #tm.sleep(60)
