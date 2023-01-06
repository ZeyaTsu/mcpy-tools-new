import main
import math
import colorama
from colorama import Fore, Back, Style
colorama.init()

instructions_color = Fore.GREEN 
default = Fore.WHITE
from nbt import nbt

user_path = None

def nbt_onask():
    print(Fore.RED + "/!\ If the value is a non-decimal number, don't try to edit it with a decimal number.\nExample: Difficulty = 2 (Avoid putting 2.0 or else the file may be corrupted)")
    print(instructions_color + "\nDo you want to edit a value ? y/n/read/export" + default)
    while True:
        user_choice = str(input("> "))
        match user_choice.lower():
            case 'y':
                nbt_onedit()
                break
            case 'n':
                main.main()
                break
            case 'read':
                nbt_onread()
                break
            case 'export':
                nbt_exportfile()
                break

def nbt_exportfile():
    global user_path
    if user_path == None:
        print(instructions_color + "Example. C:\\example\\roaming\\.minecraft\\saves\\myworld" + default)
        user_path = str(input("World's directory (level.dat) > "))
        user_path = user_path + "\\level.dat"

    nbtfile = nbt.NBTFile(user_path, 'rb')

    with open('level_dat_export.txt', 'w+') as file:
        for tag in nbtfile["Data"].tags: 
            export = tag.tag_info()
            file.write('\n'+export)
    print(instructions_color + f"{user_path} was successfully exported as txt." +default)
    nbt_onask()

def nbt_onread():
    global user_path
    if user_path == None:
        print(instructions_color + "Example. C:\\example\\roaming\\.minecraft\\saves\\myworld" + default)
        user_path = str(input("World's directory (level.dat) > "))
        user_path = user_path + "\\level.dat"
 
    nbtfile = nbt.NBTFile(user_path, 'rb')
    
    print(instructions_color, nbtfile, default)
    print(instructions_color, nbtfile["Data"].tag_info(), default)

    for tag in nbtfile["Data"].tags:
        tagname, value = tag.tag_info().split(':')
        print(instructions_color, tagname, f': {Fore.CYAN}', value, default, sep='')

    nbt_onask()
   
def nbt_onedit():
    global user_path
    print(instructions_color + "Which value do you want to edit ?\n(Example:WabderubgTraderSpawnChance)" + default)   
    user_edit_nbt = str(input("> "))
    user_edit_nbt_value = input(f"New {user_edit_nbt} value > ")

    try:
        user_edit_nbt_value = int(user_edit_nbt_value)
    except ValueError:
        try:
            user_edit_nbt_value = float(user_edit_nbt_value)
        except ValueError:
            print(Fore.RED + "     Input cannot be a string")
            nbt_onedit()

    nbtfile = nbt.NBTFile(user_path, 'rb')
    try:
        nbtfile["Data"][user_edit_nbt].value = user_edit_nbt_value
        print(nbtfile["Data"][user_edit_nbt].tag_info())
        nbtfile.write_file(user_path)
    except Exception as e:
        print(Fore.RED, e, default)
    nbt_onask()