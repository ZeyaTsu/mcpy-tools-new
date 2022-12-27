import main
import math
import colorama
from colorama import Fore, Back, Style
colorama.init()

instructions_color = Fore.GREEN 
default = Fore.WHITE

def distance():
    print(instructions_color + "No decimals." + default)
    first_x_coords = int(input("from X: "))
    first_z_coords = int(input("from Z: "))
    second_x_coords = int(input("to X: "))
    second_z_coords = int(input("to Z: "))
    walking_method = str(input("Elytra/Running: "))
    walking_method = walking_method.lower()
    match walking_method:
        case ("running" | "run" | "r"):
            vel = 5.6
        case ("elytra" | "fly" | "e"):
            vel = 7.2
        
    vector_x = second_x_coords - first_x_coords
    if vector_x < 0:
        vector_x *= -1
    vector_x += 1

    vector_z = second_z_coords - first_z_coords
    if vector_z < 0:
        vector_z *= -1
    vector_z += 1

    distance = int(math.sqrt((vector_x - 2)**2 + (vector_z -2)**2))
    time = distance // vel
    print(f"From X:{first_x_coords} Z:{first_z_coords} To X:{second_x_coords} Z:{second_z_coords}")
    print(f"There are {vector_x + vector_z} blocks.")
    print(f"It takes around {time} seconds or {time//60} minutes.")
    main.main()