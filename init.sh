sudo -i
  #statements
apt-get install python3-pip python-pip
apt-get clean
apt-get autoremove
apt-get update
apt-get install -f
dpkg --configure -a
apt --fix-broken install
