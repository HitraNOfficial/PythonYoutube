import colorama
from colorama import Fore, Back, Style
import os
import time

def clear():
    os.system('cls') # windows command

def draw_tree(light):
    print(f"      {Fore.YELLOW}  / \\")
    print(f"      {Fore.YELLOW}<     >")
    print(f"       {Fore.YELLOW}|/ \\|")
    print(f"{Fore.GREEN}         *")
    print(f"{Fore.GREEN}        ***")
    print(f"{Fore.GREEN}      {light}*{Back.RESET}*{Fore.CYAN}o{Fore.GREEN}**{light}*{Back.RESET}*")
    print(f"{Fore.GREEN}    *{light}*{Back.RESET}******{Fore.RED}o{Fore.GREEN}**")
    print(f"{Fore.GREEN}      ***{light}*{Back.RESET}***")
    print(f"{Fore.GREEN}    ***{light}*{Back.RESET}*{Fore.BLUE}o{Fore.GREEN}*****")
    print(f"{Fore.GREEN}  **{Fore.RED}q{Fore.GREEN}*****{light}*{Back.RESET}**{Fore.WHITE}p{Fore.GREEN}***")
    print(f"{Fore.GREEN}    ******{Fore.BLUE}o{Fore.GREEN}**{light}*{Back.RESET}*")
    print(f"{Fore.GREEN}  **{Fore.MAGENTA}p{Fore.GREEN}***{light}*{Back.RESET}******{light}*{Back.RESET}*")
    print(f"{Fore.GREEN}*{light}*{Back.RESET}**{Fore.WHITE}o{Fore.GREEN}**{light}*{Back.RESET}******{Fore.RED}q{Fore.GREEN}*{light}*{Back.RESET}**")
    print(f"        {Back.YELLOW}|||")
    print(f"        {Back.YELLOW}|||")

colorama.init(autoreset=True)

for x in range(100):
    clear()
    if x % 2 == 0:
        draw_tree(Back.RED)
    else:
        draw_tree(Back.MAGENTA)
    
    time.sleep(1)
