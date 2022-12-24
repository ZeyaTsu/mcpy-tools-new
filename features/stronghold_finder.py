import main
import math
import colorama
from colorama import Fore, Back, Style
colorama.init()

instructions_color = Fore.GREEN 
default = Fore.WHITE



def stronghold():
    print(instructions_color + "Follow the steps to get the correct coordinates.")
    print("1. Go to X:0 and Z:0 (Press F3 to show coordinates)")
    print("2. Throw an ender eye, look at the center of it and look at 'Facing' Section.")
    print("Write down the Facing (North,south,west or east) and the first number after it.")
    print("E.g: Facing: north (Towards negative Z) (xxx <- this number)")
    print("Write that number here. (The most you look to the center of it, the most accurate it is.)" + default)
    print("Decimals are with a . and not ,")
    First_Angle = float(input("> "))
    Facing = str(input("Facing: north/south/east/west > "))
    Facing = Facing.lower()

    match Facing:
        case ("north" | "n"):
            print("Please go to X: 0 Z: -310")
            coords = -310
        case ("south" | "s"):
            print("Please go to X: 0 Z: 310")
            coords = 310
        case ("west" | "w"):
            print("Please go to X: -310 Z:0")
            coords = -310
        case ("east" | "e"):
            print("Please go to X: 310 Z:0")
            coords = 310
    print("Redo the steps above and enter the number you get in the facing section:")
    Second_Angle = float(input("> "))

    final_first_angle = 90 - First_Angle 
    final_second_angle = 90 - Second_Angle

    we_first_angle = First_Angle
    we_second_angle = Second_Angle

    def north_south(final_first_angle, coords, final_second_angle):
        h1 = math.radians(final_first_angle)
        h2 = math.radians(final_second_angle)

        xNorthFind = -(coords / (math.tan(h1) - math.tan(h2)))
        zNorthFind = (coords * math.tan(h1)) / (math.tan(h1) - math.tan(h2))

        print(instructions_color + "Stronghold found!")
        print("X:", xNorthFind, "Z:", zNorthFind)
        print("Note: If you don't find the stronghold on those coordinates, it may be around of that area.")
        main.main()

    def west_east(we_first_angle, coords, we_second_angle):
        h3 = math.radians(we_first_angle)
        h4 = math.radians(we_second_angle)

        xWestFind = (coords * math.tan(h3)) / (math.tan(h3) - math.tan(h4))
        zWestFind = -(coords / (math.tan(h3) - math.tan(h4)))

        print(instructions_color + "Stronghold found!")
        print("X:", xWestFind, "Z:", zWestFind)
        print("Note: If you don't find the stronghold on those coordinates, it may be around of that area.")
        main.main()

    match Facing:
        case ("north" | "south" | "n" | "s"):
            north_south(final_first_angle, coords, final_second_angle)
        case ("west" | "east" | "w" | "e"):
            west_east(we_first_angle, coords, we_second_angle)