import time
import sys
import os


def welcome():
    a = '''\033[1;31;40m 


><><|~~~~1.BASIC TOOLS
><><|~~~~2.PHISHER TOOLS
><><|~~~~3.BOMBING TOOLS
><><|~~~~4.IP TOOLS'''
    print(a)
welcome()
print("\033[1;34;40m ")
select1 = input("|==========||==========|ENTER IN OPTION|==========||==========|>---->")
if select1 == '1':
    os.system("clear")
    os.system("python3 basic.py")
elif select1 == '4':
    os.system("clear")
    os.system("python3 ipa.py")
elif select1 == '2':
    os.system("clear")
    os.system("python3 phish.py")
elif select1 == '3':
    os.system("clear")
    os.system("python3 bomber.py")
else:
    print("\033[1;32;40m")
    print("INVALID!!")
    os.system("python3 lobby.py")
    os.system("clear")



    
