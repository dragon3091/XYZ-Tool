import os, sys, time
def slowtype(t):
   for D in t + "\n":
   	sys.stdout.write(D)
   	sys.stdout.flush()
   	time.sleep(6/100)
os.system('clear')
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0m"     # White
R = "\033[31m"    # Red
PU = "\033[2;35m" #purple
print(GG)
print ("""
__  ___   _______  _____ ___   ___  _     
\ \/ \ \ / |__  / |_   _/ _ \ / _ \| |    
 \  / \ V /  / /    | || | | | | | | |    
 /  \  | |  / /_    | || |_| | |_| | |___ 
/_/\_\ |_| /____|   |_| \___/ \___/|_____|""")
slowtype("_____________________________")
print ("")
slowtype (PU+"WELCOM TO V4 OF XYZ TOOL")
print ("__________________")
print("IN HERE, YOU CAN DOWNLOAD TERMUX START / METASPLOI/ A LOT OFTOOLS")
print("             ")
print(R+"1-Termux Start\n2-Metasploit\n3-OSIF\n4-T-Header\n5-Hack cam\n6-DDOS ATTACK\n7-HxWhatsapp\n8-Facebook Report\n9-lazy max\n10-Termux-Banner")
print ("")
k1 = input ("WHAT DO YOU INSTALL : ")
print ("               ")
if k1 == "1" :
	os.system('pkg install root-repo &&apt update  && apt upgrade && apt install git && apt install python && apt install python2 && apt install python3 && pip3 install pip && pip2 install requests && pip2 install mechanize && pkg install ruby && pkg install nano && apt install host && apt install golang &&apt install havij && apt install wireshark && apt install cmatrix && pkg install figlet && pkg install wget && pkg install wget -y && pkg install python2 -y && apt install wireshark && pkg install cowsay && pkg install toilet && gem install lolcat && pkg install curl && pkg install wgetrc && pkg install unzip && pkg install w3m')

if k1 == "2" :  
    os.system('pkg update && pkg upgrade - y && pkg insatll wget -y && pkg install ruby -y && wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh')
if k1== "3":
    os.system('pkg update&&pkg upgrade&&pkg install python&&pkg install python2&&pkg install git&& git clone https://github.com/CiKu370/OSIF &&cd OSIF&&chmod +x *&&mv OSIF $HOME')
if k1== "4" : 
    os.system("apt update && apt upgrade&&git clone https://github.com/remo7777/T-Header&&cd T-Header&&chmod 777 t-header.sh&&bash t-header.sh")
if k1== "5" :
    os.system('pkg update&&pkg upgrade&&pkg install python2&&pkg install python&&pip2 install requests&&pkg install git&&git clone https://github.com/kancotdiq/ipcs&&mv ipcs $HOME')
if k1=="6" : 
    os.system('pkg update&&pkg upgrade&&pkg install git&& pkg install python&& pkg install python2&&git clone https://github.com/dragon3091/dragon-ddos-attaack&& mv dragon-ddos-attaack $HOME ') 
if k1=="7" :
	os.system("pkg update&&pkg upgrade&&pkg install python&&pkg install python2&&pkg install git&& git clone https://github.com/Bl4ckDr460n/HxWhatsApp&& mv HxWhatsApp $HOME")
if k1=="8" :
	os.system("pkg update&&pkg upgrade&& pkg install python&&pkg insatll unzip&&pkg install git&&git clone https://github.com/IlayTamvan/Report&&cd Report && unzip Report.zip&&chmod +x Report.py&&mv Report $HOME ")
if k1 =="9" :
	os.system("pkg update&&pkg upgrade&&pkg install git&&pkg install python&& git clone https://github.com/Gameye98/Lazymux&& python2 lazymax.py&&mv Lazymux $HOME")
if k1 =="10" :
	os.system("pkg update&&pkg upgrade&&pkg install git&&https://github.com/Bhai4You/Termux-Banner&& chmod +x requirement.sh&& chmod +x t-ban.sh&& bash requirement.sh&& bash t-ban.sh")
else : 
    os.system('exit')
 
