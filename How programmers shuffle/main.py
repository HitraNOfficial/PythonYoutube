import colorama
from colorama import Fore, Back, Style
import os
import time

def clear():
    os.system('cls') # windows command

def head():
    print(f"     {Fore.GREEN}_\\|/^")
    print(f"      {Fore.GREEN}(_oo")
    print(f"       {Fore.GREEN}|")

def step_one():
    head()
    print(f"      {Fore.GREEN}/|\\/")
    print(f"     {Fore.GREEN}| |")
    print(f"      {Fore.GREEN}/ \\")
    print(f"     {Fore.GREEN}/   \\")
    print(f"    {Fore.GREEN} L    L")

def step_two():
    head()
    print(f"      {Fore.GREEN}/|\\_")
    print(f"     {Fore.GREEN} \\|")
    print(f"      {Fore.GREEN} ||")
    print(f"      {Fore.GREEN} |L")
    print(f"      {Fore.GREEN} L ")

def step_tree():
    head()
    print(f"      {Fore.GREEN}/|\\_")
    print(f"     {Fore.GREEN} \\|")
    print(f"      {Fore.GREEN} ||")
    print(f"      {Fore.GREEN} L|")
    print(f"      {Fore.GREEN}  L ")
    

colorama.init(autoreset=True)

for x in range(100):
    step_one()
    time.sleep(0.18)
    clear()
    step_two()
    time.sleep(0.18)
    clear()
    step_one()
    time.sleep(0.18)
    clear()
    step_tree()
    time.sleep(0.18)
    clear()
