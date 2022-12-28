import main
import math
import colorama
from colorama import Fore, Back, Style
colorama.init()

from configparser import ConfigParser
config = ConfigParser()

instructions_color = Fore.BLUE 
default = Fore.WHITE
modding_color = Fore.GREEN
no_mod = Fore.RED

def config_checker():
    print(instructions_color + "Note: You can add your own features by creating an extension to MCPy-Tools")
    print("However, if you do mod MCPy-Tools don't forget to add your own section by using mod.py")

    config.read("config.ini")
    user = "DEFAULT"
    config_data = config[user]
    version = config_data["version"]
    features = config_data["features"]
    name = config_data["name"]
    author = config_data["author"]

    print(name, version, features, author)
    config.read("mod.ini")
    if config.has_section("MOD") == True:
        mod_data = config["MOD"]
        version = mod_data["version"]
        features = mod_data["features"]
        name = mod_data["name"]
        author = mod_data["author"]

        print(modding_color + "MOD:", name, version, features, author)
    else:
        print(no_mod + "No mod loaded." + default)
        

