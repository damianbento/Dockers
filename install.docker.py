import os
import socket
import getpass

    

print ('Enter Sudo Password')
sudoPassword = getpass.getpass()

installed = 'apt list | grep docker-ce'
i = os.system('echo %s|sudo -S %s' % (sudoPassword, installed))
if i == 0:
    print ('Docker is installed')
else:
    print ('Docker is not installed')
    aptupdate = 'apt-get update'
    base = 'apt install apt-transport-https ca-certificates curl software-properties-common -y'
    key = 'yes '' | curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -'
    addrepo = 'add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"'
    installdocker = 'apt install docker-ce -y'
    uno = 'usermod -aG docker ${USER}'
    dos = 'su - ${USER}'
    tres = 'id -nG' 
    cuatro = 'usermod -aG docker ${USER}'
    print("Installing Docker modules on",socket.gethostname(),"server" )
    p = os.system('echo %s|sudo -S %s' % (sudoPassword, aptupdate))

resp = input('Install Swarm yes or no: ')
if resp == 'yes' or 'Yes' or 'YES' or 'y' or 'Y':
    print ("install Swarm")

else:
    print ("No install Swarm")
