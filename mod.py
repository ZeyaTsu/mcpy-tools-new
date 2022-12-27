from configparser import ConfigParser

config = ConfigParser()

version = float(input("Version: "))
features = float(input("Features: "))
mod_name = str(input("Mod name: "))
author = str(input("Author/Team: "))

config["MOD"] = {
    "version": version,
    "features": features,
    "name": mod_name,
    "author": author
}

with open("mod.ini", "w") as f:
    config.write(f)