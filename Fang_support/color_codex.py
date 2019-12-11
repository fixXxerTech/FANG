from termcolor import colored 


#----------Color Codex------------|
ERROR= colored('[-] ','red')     
SUCCESS= colored('[+] ','green') 
NOTICE= colored('[!] ','yellow') 
WAITING= colored('[?] ','blue')  
MAYBE= colored('[=] ','cyan')    
MAYBE2= colored(' [=]','cyan')   

b= '\x1b[1m\x1b[32m=\x1b[0m'
b2='\x1b[1m\x1b[34m|\x1b[0m'
hold='\x1b[1m\x1b[34m[\x1b[0m'
hold2='\x1b[1m\x1b[34m]\x1b[0m'
at="\x1b[1m\x1b[31m'@\x1b[0m"
too='\x1b[1m\x1b[31m>>\x1b[0m'
too2='\x1b[1m\x1b[31m<<\x1b[0m'
lud='\x1b[1m\x1b[33m[!]\x1b[0m'
fangg= "\x1b[1m\x1b[31mFANG\x1b[0m"
fangg= "\x1b[1m\x1b[5m{}\x1b[0m".format(fangg)
list1= '\x1b[1m\x1b[32m01\x1b[0m'
list2= '\x1b[1m\x1b[32m02\x1b[0m'
list3= '\x1b[1m\x1b[32m03\x1b[0m'
list4= '\x1b[1m\x1b[32m04\x1b[0m'

def border_num(number):
	return '{}{}{}'.format(hold,number,hold2)

def display():
	print ('This display function from Color_codex....')

show= 'This id from show var in Color_codex'