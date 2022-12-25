import main
import math
import colorama
from colorama import Fore, Back, Style
colorama.init()

instructions_color = Fore.GREEN 
default = Fore.WHITE

def blocks_to_chunks():
    print(instructions_color + "No decimals" + default)
    blocks = int(input("Blocks: "))
    chunks = blocks / 16
    print(instructions_color + f"{blocks} blocks = {chunks} chunk(s)" + default)
    index()

def chunks_to_blocks():
    print(instructions_color + "No decimals" + default)
    chunks = int(input("Chunks: "))
    blocks = chunks * 16
    print(instructions_color + f"{chunks} chunks = {blocks} blocks" + default)
    index()

def index():
    print(instructions_color + "Choose an option" + default)
    print("1 · Blocks to chunks")
    print("2 · Chunks to blocks")
    print("3 · Go back to menu")
    choice = True
    while choice: 
        user_choice = str(input("> "))
        match user_choice:
            case '1':
                blocks_to_chunks()
                choice = False
            case '2':
                chunks_to_blocks()
                choice = False
            case '3':
                main.main()
                choice = False