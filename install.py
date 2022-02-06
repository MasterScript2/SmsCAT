import os
import time
import colorama
from os import system as sys
from colorama import Fore

print(Fore.RED+"["+Fore.YELLOW+"*"+Fore.RED+"]"+Fore.WHITE+"Descargando paquetes bash")
time.sleep(0.2)
print(Fore.RED+"["+Fore.YELLOW+"*"+Fore.RED+"]"+Fore.WHITE+"Instalando Figlet")
sys("apt -y install figlet")
print(Fore.RED+"["+Fore.YELLOW+"*"+Fore.RED+"]"+Fore.WHITE+"Instalando toilet")
sys("apt -y install toilet")
print(Fore.BLUE+"Iniciando descarga de librerias necesarias | requirements.txt"+Fore.WHITE)
sys("python3 -m pip install -r requirements.txt")
print(Fore.RED+"INSTALACION COMPLETADA ...Espera")
time.sleep(2)
os.system("python3 run.py")