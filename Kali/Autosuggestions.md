[Back](https://suchitreddi.github.io/Kali/)

for autosuggestions before typing full words:(check web for more accurate description)
apt-get install zsh
apt-get install zsh-syntax-highlighting
apt-get install zsh-autosuggestions
cp ~/.zshrc ~/.zshrcbackup
echo "source $(dpkg -L zsh-autosuggestions | grep 'zsh$')" | tee -a ~/.zshrc
echo "source /usr/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" | tee -a ~/.zshrc
source ~/.zshrc
nano ~/.bashrc
add exec zsh after #for examples in the third line and save

[Back](https://suchitreddi.github.io/Kali/)
