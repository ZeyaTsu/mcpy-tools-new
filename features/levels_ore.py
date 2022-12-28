import main
import math
import colorama
from colorama import Fore, Back, Style
colorama.init()

instructions_color = Fore.GREEN 
default = Fore.WHITE

def ore():
    print(instructions_color + "- - - - - Y Levels - - - - -")
    print("O-Copper: 47-48")
    print("O-Coal: 95-96")
    print("O-Lapis Lazuli: 0")
    print("O.N-Gold: 32 or -64/-16")
    print("O-Redstone: -58 or -64")
    print("O-Diamond: -58 ")
    print("O-Emerald: 256")
    print("N-Quartz: 12-80")
    print("N-Netherite: 11-13")
    print("Note: Gold is more present in Badlands biome or Nether.")
    print("Note: Can be found in negative Y caves.")
    print("N = Nether, O = Overworld." + default)
    main.main()