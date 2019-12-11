import sys
import time
import platform
from termcolor import colored
from Fang_support.color_codex import *
#from windows import *

machine_OS= platform.system()
python= colored (platform.python_version(),'green')

def launch(command):
	if machine_OS== 'Windows':

		try:
			#from windows import wifi_variant
			from windows import config
			time.sleep(0.8)
			print ('\n')
			print ('Python version: {}'.format(python))
			print ('\n')
			time.sleep(0.8)
			py2= True
			py3= False
		except Exception as e:
			py2= False
			py3= True
			time.sleep(0.8)
			print ('\n')
			print ('Python version: {}'.format(python))
			print ('\n')
			time.sleep(0.8)
			from .windows import config
			#from .windows.wifi_variant import main
			from .windows.chrome_variant import chromedump

		variant= command
		#variant= command.split(' ',1)[0]  # This is proper if 'command' value is a string.
		if variant == 1:
			chrome_PASS= chromedump('active')
			print (chrome_PASS)
			return
		elif variant == 2:
			#Win_Fang.mozilla_variants.drop_type.append('plain')
			if py2:
				from windows import mozilla_variants
			elif py3:
				from .windows import mozilla_variants
			return
		elif variant == 3:
			if py2:
				from windows import wifi_variant
				wifi_variant.main()
			elif py3:
				from .windows.wifi_variant import main
			return
		elif variant == 4:
			time.sleep(0.5)
			print ('\n')
			print (NOTICE+'This option is currently being developed, any contributions are more than welcome!!  :-)')
			time.sleep(1)
			print ('\n')
			sys.exit(SUCCESS+'God speed..')
			#for i in Win_Fang
		else:
			print ('\n')
			print (ERROR+'Invalid Option!')
			return

	elif machine_OS== 'Linux':

		try:
			from linux import wifi_variant
			from linux import config
			time.sleep(0.8)
			print ('\n')
			print ('Python version: {}'.format(python))
			print ('\n')
			time.sleep(0.8)
			py2= True
			py3= False
		except Exception as e:
			#print ('python2 error '+str(e))
			py2= False
			py3= True
			time.sleep(0.8)
			print ('\n')
			print ('Python version: {}'.format(python))
			print ('\n')
			time.sleep(0.8)
			from .linux import config
			from .linux.wifi_variant import main

		variant= command
		#variant= command.split(' ',1)[0]  # This is proper if 'command' value is a string.
		if variant == 1:
			if py2:
				from linux import mozilla_variants
			elif py3:
				from .linux import mozilla_variants
			return
			#Lnx_Fang.mozilla_variants.drop_type.append('plain')
		elif variant == 2:
			if py3:
				main()
			elif py2:
				wifi_variant.main()
			return
		elif variant == 3:
			time.sleep(0.5)
			print ('\n')
			print (NOTICE+'This option is currently being developed, any contributions are more than welcome!!  :-)')
			time.sleep(1)
			print ('\n')
			sys.exit(SUCCESS+'God speed..')
		else:
			print ('\n')
			print (ERROR+'Invalid Option!')
			return