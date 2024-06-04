#!/usr/bin/python3
# GLUP - AN AI ASSISTANT POWERED BY GEMINI
# DEVELOPER - GOSPEL CHUKWUNONSO
import os
from time import sleep
from colorama import Fore, Back

# check if it's a linux or a windows platform, then clear the terminal output
if os.name == 'posix': # linux
   os.system('clear')
else: # windows
   os.system('cls')

#api_key
api_key_glup = "AIzaSyB5Y0jceloOzOUmVGtsrfwxoi-3QTFJRm8"

import google.generativeai as genai
import os

genai.configure(api_key=api_key_glup)

# start glup AI
def start_glup():
    global api_key_glup
    model = genai.GenerativeModel('gemini-1.0-pro-latest')
    user_text = input('Message: ')
    response = model.generate_content(user_text)
    print()
    print(Fore.YELLOW+'Glup:'+Fore.WHITE)
    for text in response.text:
        print(text, end='', flush=True)
        sleep(0.05)
    print()
    print()

try:
    while True:
          start_glup()
except KeyboardInterrupt:
    print(Fore.YELLOW+'\n[+] Thanks for using glup...\n'+Fore.WHITE)
    exit(0)