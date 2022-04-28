import os
import time

from sqlalchemy import false, true

os.system("toilet -f ivrit 'PHISHING' | boxes -d cat -a hc -p h20 | lolcat ")
phish = '''\033[1;31;40m 

><><|~~~~1.SEEKER
><><|~~~~2.ZPHISHER
><><|~~~~3.BLACKEYE
><><|~~~~4.SOCIALPHISH

><><|~~~~00.BACK
'''
print(phish)
print("\033[1;34;40m ")
select = input("|==========||==========|ENTER IN OPTION|==========||==========|>---->")

loop = true
while loop == true:
    if select == '1':
        os.system("clear")
        phish1='''\033[1;31;40m 
        _____________________________________________________________
                                                                    |
                |~~~>1. INSTALL SEEKER       |~~~>2. RUN SEEKER    |~~~~~~>
        ____________________________________________________________|
            '''
        print(phish1)
        print("\033[1;34;40m ")
        input1 = input("|==========||==========|ENTER IN OPTION|==========||==========|>---->")
        if input1 == '1':
            os.system("git clone https://github.com/thewhiteh4t/seeker ; cd seeker ; sudo ./install.sh ")
        
        elif input1 == '2':
            loop = false
            os.system("python3 tools/seeker/seeker.py")

        else:
            print("INVALID!!")

    elif select == '2':
        os.system("clear")
        phish2='''\033[1;31;40m 
        _____________________________________________________________
                                                                    |
                |~~~>1. INSTALL ZPHISHER   |~~~>2. RUN ZPHISHER    |~~~~~~>
        ____________________________________________________________|
            '''
        print(phish2)
        print("\033[1;34;40m ")
        input2 = input("|==========||==========|ENTER IN OPTION|==========||==========|>---->")
        if input2 == '1':
            os.system("git clone https://github.com/htr-tech/zphisher ; cd zpshiher ; chmod +x * ; ./zphisher.sh ")
        elif input2 == '2':
            loop = false
            os.system("cd zphisher ; ./zphisher.sh ")

        else:
            print("INVALID!!")
            

    elif select == '3':
        os.system("clear")
        phish3='''\033[1;31;40m 
        _____________________________________________________________
                                                                    |
                |~~~>1. INSTALL BLACKEYE   |~~~>2. RUN BLACKEYE    |~~~~~~>
        ____________________________________________________________|
            '''
        print(phish3)
        print("\033[1;34;40m ")
        input3 = input("|==========||==========|ENTER IN OPTION|==========||==========|>---->")
        if input3 == '1':
            os.system("git clone https://github.com/An0nUD4Y/blackeye ; cd blackeye ;chmod +x * ; bash blackeye.sh")
        elif input3 == '2':
            loop = false
            os.system('cd blackeye ; bash blackeye.sh')
        else:
            print("INVALID!!")


    elif select == '4':
        os.system("clear")
        phish4='''\033[1;31;40m 
        _____________________________________________________________
                                                                    |
                |~~~>1. INSTALL SF         |~~~>2. RUN SF          |~~~~~~>
        ____________________________________________________________|
            '''
        print(phish4)
        print("\033[1;34;40m ")
        input4 = input("|==========||==========|ENTER IN OPTION|==========||==========|>---->")
        if input4 == '1':
            os.system('git clone https://github.com/xHak9x/SocialPhish ; cd SocialPhish ; chmod +x * ; ./socialphish.sh ')
        elif input4 == '2':
            loop = false
            os.system("cd SocialPhish ; chmod +x * ; ./socialphish.sh")
        else:
            print("INVALID!!")


    elif select == '00':
        os.system("python3 lobby.py")


else:
    print("INVALID!!")
    os.system("python3 tools/phish.py")

