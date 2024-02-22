import smtplib, ssl
import string
import os
from time import strftime
import sys

TO_ADDRESS = 'REDACTED'
SMTP_SERVER = 'smtp.gmail.com'

SMTP_USERNAME = "REDACTED"
SMTP_PASSWORD = "REDACTED"

context = ssl.create_default_context()

EMAILTEMPLATE = """From: Raspberry Pi - sherl0ck
Subject: New Events on RPi

The game is on! Is this real?

"""

LOGFILE = '/var/tmp/opencanary-tmp.log'

# very basic code to send a simple email to the defined recipient
def  SendEmail(emailText):
    emailSent = False
    try:
        emailMessage = EMAILTEMPLATE + emailText
        server = smtplib.SMTP(SMTP_SERVER,587)
        server.ehlo()
        server.starttls(context=context)
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(SMTP_USERNAME, TO_ADDRESS, emailMessage)
        server.quit()
        emailSent = True
    except:
        print("Error sending Emails - Log not Emptied")
    return emailSent

def findParam(sourceEvent, checkString):
    result = ""
    fullCheckString = '"' + checkString + '": '
    startChar = sourceEvent.find(fullCheckString)
    if startChar > 0:
        startChar += len(fullCheckString)
        endChar = sourceEvent.find(',', startChar)
        if endChar < 0:
            endChar = sourceEvent.find('}', startChar)
        if endChar > 0:
            result = sourceEvent[startChar:endChar].strip('" ')
    return result

# basic parser for each line of text to see if it is one of the whitelisted events that do not need reporting
def CheckLine(sourceEvent):
    sendTheEmail = True

    sourceIP   = findParam(sourceEvent, "src_host")
    destIP     = findParam(sourceEvent, "dst_host")
    destPort   = findParam(sourceEvent, "dst_port")
    sourcePort = findParam(sourceEvent, "src_port")
    logType    = findParam(sourceEvent, "logtype")
    adjTime    = findParam(sourceEvent, "local_time_adjusted")

    # better code would be to use a config file, but for now let's just add some simple cases
    if destPort == "-1":
        if destIP == "":
            # most probably logs like Canary Running!!!
            sendTheEmail = False
            print("Basic logs")
    else:
        if logType == "13001":
            if destIP == "0.0.0.0":
            # Too much SNMP traffic when enabled - should investigate
                sendTheEmail = False
                print("SNMP traffic")
        else:
            sendTheEmail = True

#don't remove the below lines until localtext="" line
    displayCommand = "{0}:{1} > {2}:{3}  ".format (sourceIP,sourcePort,destIP,destPort)
    if (sendTheEmail):
        displayCommand += '\033[31;40m UNKNOWN \033[37;40m\n'
    else:
        displayCommand += '\033[32;40m Ignored \033[37;40m\n'

    f = open("/dev/tty1", "w")
    f.write(displayCommand)
    f.close()
#Investigate this return is resulting in any sendTheEmail's after this being invalid. 
#But commenting it is stopping emails
    return sendTheEmail

#main code starts here
localText = ""

file2 = open(LOGFILE,'r')
#Display the logs neatly.
count = 0
for line in file2:
    sourceIP   = findParam(line.strip(), "src_host")
    destIP     = findParam(line.strip(), "dst_host")
    destPort   = findParam(line.strip(), "dst_port")
    sourcePort = findParam(line.strip(), "src_port")
    logType    = findParam(line.strip(), "logtype")
    adjTime    = findParam(line.strip(), "local_time_adjusted")
    if (CheckLine(line.strip())==True):
        count +=1
        localText += "Event {}:\n\n".format(count)
        localText += "Source IP: {}    Destination IP: {} \nSource Port: {}            Destination Port: {} \nTime: {}\n".format(sourceIP, destIP, sourcePort, destPort, adjTime)
        localText += "\n{}".format(line)
        localText += "================================================\n"
    else:
        print("ignoring line\n\r")
file2.close()

#print(localText)

if (count > 0):
    emailsSent= SendEmail(localText)
    if(emailsSent):
        print("Sent mail successfully!")
        #this is a bit crude but acts as a simple emptying of the log file
        # Only clear the log if the email was sent, if not the log will remain and next time it will re-try
        file2 = open(LOGFILE,'w')
        file2.writelines([])
        file2.close