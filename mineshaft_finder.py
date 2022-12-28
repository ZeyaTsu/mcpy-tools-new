import main
import math
import colorama
from colorama import Fore, Back, Style
colorama.init()

instructions_color = Fore.GREEN 
default = Fore.WHITE

def mineshaft():
    print(instructions_color + "No decimals.")
    print("This is a mirroring method to find a second mineshaft once you have one." + default)
    x_coords = int(input("X: "))
    y_coords = int(input("Y: "))
    z_coords = int(input("Z:  "))

    mineshaft_x = x_coords * -1
    mineshaft_z = z_coords * -1

    print(instructions_color + "Mineshaft found!")
    print(f"X: {mineshaft_x} Y: {y_coords} Z: {mineshaft_z}")
    main.main()