import main
import math
import colorama
import json
import time
from colorama import Fore, Back, Style
colorama.init()

section_color = Fore.CYAN
instructions_color = Fore.GREEN 
default = Fore.WHITE
from nbt import nbt

user_path = None
stat_path = None

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
    if user_edit_nbt == "LevelName":
        user_edit_nbt_value = str(input(f"New {user_edit_nbt} name > "))
    else:
        user_edit_nbt_value = input(f"New {user_edit_nbt} value > ")
        try:
            user_edit_nbt_value = int(user_edit_nbt_value)
        except ValueError:
            try:
                user_edit_nbt_value = float(user_edit_nbt_value)
            except ValueError:
                print(Fore.RED + "     Value cannot be a string")
                nbt_onedit()

    nbtfile = nbt.NBTFile(user_path, 'rb')
    try:
        nbtfile["Data"][user_edit_nbt].value = user_edit_nbt_value
        print(nbtfile["Data"][user_edit_nbt].tag_info())
        nbtfile.write_file(user_path)
    except Exception as e:
        print(Fore.RED, e, default)
    nbt_onask()


"""

STATS 

"""

def stat_onask():
    print(Fore.RED + "/!\ If the value is a non-decimal number, don't try to edit it with a decimal number.\n(Avoid putting X.0 or else the file may be corrupted)")
    print(instructions_color + "\nDo you want to edit a value ? y/n/read/export" + default)
    while True:
        user_choice = str(input("> "))
        match user_choice.lower():
            case 'y':
                stat_onedit()
                break
            case 'n':
                main.main()
                break
            case 'read':
                stat_onread()
                break
            case 'export':
                stat_exportfile()
                break

def stat_onread():
    global stat_path
    if stat_path == None:
        print(instructions_color + "Example. C:\\example\\roaming\\.minecraft\\saves\\myworld\\stats\\name_file.json" + default)
        stat_path = str(input("World's (stat) directory > "))
        stat_path_file = str(input("JSON File name (xx.json) (no need to precise .json) > "))
        stat_path = stat_path + "\\" + stat_path_file + ".json"
    try: 
        with open(stat_path, 'r') as f:
            data = json.load(f)
    except Exception as e:
        print(Fore.RED + "Unable to read", stat_path, "> No such directory or file.")
        stat_path = None
        main.main()
    stats = data['stats']

    try:
        mined = stats['minecraft:mined']
        print(section_color + "[Mined]" + default)
        for key, value in mined.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(Fore.RED+"Can't read 'Mined' stats. (maybe it doesn't exist yet)", default)
    try:
        custom = stats['minecraft:custom']
        print(section_color + "\n[Custom]" + default)
        for key, value in custom.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(Fore.RED+"Can't read 'Custom' stats. (maybe it doesn't exist yet)", default)
    try:
        killed = stats['minecraft:killed']
        print(section_color + "\n[Killed]" + default)
        for key, value in killed.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(Fore.RED+"Can't read 'Killed' stats. (maybe it doesn't exist yet)", default)
    try:
        picked_up = stats['minecraft:picked_up']
        print(section_color + "\n[Picked Up]" + default)
        for key, value in picked_up.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(Fore.RED+"Can't read 'Picked Up' stats. (maybe it doesn't exist yet)", default)
    try:
        crafted = stats['minecraft:crafted']
        print(section_color + "\n[Crafted]" + default)
        for key, value in crafted.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(Fore.RED+"Can't read 'Crafted' stats. (maybe it doesn't exist yet)", default)
    try:
        used = stats['minecraft:used']
        print(section_color + "\n[Used]" + default)
        for key, value in used.items():
            print(f"{key}: {value}")  
    except Exception as e:
        print(Fore.RED+"Can't read 'Used' stats. (maybe it doesn't exist yet)", default)

    try:
        used = stats['minecraft:broken']
        print(section_color + "\n[Broken]" + default)
        for key, value in used.items():
            print(f"{key}: {value}")  
    except Exception as e:
        print(Fore.RED+"Can't read 'Broken' stats. (maybe it doesn't exist yet)", default)

    try:
        used = stats['minecraft:dropped']
        print(section_color + "\n[Dropped]" + default)
        for key, value in used.items():
            print(f"{key}: {value}")  
    except Exception as e:
        print(Fore.RED+"Can't read 'Dropped' stats. (maybe it doesn't exist yet)", default)

    try:
        used = stats['minecraft:killed_by']
        print(section_color + "\n[Killed by]" + default)
        for key, value in used.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(Fore.RED+"Can't read 'Killed by' stats. (maybe it doesn't exist yet)", default)

    stat_onask()

def stat_onedit():
    global stat_path

    item_name = str(input("Item name: "))
    new_value = str(input("New value: "))
    section = str(input("Section name (e.g: Used): "))
    item_name.lower()
    section.lower()
    item_name = "minecraft:"+item_name
    section = "minecraft:"+section
    

    with open(stat_path, 'r') as f:
        data = json.load(f)

    if section not in data['stats']:
        print(f"{Fore.RED} MCPY-ERROR > Section {section} not found.", default)
        return

    items = data['stats'][section]
    if item_name not in items:
        print(f"{Fore.RED} MCPY-ERROR > Item {item_name} not found in section {section}.", default)
        return

    items[item_name] = new_value
    with open(stat_path, 'w') as f:
        json.dump(data, f)
    print(f"{instructions_color} Item {item_name} in section {section} has been set to {new_value}.", default)

    stat_onask()

