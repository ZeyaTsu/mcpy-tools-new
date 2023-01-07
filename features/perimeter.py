import main
import math
import colorama
from colorama import Fore, Back, Style
colorama.init()

instructions_color = Fore.GREEN 
default = Fore.WHITE

def perimeter():
    print(instructions_color + "No decimals." + default)
    first_x_coords = int(input("From X: "))
    first_y_coords = int(input("From Y: "))
    first_z_coords = int(input("From Z: "))

    second_x_coords = int(input("To X: "))
    second_y_coords = int(input("To Y: "))
    second_z_coords = int(input("To Z: "))

    vector_x = second_x_coords - first_x_coords
    if vector_x < 0:
        vector_x *= -1
    #vector_x += 1

    vector_y = second_y_coords - first_y_coords
    if vector_y < 0:
        vector_y *= -1
    vector_y += 1

    vector_z = second_z_coords - first_z_coords
    if vector_z < 0:
        vector_z *= -1
    #vector_z += 1

    perimeter = ((vector_z + vector_x)*2)*vector_y 
    print(instructions_color + f"The perimeter is {perimeter} blocks" + default)
    main.main()