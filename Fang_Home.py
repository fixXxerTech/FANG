
# # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#	Name: Fang [ No full meaning ;-] ]      		  #
#	Author: ThefixXxer [Managwu Ikenna Alfred]		  #
#	Description: Fang is a password recovery utility  #
#				 built in python for decryption and   #
#                recovery of misplaced logins.        #
#                [that can really be frustrating!!! ] #
#				 									  #
#    /Fang currently supports windows and linux/      #
#													  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#  					  DISCLAMER:                      #
#					 ------------					  #
#  NOTE!!: Fang was not designed as a trojan rather   #
#	       a utility to aid in the recovery of 	      #
#		   misplaced login credentials from personal  #
#          owned PCs, use and modify with regard to   #
#          the terms of GNU public license.           #
#	 												  #
#  	Please stay legal.								  #
#                                    	 			  #
#	       /Mac-OS support comming soon/ 	          #
#													  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # #


import time
import platform
from termcolor import colored
from Fang_tools.trigger import launch
from Fang_support.color_codex import *
#try:
#	from Fang_support.color_codex import *
#	py2= True
#	py3= False
#except:
#	py2= False
#	py3= True
#	print ('In python3 ')
#	from .Fang_support.color_codex import *



one= border_num(list1)
two= border_num(list2)
three= border_num(list3)
four= border_num(list4)


machine_OS= colored(str(platform.system()),'green')
machine_name= '\x1b[1m\x1b[34m{}\x1b[0m'.format(platform.node())

old_cmd= ['8.1','8','7','XP','Vista']
if platform.system()== 'Windows':
	if platform.release() in old_cmd:
		from Fang_Alternative import Fang_Home_Alternative
	#import Fang_Alternative.Fang_Home_Alternative


banner= '''

|====================================================================|
|                                                                    |
|                       [!][!] FANG [!][!]                           |
|                                                                    |
|                             <<  >>                                 |
|                         <<<        >>>                             |
|			    '@                                       |
|                                                                    |
|====================================================================|
		Author             : ThefixXxer
		Version            : 1.0.0
		Linkdin            : Ikenna Alfred Managwu
		Follow me on Github: @ThefixXxer
'''.replace('=',b).replace('|',b2).replace("'@",at).replace('<<',too2).replace('[!]',lud).replace('FANG',fangg).replace('Author',colored('Author', 'red')).replace('Version',colored('Version', 'red')).replace('Linkdin',
	colored('Linkdin', 'red')).replace('Follow me on Github',colored('Follow me on Github', 'red')).replace('ThefixXxer',colored('ThefixXxer', 'green')).replace('1.0.0',colored('1.0.0', 'green')).replace('Ikenna Alfred Managwu',
	colored('Ikenna Alfred Managwu', 'green')).replace(':',colored(':', 'yellow')).replace("@ThefixXxer",colored("@ThefixXxer", 'green'))

time.sleep(0.8)
print(banner)



if platform.system()== 'Windows':
	header_WIN= colored(''' 

	=========================================
	  Recover Credentials From Where ??
	==========================================

	[01] Chrome
	[02] Firefox
	[03] Wifi
	[04] All

	''','magenta').replace('[01]',one).replace('[02]',two).replace('[03]',three).replace('[04]',four).replace('Chrome',colored('Chrome','magenta')).replace('Firefox',colored('Firefox','magenta')).replace('Wifi',colored('Wifi','magenta')).replace('All',colored('All','magenta'))
	time.sleep(0.8)
	print (header_WIN)

	fang_choice= '  Fang@OS[name]: ~>>> '.replace('OS',machine_OS).replace('name',machine_name).replace('@',at).replace('Fang',colored('Fang','blue'))
	fang_choice= input(fang_choice)

	launch(int(fang_choice))



elif platform.system()=='Linux':
	header_LNX= colored(''' 

	=========================================
	  Recover Credentials From Where ??
	==========================================

	[01] Firefox
	[02] Wifi
	[03] All

	''','magenta').replace('[01]',one).replace('[02]',two).replace('[03]',three).replace('[04]',four).replace('Chrome',colored('Chrome','magenta')).replace('Firefox',colored('Firefox','magenta')).replace('Wifi',colored('Wifi','magenta')).replace('All',colored('All','magenta'))
	time.sleep(0.8)
	print (header_LNX)

	fang_choice= '  Fang@OS[name]: ~>>> '.replace('OS',machine_OS).replace('name',machine_name).replace('@',at).replace('Fang',colored('Fang','blue'))
	fang_choice= input(fang_choice)

	launch(int(fang_choice))
