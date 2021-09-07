import os, sys, time
def slowtype(t):
   for D in t + "\n":
   	sys.stdout.write(D)
   	sys.stdout.flush()
   	time.sleep(6/100)
os.system('clear')
############
print('\033[33m')
print ("""
__  ___   _______  _____ ___   ___  _     
\ \/ \ \ / |__  / |_   _/ _ \ / _ \| |    
 \  / \ V /  / /    | || | | | | | | |    
 /  \  | |  / /_    | || |_| | |_| | |___ 
/_/\_\ |_| /____|   |_| \___/ \___/|_____|""")
slowtype("_____________________________")
slowtype ("\033[33;1mWELCOM TO V1 OF XYZ TOOL")
print ("__________________")
print("you can download important tools here")
print("             ")
print("\033[36;1m1-Metasploit\n2-OSIF\n3-T-Header\n4-Hack cam\n")
k1 = input ("what do you want: ")
print ("               ")
if k1 == "1" :  
 os.system('pkg update && pkg upgrade - y && pkg insatll wget -y && pkg install ruby -y && wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh')
if k1== "2":
   os.system('pkg update&&pkg upgrade&&pkg install python&&pkg install python2&&pkg install git&&git clone https://github.com/CiKu370/0SI F&&cd OSIF&&chmod +x *&&pip2 install -r requirements.txt&&cd osif.py&&python2 osif.py')
if k1== "3" : 
    os.system("apt update && apt upgrade&&git clone https://github.com/remo7777/T-Header&&cd T-Header&&chmod 777 t-header.sh&&bash t-header.sh&&Type Your Name and yes")
if k1== "4" :
	os.system('pkg update&&pkg upgrade&&pkg install python2&&pkg install python&&pip2 install requests&&pkg install git&&git clone https://github.com/kancotdiq/ipcs&&cd ipcs&&python2 scan.py')
else : 
    os.system('exit')
