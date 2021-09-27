#https://www.arclab.com/en/kb/email/list-of-smtp-and-pop3-servers-mailserver-list.html
from smtplib import SMTP
server =SMTP('smtp.gmail.com' , 587)
server.starttls() #turn on TLSالنقل الآمن
server.login('USER' , 'PASSWORD')
server.sendmail("from_address" , "to_addrs" , "message")
server.quit()
#https://myaccount.google.com/u/1/lessecureapps?pli=1&pageld=none
#Allow less secure apps : ON
