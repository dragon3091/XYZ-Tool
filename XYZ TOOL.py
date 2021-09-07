import os
os.system('clear')
import os, sys, time
def slowtype(t):
   for D in t + "\n":
   	sys.stdout.write(D)
   	sys.stdout.flush()
   	time.sleep(6/100)
os.system('clear')
print ("\033[31mXYZ TOOL")
print("_____________")

slowtype ("\033[34;1mWELCOM TO V1 OF XYZ TOOL")
print ("__________________")
print("you can download important tools here")
print("             ")
print("\033[36;1m1-Metasploit\n2-OSIF\n3-T-Header\n4-Hack cam\n")
k1 = input ("what do you want: ")
print ("               ")
if k1 == "1" :  
    print("""\033[32;1mpkg update && pkg upgrade - y

pkg insatll wget

pkg install ruby

wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh

./metasploit.sh

msfconsol""")
if k1== "2":
    print ("""pkg update

pkg upgrade

pkg install python

pkg install python2

pkg install git

git clone https://github.com/CiKu370/0SIF
Is

cd OSIF

Is

chmod +x *

Is
pip2 install -r requirements.txt

Is
cd osif.py

python2 osif.py""")
if k1== "3" : 
    print ("""to Type Your Name in termux 

apt update && apt upgrade



 git clone https://github.com/remo7777/T-Header


 cd T-Header


 chmod 777 t-header.sh


 bash t-header.sh


Type Your Name and yes""")
if k1== "4" :
	print("""pkg update
  pkg upgrade
    pkg install python2
   pkg install python

    pip2 install requests
    pkg install git
   git clone https://github.com/kancotdiq/ipcs
   cd ipcs
   ls
    python2 scan.py""")
else : 
    os.system('exit')
