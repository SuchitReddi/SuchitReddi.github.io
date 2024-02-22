echo "This script is for hosting the github pages site as it is on my raspberry pi"
echo "This script assumes that you are running it from the root of main github site"

echo

cd /var/www/
sudo git clone https://github.com/suchitreddi/suchitreddi.github.io.git
sudo mv suchitreddi.github.io githubpagessite
echo
echo "Cloned main site at \"/var/www/githubpagessite\""

echo

cd githubpagessite
sudo git clone https://github.com/suchitreddi/Notes.git
echo
echo "Cloned Notes folder"

echo

echo "Creating gitpull.sh for automatic updates of the site"
echo "cd /var/www/gitpages && sudo git fetch --all && sudo git reset --hard origin/main && sudo git pull origin main" >> /home/$USER/gitpull.sh
echo "cd /var/www/gitpages/Notes && sudo git fetch --all && sudo git reset --hard origin/main && sudo git pull origin main" >> /home/$USER/gitpull.sh
echo
echo "Created gitpull.sh, edit location of repositories using \"sudo nano /home/$USER/gitpull.sh\""

echo

echo "Add gitpull.sh to crontab by adding this line to \"sudo crontab -e\" : \"*/1 * * * * /home/sherl0ck/tools/nginx/gitpull.sh\""
echo
echo "Visit \"https://suchitreddi.github.io/Work/self_site.html\" for more information on how to host the site."
