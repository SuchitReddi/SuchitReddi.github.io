#!/bin/bash

# Define the expected SSID
EXPECTED_SSID="Student" #CHANGE AS REQUIRED
EXPECTED_INTERFACE="wlan0"
# Check if the current SSID matches the expected SSID
CURRENT_SSID=$(/sbin/iwgetid --raw $EXPECTED_INTERFACE)

#Log file path
LOG="/home/<user>/tools/scripts/wifi_check-log.txt" #CHANGE AS REQUIRED

# IP for ping check
IP=10.6.15.254

if [ "$CURRENT_SSID" != "$EXPECTED_SSID" ]; then
    echo "$(date -Is) Wi-Fi is not connected to the expected SSID ($EXPECTED_SSID), attempting to reconnect" >> $LOG
    echo "Failure. Trying to Reconnect to $EXPECTED_SSID"
    if command -v /sbin/ip &> /dev/null; then
        /bin/nmcli connection up $EXPECTED_SSID
    elif command -v sudo ifconfig &> /dev/null; then
        nmcli connection up $EXPECTED_SSID
        sleep 10
    else
        echo "$(date -Is) Failed to reconnect: issue with nmcli command" >> $LOG
    fi
else
    echo "Connected to $EXPECTED_SSID"
fi

# Ping the router to check for internet connectivity
ping -c 4 $IP > /dev/null
if [ $? -eq 0 ]; then
    echo "Ping check successful"
else
    echo "Ping check failed"
    echo "$(date -Is) Ping failed, Wi-Fi connectivity issues detected" >> $LOG
fi

echo 'WiFi check finished'
