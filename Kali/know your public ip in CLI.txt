host myip.opendns.com resolver1.opendns.com

or

dig TXT +short o-o.myaddr.l.google.com @ns1.google.com

or

dig +short myip.opendns.com @resolver1.opendns.com

these will provide public ip address while ipconfig and ifconfig provide private ip address.