def stat_exportfile():
    global stat_path
    if stat_path == None:
        print(instructions_color + "Example. C:\\example\\roaming\\.minecraft\\saves\\myworld\\stats\\name_file.json" + default)
        stat_path = str(input("World's (stat) directory (xx.json) > "))

    try: 
        with open(stat_path, 'r') as f:
            data = json.load(f)
    except Exception as e:
        print(e)

    with open('stats.txt', 'w+') as f:
        stats = data['stats']

        try:
            mined = stats['minecraft:mined']
            print("Mined:")
            f.write("\nMined:")
            for key, value in mined.items():
                f.write(f"\n{key} : {value}")
                #print(f"{instructions_color} Successfully exported {key} : {value} in stats.txt", default)
                print(f"{instructions_color}█", end="")
                time.sleep(0.01)
        except Exception as e:
            print(Fore.RED + "Can't proceed 'Mined' stats.")

        try:
            custom = stats['minecraft:custom']
            print("\nCustom:")
            f.write("\nCustom:")
            for key, value in custom.items():
                f.write(f"\n{key} : {value}")
                print(f"{instructions_color}█", end="")
                time.sleep(0.01)
                #print(f"{instructions_color} Successfully exported {key} : {value} in stats.txt", default)
        except Exception as e:
            print(Fore.RED + "Can't proceed 'Custom' stats.")

        try: 
            killed = stats['minecraft:killed']
            print("\nKilled:")
            f.write("\nKilled:")
            for key, value in killed.items():
                f.write(f"\n{key} : {value}")
                print(f"{instructions_color}█", end="")
                time.sleep(0.01)
                #print(f"{instructions_color} Successfully exported {key} : {value} in stats.txt", default)
        except Exception as e:
            print(Fore.RED + "Can't proceed 'killed' stats.")

        try:
            picked_up = stats['minecraft:picked_up']
            print("\nPicked Up:")
            f.write("\nPicked Up:")
            for key, value in picked_up.items():
                f.write(f"\n{key} : {value}")
                print(f"{instructions_color}█", end="")
                time.sleep(0.01)
                #print(f"{instructions_color} Successfully exported {key} : {value} in stats.txt", default)
        except Exception as e:
            print(Fore.RED + "Can't proceed 'Picked Up' stats.")

        try:    
            crafted = stats['minecraft:crafted']
            print("\nCrafted:")
            f.write("\nCrafted:")
            for key, value in crafted.items():
                f.write(f"\n{key} : {value}")
                print(f"{instructions_color}█", end="")
                time.sleep(0.01)
                #print(f"{instructions_color} Successfully exported {key} : {value} in stats.txt", default)
        except Exception as e:
            print(Fore.RED + "Can't proceed 'Crafted' stats.")
        
        try:
            used = stats['minecraft:used']
            print("\nUsed:")
            f.write("\nUsed:")
            for key, value in used.items():
                f.write(f"\n{key} : {value}")
                print(f"{instructions_color}█", end="")
                time.sleep(0.01)
                #print(f"{instructions_color} Successfully exported {key} : {value} in stats.txt", default)
        except Exception as e:
            print(Fore.RED + "Can't proceed 'Used' stats.")

        try:
            used = stats['minecraft:broken']
            print("\nBroken:")
            f.write("\nBroken:")
            for key, value in used.items():
                f.write(f"\n{key} : {value}")
                print(f"{instructions_color}█", end="")
                time.sleep(0.01)
                #print(f"{instructions_color} Successfully exported {key} : {value} in stats.txt", default)
        except Exception as e:
            print(Fore.RED + "\nCan't proceed 'Broken' stats.")

        try:
            used = stats['minecraft:dropped']
            print("\nDropped:")
            f.write("\nDropped:")
            for key, value in used.items():
                f.write(f"\n{key} : {value}")
                print(f"{instructions_color}█", end="")
                time.sleep(0.01)
                #print(f"{instructions_color} Successfully exported {key} : {value} in stats.txt", default)
        except Exception as e:
            print(Fore.RED + "\nCan't proceed 'Dropped' stats.")

        try:
            used = stats['minecraft:killed_by']
            print("\nKilled by:")
            f.write("\nKilled by:")
            for key, value in used.items():
                f.write(f"\n{key} : {value}")
                print(f"{instructions_color}█", end="")
                time.sleep(0.01)
                #print(f"{instructions_color} Successfully exported {key} : {value} in stats.txt", default)
        except Exception as e:
            print(Fore.RED + "\nCan't proceed 'Killed by' stats.")
            
        print(f"\n{instructions_color}Succesfully exported {stat_path} into stats.txt" + default)
    stat_onask()