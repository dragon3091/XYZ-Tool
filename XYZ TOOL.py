import os, sys, time
def slowtype(t):
   for D in t + "\n":
   	sys.stdout.write(D)
   	sys.stdout.flush()
   	time.sleep(6/100)
os.system('clear')
###########
print('\033[34m')
print ("""
__  ___   _______  _____ ___   ___  _     
\ \/ \ \ / |__  / |_   _/ _ \ / _ \| |    
 \  / \ V /  / /    | || | | | | | | |    
 /  \  | |  / /_    | || |_| | |_| | |___ 
/_/\_\ |_| /____|   |_| \___/ \___/|_____|""")
slowtype("_____________________________")
slowtype ("\033[31mWELCOM TO V3 OF XYZ TOOL")
print ("__________________")
print("you can download termux starts and important tools and funy tools here")
print("             ")
print("\033[32;10m1-termux start\n2-Metasploit\n3-OSIF\n4-T-Header\n5-Hack cam\n6-DDOS ATTACK\n")
k1 = input ("what do you want: ")
print ("               ")
if k1 == "1" :
	os.system('pkg install root-repo &&apt update  && apt upgrade && apt install git && apt install python && apt install python2 && apt install python3 && pip3 install pip && pip2 install requests && pip2 install mechanize && pkg install ruby && pkg install nano && apt install golang &&apt install havij && apt install wireshark && apt install cmatrix && pkg install figlet && pkg install wget && pkg install wget -y && pkg install python2 -y && apt install wireshark && pkg install cowsay && pkg install toilet && gem install lolcat && pkg install curl && pkg install wgetrc && pkg install unzip && pkg install w3m')
if k1 == "2" :  
    os.system('pkg update && pkg upgrade - y && pkg insatll wget -y && pkg install ruby -y && wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh')
if k1== "3":
    os.system('pkg update&&pkg upgrade&&pkg install python&&pkg install python2&&pkg install git&& git clone https://github.com/CiKu370/OSIF &&cd OSIF&&chmod +x *&&pip2 install -r requirements.txt&&cd osif&&python2 osif.py')
if k1== "4" : 
    os.system("apt update && apt upgrade&&git clone https://github.com/remo7777/T-Header&&cd T-Header&&chmod 777 t-header.sh&&bash t-header.sh&&Type Your Name and yes")
if k1== "5" :
    os.system('pkg update&&pkg upgrade&&pkg install python2&&pkg install python&&pip2 install requests&&pkg install git&&git clone https://github.com/kancotdiq/ipcs&&cd ipcs&&python2 scan.py')
if k1=="6" : 
    os.system('pkg update&&pkg upgrade&&pkg install git&& pkg install python&& pkg install python2&&git clone https://github.com/dragon3091/dragon-ddos-attaack&&cd dragon-ddos-attaack&&python dos dragon.py') 
else : 
    os.system('exit')
