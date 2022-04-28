import os
import time
import getpass

os.system("toilet -f ivrit 'LOGIN' | boxes -d cat -a hc -p h20 | lolcat") 
print("\033[1;32;40m")

correctusername = 'predx'
correctpass = 'predx'
loop ='true'
while loop == 'true':
    username = input(" >~~~~~~~~~~~>ENTER USERNAME(default=shell)>~~~~~~~~~~~>|= ")
    if username == correctusername:
        loop1 ='true'
        while loop1 == 'true':
            password = getpass.getpass(">~~~~~~~~~~~>ENTER PASSWORD(default=shell)>~~~~~~~~~~~>|==")
            if password == correctpass:
                print("logged in successfull")
                time.sleep(1)
                os.system("clear")
                loop ='false'
                loop1 = 'false'
            else:
                print("password incorrect")
    else:
        print("invalid username")

os.system("cd tools ; python3 lobby.py")
