import time
import platform 
import subprocess
from termcolor import colored


#----------Color Codex------------|
ERROR= colored('[-] ','red')     #|
SUCCESS= colored('[+] ','green') #|
WAITING= colored('[?] ','blue')  #|


def global_vars():
	global msg, raw_msg, boundry, Network, password

	msg = ''
	raw_msg= ''

	boundry= colored('| ---- | ','red')
	Network= colored('Network: ','green')
	password= colored('Password: ','cyan')
	msg += colored('<[--Dumped-Passwords-<<Wifi>>--]>\n======================================= \n','green')
	raw_msg += '<[--Dumped-Passwords-<<Wifi>>--]>\n======================================= \n'

def credentials(network, password):
	info_list= []
	info_list.append({
		u'Network': network,
		u'password': str(password)
		})
	return info_list

def plain_output_method(info, msg):
	for creds in info:
		msg += u'\n{0} {1} {2}'.format(boundry, Network, creds['Network'])#.encode('ascii','ignore'))
		msg += u'\n{0} {1} {2}'.format(boundry, password, creds['password'])#.encode('ascii','ignore'))
		msg += u'\n{0}'.format(boundry)

	return (msg)

def txt_output_method(info, raw_msg):
	for creds in info:
		raw_msg += u'\n| ---- | Network: {}'.format(creds['Network'])#.encode('ascii','ignore'))
		raw_msg += u'\n| ---- | Password: {}'.format(creds['password'])#.encode('ascii','ignore'))
		raw_msg += u'\n| ---- | '
	
	return raw_msg



def main():
	try:
		global_vars()
		data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
		profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
		
		msg=''
		raw_msg= ''
		assembled_creds= ''
		
		header = colored('\n\n<[--Dumped-Passwords-<<Wifi>>--]>\n======================================= \n','green')
		raw_header = '\n\n<[--Dumped-Passwords-<<Wifi>>--]>\n======================================= \n'
		
		for i in profiles:
		    try:
		        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
		        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
		        try:
		        	#print ("{:<30}|  {:<}".format(i, results[0]))
		        	info= credentials(i, results[0])
		        	assembled_creds += plain_output_method(info, msg)
		        except IndexError:
		            #print ("{:<30}|  {:<}".format(i, ""))
		        	info= credentials(i, "None")
		        	assembled_creds += plain_output_method(info, msg)
		    except subprocess.CalledProcessError:
		    	#print ("{:<30}|  {:<}".format(i, "ENCODING ERROR"))
		        info= credentials(i, "ENCODING ERROR")
		        assembled_creds += plain_output_method(info, msg)

		print (SUCCESS+'Wifi passwords from Machine: [{0}]--[{1}]'.format(platform.node(), platform.system()))
		time.sleep(0.8)
		print (WAITING+'Extracting Wifi credentials....')
		time.sleep(0.8)
		print (WAITING+'Sorting Wifi credentials....')
		time.sleep(0.8)
		print (SUCCESS+'Displaying credentials....')
		time.sleep(0.8)
		print (header+assembled_creds)
		# Conditional for text output,
			# Text writer function.

	except Exception as wireless_pass_err:
		print ('\n')
		print (ERROR+'Error retrieving wifi-creditials.\nReason: {}'.format(wireless_pass_err))

	#input("")

main()