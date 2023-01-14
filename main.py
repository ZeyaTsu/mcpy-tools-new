import colorama
from colorama import Fore, Back, Style
import time
import check_config

import features

from configparser import ConfigParser
config = ConfigParser()
config.read("mod.ini")

modded = False
if config.has_section("MOD") == True:
    modded = True
    import features.mcpy_mod


colorama.init()
fc = Fore.CYAN
fb = Fore.BLUE
default = Fore.WHITE

mcpy = """

███╗   ███╗ ██████╗██████╗ ██╗   ██╗       
████╗ ████║██╔════╝██╔══██╗╚██╗ ██╔╝       
██╔████╔██║██║     ██████╔╝ ╚████╔╝        
██║╚██╔╝██║██║     ██╔═══╝   ╚██╔╝         
██║ ╚═╝ ██║╚██████╗██║        ██║          
╚═╝     ╚═╝ ╚═════╝╚═╝        ╚═╝          
                                           
████████╗ ██████╗  ██████╗ ██╗     ███████╗
╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
   ██║   ██║   ██║██║   ██║██║     ███████╗
   ██║   ██║   ██║██║   ██║██║     ╚════██║
   ██║   ╚██████╔╝╚██████╔╝███████╗███████║
   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                           

"""

def menu():
    print(fb+"- - - Finder - - -"+default)
    print("1 · Stronghold Finder | 2 · Mineshaft Finder")

    print(fb+"- - - Vectors - - -"+default)
    print("3 · Volume | 4 · Perimeter | 5 · Distance")

    print(fb+"- - - Other - - -"+default)
    print("6 · Chunk <=> Blocks | 7 · Y Levels for ores | 8 · CanPlace/Destroy command")

    print(fb+"- - - Worlds (File related) - - -"+default)
    print("9 · World level.dat editor/reader | 10 · World stats editor/reader")

    choice = True
    while choice:
        user_choice = str(input("> "))
        match user_choice:
            case '1':
                features.stronghold_finder.stronghold()
                choice = False
            case '2':
                features.mineshaft_finder.mineshaft()
                choice = False
            case '3':
                features.volume.volume()
            case '4':
                features.perimeter.perimeter()
            case '5':
                features.distance.distance()
            case '6':
                features.chunk_blocks.index()
            case '7':
                features.levels_ore.ore()
            case '8':
                features.commands.canplacedestroy()
            case '9':
                features.worlds.nbt_onread()
            case '10':
                features.worlds.stat_onread()
            
                
def main():
    print(fc,mcpy,default)
    check_config.config_checker()
    if modded == False:
        menu()
    else: 
        features.mcpy_mod.mod_main()

if __name__ == '__main__':
    main()