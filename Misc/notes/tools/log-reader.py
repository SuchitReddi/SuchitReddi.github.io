import smtplib, ssl
import string
import os
from time import strftime
import sys

#Settings
TO_ADDRESS = 'securityalerts@duck.com'
SMTP_SERVER = 'smtp.gmail.com'

SMTP_USERNAME = "vizagrockers123@gmail.com"
SMTP_PASSWORD = "rwtn cauo nuhy ymyh"
SUBJECT = "OpenCanary Alert"

context = ssl.create_default_context()

EMAILTEMPLATE = """From: OpenCanary RPi
Subject: OpenCanary Alert from RPi

New Events
"""

NEWLINE = "\n\r"
SOURCELOGFILE = '/var/tmp/opencanary-tmp.log'

# very basic code to send a simple email to the defined recipient
def  SendEmail(emailText):
    emailSent = False
    try:
        emailMessage = EMAILTEMPLATE + emailText
        server = smtplib.SMTP(SMTP_SERVER,587)
        server.ehlo()
        server.starttls(context=context)
#        print("tls started")
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
#        print("Login Successful")
        server.sendmail(SMTP_USERNAME, TO_ADDRESS, emailMessage)
#        print("Sent mail")
        server.quit()
        emailSent = True
    except:
        print("Error sending Emails - Log not Emptied")
    return emailSent



# utility to find the value for a given source parameter.
# sample of event string elements is
# , "node_id": "opencanary-1", "src_host": "192.168.0.11", "src_port": "37284"}
# the string to check should be of the format "src_port"

def findParam(sourceEvent,checkString):
    result = ""
    fullCheckString = '"'+checkString+'": "'
    startChar = sourceEvent.find(fullCheckString)
    if(startChar>0):
        startChar +=len(fullCheckString)
        endChar =sourceEvent.find('"',startChar)
        if(endChar>0):
            result = sourceEvent[startChar:endChar]
        else:
            print("no matching end \n")
    return result

#basic parser for each line of text to see if it is one of the whitelisted events that do not need reporting
def CheckLine (sourceEvent):
     sendTheEmail = True
     print("checking line > {}\n",sourceEvent)

     sourceIP        = findParam(sourceEvent,"src_host")
     destinationPort = findParam(sourceEvent,"dst_port")
     sourcePort      = findParam(sourceEvent,"src_port")
     print("source IP: {}   destination port: {} \n".format(sourceIP,destinationPort))
     #better code would be to use a config file, but for now lets just add some simple cases
     if(sourceIP =="127.0.0.1"):
#         if(destinationPort=="631"):
             #local port on Rpi doing a regular check of the printer port
             sendTheEmail = False
             print("No new events")
     else:
         if(destinationPort == "-1"):
             #most prolly logs like Canary Running!!!
             sendTheEmail = False
             print("Basic logs")
     else:
         if(sourceIP == "192.168.0.13"):
             if(destinationPort == "445") or (destinationPort == "139" ):
                 #mac mini doing a regular port check on these 2 ports
                 sendTheEmail = False
         else:
             if(sourceIP == "192.168.0.15"):
                 if(destinationPort == "139"):
                      #main PC on wired network
                      sendTheEmail = False
     displayCommand = "{0}:{1} > {2}  ".format (sourceIP,sourcePort,destinationPort)
     if (sendTheEmail):
         displayCommand += '\033[31;40m UNKNOWN \033[37;40m\n'
     else:
         displayCommand += '\033[32;40m Ignored \033[37;40m\n'

     f = open("/dev/tty1", "w")
     f.write(displayCommand)
     f.close()
     return sendTheEmail

#main code starts here
localText = ""


file2 = open(SOURCELOGFILE,'r')
count  =0
for line in file2:
    if (CheckLine(line.strip())==True):
        count +=1
        localText += "Event {}: {}".format(count,line.strip())
        localText += NEWLINE
    else:
        print("ignoring line\n\r")
file2.close

if (count >0):
    emailsSent= SendEmail (localText)
    if(emailsSent):
        #this is a bit crude but acts as a simple emptying of the source file
        # Only clear the log if the email was sent
        # if not the log will remain and next time it will re-try
        file2 = open(SOURCELOGFILE,'w')
        file2.writelines([])
        file2.close
