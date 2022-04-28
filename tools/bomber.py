import os
import time

from sqlalchemy import false, true
printer = '''

\033[1;34;40m 
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
\033[1;34;40m 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
\033[1;31;40m

'''
print(printer)
print("________________________________________________________")
print("|==========|     1. YETANOTHERSMSBOMBER     |==========|")
print("|==========|     2.     XLR8_BOMBER         |==========|")
print("|==========|     3.        TBOMB            |==========|")
print("|==========|     4.       MAILBOMB          |==========|")
print(" |========||==========||==========||==========||======|")
print("|==========|      SELECT 00 TO GO BACK      |==========|")
print("---------------------------------------------------------")
print("\033[1;34;40m ")
bomb = input("|==========||==========|ENTER IN OPTION|==========||==========|>---->")

loop = true
while loop == true:
  if bomb == '1':
    os.system("clear")
    print(printer)
    printer1='''\033[1;31;40m 
      _____________________________________________________________
      |                                                            |
      |    |~~~>1. INSTALL YASMSB     |~~~>2. RUN YASMSB           |
      |                                                            |
      |                  |~~~>00. BACK                             |
      |____________________________________________________________|
          '''
    print(printer1)
    print("\033[1;34;40m ")
    YASMSB = input("|==========||==========|ENTER IN OPTION|==========||==========|>---->")
    if YASMSB == '1':
      os.system("clear")
      os.system("git clone https://github.com/AvinashReddy3108/YetAnotherSMSBomber ; cd YetAnotherSMSBomber ; pip3 install -r requirements.txt ")
    elif YASMSB == '2':
      os.system("clear")
      phone = input("||ENTER TARGET PHONE NUMBER |==========|>---->")
      space =' '
      numsms = input("||ENTER NUMBER OF MESSAGES |==========|>---->")
      print("\033[1;31;40m ")
      os.system("cd YetAnotherSMSBomber ; python3 bomber.py -N  "+ space + numsms + space + phone)
    elif YASMSB == '00':
      loop = false
      os.system("python3 tools/bomber.py")
    else:
      print("\033[1;32;40m ")
      loop = false
      print("INVALID!!")
      

  elif bomb == '2':
    os.system("clear")
    print(printer)
    printer2='''\033[1;31;40m 
     ______________________________________________________________
    |                                                             |
    |     |~~~>1. INSTALL XLR8     |~~~>2. RUN XLR8               |
    |                   |~~~>00. BACK                             |
    |_____________________________________________________________|
          '''
    print(printer2)
    print("\033[1;34;40m")
    XLR8 = input("|==========||==========|ENTER IN OPTION|==========||==========|>---->")
    if XLR8 == '1':
      os.system("clear")
      os.system("git clone https://github.com/anubhavanonymous/XLR8_BOMBER ")
    elif XLR8 =='2':
      os.system("clear")
      os.system("cd XLR8_BOMBER ; sudo python3 xlr8.py ")
    elif XLR8 == '00':
      loop = false
      os.system("python3 tools/bomber.py")
    else:
      print("\033[1;32;40m")
      print("INVALID!!")
    
  elif bomb == '3':
    os.system("clear")
    print(printer)
    printer3='''\033[1;31;40m 
    _______________________________________________________________
    |                                                             |
    |     |~~~>1. INSTALL TBOMB     |~~~>2. RUN TBOMB             |
    |                   |~~~>00. BACK                             |
    |_____________________________________________________________|
          '''
    print(printer3)
    print("\033[1;34;40m")
    TBOMB = input("|==========||==========|ENTER IN OPTION|==========||==========|>---->")
    if TBOMB == '1':
      os.system("clear")
      os.system("git clone https://github.com/TheSpeedX/TBomb")
    elif TBOMB == '2':   
      os.system("clear")
      os.system("cd TBomb ; chmod +x * ; ./TBomb.sh")
    elif TBOMB == '00':
      loop = false
      os.system("python3 tools/bomber.py")
    else:
      print("\033[1;32;40m")
      print("INVALID!!")


  elif bomb == '4':
    os.system("clear")
    os.system("python3 tools/mailbomb.py")

  elif bomb == '00':
    os.system("clear")
    os.system("python3 tools/lobby.py")

  else:
    loop = false
    print("\033[1;32;40m")
    print("INVALID!!")
    

      


