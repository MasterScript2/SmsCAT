#!/usr/bin/evn python
import os
import time
import colorama
import random
import requests
from colorama import Fore
from time import sleep

class Banner:
	ban_a = "figlet sms_cat"
	ban_b = "toilet \"sms_cat\" --filter border"
	ban_c = "tput setaf 5 && toilet --filter border sms_cat"
	ban_d = "toilet \"sms_cat\" --filter gay"
class C:
	a = Fore.RED
	b = Fore.GREEN
	c = Fore.WHITE
	d = Fore.BLUE
class System:
	clear = "clear"
class License:
	creator = "MasterScript2"
	github = "https://github.com/MasterScript2/"
sys = os.system
clss = time.sleep

random = random.choice([Banner.ban_a, Banner.ban_b, Banner.ban_c, Banner.ban_d])
sys(System.clear)
sys(random)
print(C.a+"creator:", C.b+License.creator, C.b+"github", C.a+License.github)
phone = input(C.a+"\n+phone: "+C.d)
message = input(C.a+"Message: "+C.d)
print("Starting")
clss(1)
responder = requests.post('https://textbelt.com/text', {
	'phone': f'{phone}',
	'message': f'{message}',
	'key': 'textbelt',
	})
user = responder.json()
if user == True:
	print("Ocurrio un error")
else:
	print(C.a+"SEND")
print(C.b+"END")
#Es funcional...