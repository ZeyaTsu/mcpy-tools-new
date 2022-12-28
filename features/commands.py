import main
import math
import colorama
from colorama import Fore, Back, Style
colorama.init()

instructions_color = Fore.GREEN 
default = Fore.WHITE

def candestroy():
    blocklist = []
    print(instructions_color + "Write 'DONE' when finish." + default)
    item = str(input("Item: "))
    loop = True
    while loop:
        add = str(input("Can Destroy: "))
        blocklist.append(add)
        if add == "DONE":
            blocklist.pop(len(blocklist) - 1 )
            t = False
    output = ','.join(f"minecraft:{add}" for add in blocklist)
    blank = '"'
    print("/give @s minecraft:" + item + "{CanDestroy:["+ blank + output + blank + "]}")
    main.main()

def canplaceon():
    blocklist = []
    item = str(input("Item: "))
    loop = True
    while loop:
        print("Write 'DONE' when finish.")
        add = str(input("Can Be Placed On: "))
        blocklist.append(add)
        if add == "DONE":
            blocklist.pop(len(blocklist) - 1 )
            t = False
    output = ','.join(f"minecraft:{add}" for add in blocklist)
    blank = '"'
    print("/give @s minecraft:" + item + "{CanPlaceOn:["+ blank + output + blank +"]}")
    main.main()

def canplacedestroy():
    print(instructions_color + "Choose a method." + default)
    print("1 · CanDestroy")
    print("2 · CanPlaceOn")
    loop = True
    while loop:
        user_choice = str(input("> "))
        match user_choice:
            case '1':
                candestroy()
            case '2':
                canplaceon()