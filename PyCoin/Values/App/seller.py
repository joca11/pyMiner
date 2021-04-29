import random
import colorama
from colorama import Fore
import time
colorama.init()
nothing = 0
mrmot = "@FFfu8903un2087y#O$Nuf"

f = open("basics21341234.txt","r")
coins = f.read()
print (Fore.CYAN)
print(coins+" - Balance")
buyer = input ("Enter Buyer ID: ")
print("WARNING U WILL SEND WHOLE BALANCE!")
send = input ('Are U sure u want to  send: ')
coin = f.read()
if (buyer==mrmot):
    print("Sending Statred. . .")
    time.sleep(10)
    g = open("basics21341234.txt","w")
    g.write(str(nothing))
    print("Done!")
    time.sleep(2345)
else:
    print("Wrong ID!")
    time.sleep(234)
    
