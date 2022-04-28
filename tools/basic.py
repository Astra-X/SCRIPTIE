import os
import time

from sqlalchemy import false, true

def tor1():
    os.system("git clone https://github.com/Und3rf10w/kali-anonsurf")
    time.sleep(2)
    os.system("cd kali-anonsurf ; sudo ./installer.sh")
    time.sleep(10)
    os.system("sudo anonsurf start")
    time.sleep(1)
def ngrok1():
    os.system("curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo 'deb https://ngrok-agent.s3.amazonaws.com buster main' | sudo tee /etc/apt/sources.list.d/ngrok.list && sudo apt update && sudo apt install ngrok  ")
    time.sleep(10)
    os.system("clear")
    print("\033[1;32;40m") 
    ngrok2 = input("|==========||==========|ENTER YOUR AUTHTOKEN|==========||==========|>~~~~>")
    os.system("ngrok authtoken " + str(ngrok2))
    time.sleep(0.9)
    os.system("clear")
    os.system("figlet installed | lolcat ")
    ngrok1()

brow2 = ''' \033[1;32;40m
    ___________________________________________________________
    ~~~~~~~~~~~~~~~~~~~~~~~~  BROWSERS  ~~~~~~~~~~~~~~~~~~~~~~~
    \033[1;31;40m
    |~~~~1.FIREFOX                  |~~~~3.CHROME    
    |~~~~2.TOR                      |~~~~4.OPERA
    '''
    


a = ''' \033[1;32;40m 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[1;31;40m
          .                                                      .
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX    WE ARE CYKASH    Xb       .        dXp     t
dX.    9Xb      .dXb    __      WE ARE WOLVES    dXb.     dXP     .Xb
9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX'   DIE    `98v8P'  HUMAN   `XXP' `9XXXXXXXXXXXP'
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
                              XXXX X.`v'.X XXXX
                              XP^X'`b   d'`X^XX
                              X. 9  `   '  P )X
                              `b  `       '  d'
                               `             '
\033[1;32;40m
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ BASIC TOOLS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`    
_____________________________________________________________________________________
\033[1;31;40m       ~FILES~                                        ~TOOLS~             \033[1;31;40m            |
\033[1;34;40m                                                                        \033[1;31;40m              |
\033[1;34;40m |~~~~1.CREATE A FILE                           |~~~~15.START BURPSUITE  \033[1;31;40m             |       
\033[1;34;40m |~~~~2.REMOVE A FILE                           |~~~~16.START METASPLOIT \033[1;31;40m             |
\033[1;34;40m |~~~~3.CREATE A FOLDER                         |~~~~17.START HYDRA      \033[1;31;40m             |
\033[1;34;40m |~~~~4.REMOVE A FOLDER                         |~~~~18.START JOHN THE RIPPER \033[1;31;40m        |    
\033[1;34;40m |~~~~5.SEE HIDDEN FILES                        |~~~~19.START WIRESHARK     \033[1;31;40m          |
\033[1;34;40m                                                |~~~~20.START OWASP-ZAP     \033[1;31;40m          |
                          \033[1;34;40m                      |~~~~21.START WIFITE        \033[1;31;40m          |
\033[1;31;40m       ~NETWORK~                \033[1;34;40m                |~~~~22.START SET            \033[1;31;40m         | 
\033[1;34;40m |~~~~6.IFCONFIG                                |~~~~23.START SQL-MAP        \033[1;31;40m         |
\033[1;34;40m |~~~~7.ENABLE WLAN                             |~~~~24.START NGROK         \033[1;31;40m          |
\033[1;34;40m |~~~~8.ENABLE WLAN0MON                         |~~~~25.START BROWSER        \033[1;31;40m         |
\033[1;34;40m |~~~~9.DISABLE WLAN                            |~~~~26.START MALTEGO        \033[1;31;40m         |
\033[1;34;40m |~~~~10.DISABLE WLAN0MON                       |~~~~27.START WEBSPLOIT      \033[1;31;40m         |
\033[1;34;40m |~~~~11.CHANGE MAC ADDRESS                                                  \033[1;31;40m         |
\033[1;34;40m |~~~~12.DEFAULT MAC ADDRESS                    |~~~~29.INSTALL NGROK        \033[1;31;40m         |
\033[1;34;40m |~~~~13.TUNNEL THROUGH TOR                     |~~~~30.INSTALL ANONSURF     \033[1;31;40m         |    
\033[1;34;40m |~~~~14.TOR STATUS                             |====00 GO BACK ====|          \033[1;31;40m       |    \033[1;31;40m
'''

