import smtplib
import getpass
from pandas import *
from xlrd import *
def mailto(eid,pwd,sub,mes,det):
    try:
        message=open(mes,"r").read()
        details = read_excel(det,sheet_name='Sheet1')
        r,c = details.shape
        cols = list(details.columns)
        for i in range(r):
            mail = details['MAIL'].get(i)
            a=message
            for j in cols:
                if j=='MAIL':
                    continue
                else:
                    a = a.replace('$'+j,str(details[j].get(i)))
            a = "Subject:{}\n\n{}".format(sub,a)
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.starttls()
            server.login(eid,pwd)
            server.sendmail(eid,mail,a)
        return "Mail sent"
    except FileNotFoundError:
        return "File not found"
    except:
        return "Check your credentials and connectivity! Try Again"
