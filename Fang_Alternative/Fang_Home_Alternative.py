
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # #   
#                                                          #
#  	Fang-[Alternative] is a minified Fang for older	       #
#	windows command prompt e.g Windows 8.1 and lower,      #
#  it give you the full power of Fang without a beautiful  #
#               terminal experience.                       #
#                                                          #
#     /Fang currently supports windows and linux/          #
#													       #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  


 # # # # # # # # # # # # # # # # # # # # # # # # # # # 
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
  # # # # # # # # # # # # # # # # # # # # # # # # # # 

import sys
py_ver= sys.version_info

import time
import platform
if py_ver[0]== 2:
	from Fang_Tools_Alternative.trigger_Alternative import launch
elif py_ver[0]== 3:
	from .Fang_Tools_Alternative.trigger_Alternative import launch

machine_OS= str(platform.system())    
machine_name= platform.node()

time.sleep(1)
Notice= '''\n 
			          NOTICE
		                ----------

It appears you are using an older version of windows as such, due to the nature of your command prompt, you will not have a full colorful Fang experience. Windows 10 so far is the only windows OS which supports colors in command prompt, perharps try the external console 'cmder' ...

		'''
print (Notice)
cnt= input('[Enter to continue]')
if cnt== '':
	pass
else:
	print ('[?] Not "Enter" but... ok')

banner= '''

|===========================================================|
|                                                           |
|                   [!][!] FANG [!][!]                      |
|                                                           |
|                         <<  >>                            |
|                     <<<        >>>                        |
|		       '@                                   |
|                                                           |
|===========================================================|
	Author             : ThefixXxer
	Linkdin            : Ikenna Alfred Managwu
	Follow me on Github: @ThefixXxer

'''

time.sleep(0.8)
print(banner)



if platform.system()== 'Windows':
	header_WIN= ''' 

	=========================================
	  Recover Credentials From Where ??
	==========================================

	[01] Chrome
	[02] Firefox
	[03] Wifi
	[04] All

	'''
	time.sleep(0.8)
	print (header_WIN)

	fang_choice= '  Fang@OS[name]: ~>>> '.replace('OS',machine_OS).replace('name',machine_name)
	fang_choice= input(fang_choice)

	launch(int(fang_choice))



elif platform.system()=='Linux':
	header_LNX= ''' 

	=========================================
	  Recover Credentials From Where ??
	==========================================

	[01] Firefox
	[02] Wifi
	[03] All

	'''
	time.sleep(0.8)
	print (header_LNX)

	fang_choice= '  Fang@OS[name]: ~>>> '.replace('OS',machine_OS).replace('name',machine_name)
	fang_choice= input(fang_choice)

	launch(int(fang_choice))