print(a)
select2 = input("|==========||==========|ENTER IN OPTION|==========||==========|>---->")

loop = true
while loop == true:
    if select2 == '1':
        going = input("|==========|IN WHICH DIRECTORY U WANT TO CREATE FILE|=======|>---->")
        name =  input("|==========||=======|ENTER YOUR FILE NAME|=======||=========|>---->")
        loop = false
        os.system("nano " + going + name)
        os.system("python3 tools/basic.py")


    elif select2 == '2':
        going2 = input("|==========|IN WHICH DIRECTORY U WANT TO REMOVE FILE|=======|>---->")
        name2 =  input("|==========||=======|ENTER YOUR FILE NAME|=======||=========|>---->")
        loop = false
        os.system("rm " + going2 + name2)
        os.system("python3 tools/basic.py")

    elif select2 == '3':
        going3 =  input("|==========|IN WHICH DIRECTORY U WANT TO CREATE FOLDER|=======|>---->")
        name3 =   input("|==========||=======|ENTER YOUR FOLDER NAME|=======||=========|>---->")
        loop = false
        os.system("mkdir " + going3 + name3 )
        os.system("python3 tools/basic.py")

    elif select2 == '4':
        going4 = input("|==========|IN WHICH DIRECTORY U WANT TO REMOVE FOLDER|=======|>---->")
        name4 =   input("|==========||=======|ENTER YOUR FOLDER NAME|=======||=========|>---->")
        loop = false
        os.system("rm -rf " + going4 + name4)
        os.system("python3 tools/basic.py")

    elif select2 == '5':
        going5 =  input("|==========|IN WHICH DIRECTORY U WANT TO SEE HIDDEN FILES|=======|>---->")
        loop = false
        os.system("ls -ls " + going5)
        os.system("python3 tools/basic.py")

    elif select2 == '6':
        loop = false
        os.system("ifconfig")
        os.system("python3 tools/basic.py")
        

    elif select2 == '7':
        inter = input("|==========|ENTER YOUR DEVICE FLAG|==========|>---->")
        interup = 'up'
        loop = false
        os.system("sudo ifconfig " + inter + interup)
        os.system("python3 tools/basic.py")

    elif select2 == '8':
        inter1 = input("|==========|ENTER YOUR DEVICE FLAG|==========|>---->")  
        loop = false
        os.system("sudo airmon-ng start " + inter1)
        os.system("python3 tools/basic.py")

    elif select2 == '9':
        inter2 = input("|==========|ENTER YOUR DEVICE FLAG|==========|>---->")
        interdown = 'down'
        loop = false
        os.system("sudo ifconfig " + inter2 + interdown)
        os.system("python3 tools/basic.py")

    elif select2 == '10':
        inter3 = input("|==========|ENTER YOUR DEVICE FLAG|==========|>---->")
        loop = false
        os.system("sudo airmon-ng stop" + inter3)
        os.system("python3 tools/basic.py")

    elif select2 == '11':
        inter4 = input("|==========|ENTER YOUR DEVICE FLAG|==========|>---->")
        mac1 = input("|====|ENTER SPOOFED MAC YOU WANT TO SET|=======|>----> ")
        loop = false
        command = '; sudo macchanger --mac ='
        os.system("sudo macchanger -r "+ inter4 + command + mac1)
        os.system("python3 tools/basic.py")
        
    elif select2 == '12':
        inter5 = input("|==========|ENTER YOUR DEVICE FLAG|==========|>---->")
        loop = false
        os.system("sudo macchanger -p " + inter5)
        os.system("python3 tools/basic.py")

    elif select2 == '13':
        os.system("sudo anonsurf start")
        print("|=======||=======|CONGRATULATIONS|==========||==========|")
        print("|=======|=======HERE IS YOUR IP ADDRESS======|=========|")
        loop = false
        os.system("sudo anonsurf myip")
        os.system("python3 tools/basic.py")

    elif select2 == '14':
        print("\n|=======||=======|TOR STATUS|==========||==========|")
        loop = false
        os.system("sudo service tor status")
        os.system("python3 tools/basic.py")

    elif select2 == '30':
        loop = false
        tor1()
        os.system("python3 tools/basic.py")

    elif select2 == '15':
        loop = false
        os.system("burpsuite")
        

    elif select2 == '16':
        loop = false
        os.system("msfconsole")

    elif select2 == '17':
        loop = false
        os.system("sudo hydra")

    elif select2 == '18':
        loop = false
        os.system("johnny")

    elif select2 == '19':
        loop = false
        os.system("wireshark")

    elif select2 == '20':
        loop = false
        os.system("zaproxy")

    elif select2 == '21':
        loop = false
        os.system("sudo wifite")
        
    elif select2 == '22':
        loop = false
        os.system("sudo setoolkit")

    elif select2 == '23':
        loop = false
        os.system("sudo sqlmap")

    elif select2 == '24':
        input1 = input("|==========||==========|ENTER YOUR SERVICE|==========||==========|>~~~>") 
        input2 = input("|==========||==========|  ENTER ANY PORT  |==========||==========|>~~~>")
        space = ' '
        loop = false
        os.system("ngrok " + input1  + space + input2)

    elif select2 == '25':
        print(brow2)
        loop = false
        brow = input("|==========|WHICH BROWSER DO YOU WANT TO OPEN|==========|>~~~>")
        if brow == '1':
            os.system("firefox ")
        elif brow == '2':
            os.system("sudo apt install torbrowser-launcher ")
            time.sleep(5)
            os.system("torbrowser-launcher %u")
        elif brow == '3':
            chrome1 = '''
            ____________________________________________________
                                                                |
            |~~~>1. INSTALL CHROME       |~~~>2. RUN CHROME    |~~~~~~>
            ____________________________________________________|
            '''
            print(chrome1)
            chrome2 = input("|==========||==========|~~~~~~~>")
            if chrome2 == '1':
                os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb ; sudo apt install ./google-chrome-stable_current_amd64.deb")
            elif chrome2 == '2':
                os.system("google-chrome-stable")
        elif brow == '4':
            opera1 = '''
            ____________________________________________________
                                                                |
            |~~~>1. INSTALL OPERA       |~~~>2. RUN OPERA      |~~~~~~>
            ____________________________________________________|
            '''
            print(opera1)
            opera2 = input("|==========||==========|~~~~~~~>")
            if opera2 == '1':
                os.system("wget https://download3.operacdn.com/pub/opera/desktop/60.0.3255.27/linux/opera-stable_60.0.3255.27_amd64.deb ; sudo apt install ./opera-stable_60.0.3255.27_amd64.deb")
            elif opera2 == '2':
                os.system("opera")

    elif select2 == '26':
        print("|==========||==========|STARTING MALTEGO|==========||==========|")
        os.system("maltego")

    elif select2 == '27':
        print("|==========||==========|STARTING WEBSPLOIT|==========||==========|")
        os.system("websploit")

    elif select2 == '00':
        os.system("python3 lobby.py")

else:
    loop = false
    print("INVALID!!")
    os.system("python3 tools/basic.py")