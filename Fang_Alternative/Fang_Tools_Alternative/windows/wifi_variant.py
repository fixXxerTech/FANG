import time
import platform
import subprocess
#from termcolor import colored



def credentials(header, network, password):
	info_list= []
	info_list.append({
		u'Header': header,
		u'Network': network,
		u'password': str(password)
		})
	return info_list


def plain_output_method(info, raw_msg):
	for creds in info:
		raw_msg += u'\n| ---- | Network: {}'.format(creds['Network'])#.encode('ascii','ignore'))
		raw_msg += u'\n| ---- | Password: {}'.format(creds['password'])#.encode('ascii','ignore'))
		raw_msg += u'\n| ---- | '

	return raw_msg


#def txt_output_method(info, raw_msg):
	#for creds in info:
	#	raw_msg += u'\n| ---- | Network: {}'.format(creds['Network'].encode('ascii','ignore'))
	#	raw_msg += u'\n| ---- | Password: {}'.format(creds['password'].encode('ascii','ignore'))
	#	raw_msg += u'\n| ---- | '
	
	#return raw_msg.



def main():
	try:
		raw_msg= ''

		assembled_creds= ''

		header= '\n\n<[--Dumped-Passwords-<<Wifi>>--]>\n======================================= \n'

		data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
		profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
		for i in profiles:
		    try:
		        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
		        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
		        try:
		            #print ("{:<30}|  {:<}".format(i, results[0]))
		            info= credentials(header, i, results[0])
		            assembled_creds += plain_output_method(info, raw_msg)
		        except IndexError:
		            #print ("{:<30}|  {:<}".format(i, ""))
		            info= credentials(header, i, "None")
		            assembled_creds += plain_output_method(info, raw_msg)
		    except subprocess.CalledProcessError:
		        #print ("{:<30}|  {:<}".format(i, "ENCODING ERROR"))
		        info= credentials(header, i, "ENCODING ERROR")
		        assembled_creds += plain_output_method(info, raw_msg)

		print ('[+] Wifi passwords from Machine: [{0}]--[{1}]'.format(platform.node(), platform.system()))
		time.sleep(0.8)
		print ('[?] Extracting Wifi credentials....')
		time.sleep(0.8)
		print ('[?] Sorting Wifi credentials....')
		time.sleep(0.8)
		print ('[+] Displaying credentials....')
		time.sleep(0.8)
		print (header+assembled_creds)
		# Conditional for text output,
			# Text writer function
			
	except Exception as wireless_pass_err:
		print ('\n')
		print ('[-] Error retrieving wifi-creditials.\nReason: {}'.format(wireless_pass_err))

	#input("")

main()