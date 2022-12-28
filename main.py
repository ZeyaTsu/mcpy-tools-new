import colorama
from colorama import Fore, Back, Style
import time
import check_config

import features.stronghold_finder
import features.mineshaft_finder
import features.chunk_blocks
import features.distance
import features.volume
import features.perimeter
import features.levels_ore
import features.commands

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

           .----------------.  .----------------.  .----------------.  .----------------.           
          | .--------------. || .--------------. || .--------------. || .--------------. |          
          | | ____    ____ | || |     ______   | || |   ______     | || |  ____  ____  | |          
          | ||_   \  /   _|| || |   .' ___  |  | || |  |_   __ \   | || | |_  _||_  _| | |          
          | |  |   \/   |  | || |  / .'   \_|  | || |    | |__) |  | || |   \ \  / /   | |          
          | |  | |\  /| |  | || |  | |         | || |    |  ___/   | || |    \ \/ /    | |          
          | | _| |_\/_| |_ | || |  \ `.___.'\  | || |   _| |_      | || |    _|  |_    | |          
          | ||_____||_____|| || |   `._____.'  | || |  |_____|     | || |   |______|   | |          
          | |              | || |              | || |              | || |              | |          
          | '--------------' || '--------------' || '--------------' || '--------------' |          
           '----------------'  '----------------'  '----------------'  '----------------'           
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  _________   | || |     ____     | || |     ____     | || |   _____      | || |    _______   | |
| | |  _   _  |  | || |   .'    `.   | || |   .'    `.   | || |  |_   _|     | || |   /  ___  |  | |
| | |_/ | | \_|  | || |  /  .--.  \  | || |  /  .--.  \  | || |    | |       | || |  |  (__ \_|  | |
| |     | |      | || |  | |    | |  | || |  | |    | |  | || |    | |   _   | || |   '.___`-.   | |
| |    _| |_     | || |  \  `--'  /  | || |  \  `--'  /  | || |   _| |__/ |  | || |  |`\____) |  | |
| |   |_____|    | || |   `.____.'   | || |   `.____.'   | || |  |________|  | || |  |_______.'  | |
| |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
"""

def menu():
    print(fb+"- - - Finder - - -"+default)
    print("1 · Stronghold Finder")
    print("2 · Mineshaft Finder")

    print(fb+"- - - Vectors - - -"+default)
    print("3 · Volume")
    print("4 · Perimeter")
    print("5 · Distance")

    print(fb+"- - - Other - - -"+default)
    print("6 · Chunk <=> Blocks")
    print("7 · Y Levels for ores")
    print("8 · CanPlace/Destroy command")

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
            
                
def main():
    print(fc,mcpy,default)
    check_config.config_checker()
    if modded == False:
        menu()
    else: 
        features.mcpy_mod.mod_main()

if __name__ == '__main__':
    main()