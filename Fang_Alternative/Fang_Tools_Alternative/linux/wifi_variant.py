from termcolor import colored
import subprocess
import platform
import argparse
import time
try:
    import config 
    py2= True
    py3= False
except Exception as e:
    py2= False
    py3= True
    from .config import drop_type
import sys
import csv
import re
import os


global Half, NAME, SAVED_PASSW, name_arg, wifi_name, wifi_pass
Half= ''
Half += ' <[--Dumped-Passwords-<<Wifi>>--]>\n====================================== \n'
wifi_name=''
wifi_pass=''



python= platform.python_version()
if '3' in python:
    print (ERROR+'Python 3 currently not supported.')
    time.sleep(0.8)
    print (SUCCESS+'Exiting Fang...')
    time.sleep(0.8)
    sys.exit()


#----------Color Codex----------|

ERROR= '[-] '    
WAITING= '[?] ' 
SUCCESS= '[+] ' 
NOTICE= '[!] ' 




#-------------------------------------------Wifi-varient Color Codex---------------------------------------------|
try:
    boundry= '| ---- |'
    Network= 'Network: '
    password= 'Password: '
    Header= ' \n\n<[--Dumped-Passwords-<<Wifi>>--]>\n====================================== \n'


    global Full
    Full= ''
    Full += Header
except Exception as e:
    print (ERROR+'Wifi decryption error: '+e)




def csv_output_method( output_format="plain", csv_delimiter=";", csv_quotechar="\""):
    if output_format == "csv":
        Plain_Output_Method= False
        CSV_output_method= True
        tXt_output_method= False
        csv_file= open('Fang-[Wifi Pass].csv', 'w')
        global csv_writer
        csv_writer = csv.DictWriter(
            csv_file, fieldnames=["Network", "password"],
            lineterminator="\n", delimiter=csv_delimiter,
            quotechar=csv_quotechar, quoting=csv.QUOTE_ALL,
        )

        csv_writer.writeheader()
        pass



def text_output_method(name_arg, Password, half):
    global tXt_output_method,wifi_name, wifi_pass 
    Plain_Output_Method= False
    tXt_output_method= True
    CSV_output_method= False

    name_list= name_arg.splitlines()
    pass_list= Password.splitlines()

    raw_output=''

    for wifi_index, wifi_name in enumerate(name_list):
        raw_output+= '''
| ---- | Network:  {0}
| ---- | Password: {1}
| ---- |'''.format(wifi_name,pass_list[wifi_index])

    global Half
    Half += raw_output
    if not Half:
        print (ERROR+'Wifi passwords for {0}[{1}], could not be displayed.')
        return False
    else:
        print ('\n')
        print (WAITING+'Extracting encrypted Wifi credentials....')
        time.sleep(0.8)
        print (WAITING+'Decrypting Wifi credentials....')
        time.sleep(0.8)
        print ('\n')
        print(SUCCESS+"Writing to text file....")
        time.sleep(0.8)

        if os.path.isfile('Fang-[Wifi Pass].txt'):
            with open('Fang-[Wifi Pass].txt','w') as txt_output:
                txt_output.write(Half.strip())
        else :
            with open('Fang-[Wifi Pass].txt','w') as txt_output:
                txt_output.write(Half.strip())
        return True



def plain_output_method(name_arg, Password, Full):
    Plain_Output_Method= True
    tXt_output_method= False
    CSV_output_method= False
    
    name_list= name_arg.splitlines()
    pass_list= Password.splitlines()

    output=''

    for wifi_index, wifi_name in enumerate(name_list):
        output += '''
{0} {1} {2} 
{3} {4} {5} 
{6}'''.format(boundry, Network, wifi_name,boundry, password, pass_list[wifi_index],boundry)
    
    for line in output:
        Full += line

    print ('\n')
    print (WAITING+'Extracting encrypted Wifi credentials....')
    time.sleep(0.8)
    print (WAITING+'Decrypting Wifi credentials....')
    time.sleep(0.8)
    print ('\n')
    print(SUCCESS+"Displaying credentials....")
    time.sleep(0.8)

    print (Full)
    return True




COMMAND_LINUX = "sudo grep -r '^psk=' /etc/NetworkManager/system-connections/"
COMMAND_OSX = "defaults read /Library/Preferences/SystemConfiguration/com.apple.airport.preferences |grep SSIDString"
COMMAND_WINDOWS_GENERIC = "netsh wlan show profile"
RE_LINUX = '/etc/NetworkManager/system-connections/(.*)'
RE_OSX = 'SSIDString = (.*);'
PASS_OSX = 'security find-generic-password -wa '
SAVED_PASSWORDS = dict()


def get_pass_wind_individual(Name):
    output = subprocess.check_output(COMMAND_WINDOWS_GENERIC+" name="+Name+" key=clear",shell=True).decode('utf-8', errors="backslashreplace").split('\n')
    output = re.findall('Key Content(.*)\n',output)[0].strip().split(':')[1].strip()
    return output

def make_pass_dict():
    if os.name=='posix':
        try:
            output = subprocess.check_output(COMMAND_LINUX,shell=True).split('\n')
            for pair in output:
                try:
                    pair = re.findall(RE_LINUX,pair)[0].split(':')
                    Name = pair[0]
                    Pass = pair[1].split('=')[1]
                    SAVED_PASSWORDS[Name]=Pass
                except:
                    pass
        except:
            output = subprocess.check_output(COMMAND_OSX,shell=True).split('\n')
            for pair in output:
                try:
                    Name = re.findall(RE_OSX,pair)[0]
                    Pass = subprocess.check_output(PASS_OSX + Name,shell=True)
                    print ("Getting password for " + Name)
                    SAVED_PASSWORDS[Name] = Pass
                except:
                    pass

    elif os.name =='nt':
        output = subprocess.check_output(COMMAND_WINDOWS_GENERIC,shell=True).split('\n')
        Names = list()
        for name in output:
            name = name.split(':')
            try:
                Names.append(name[1].strip())
            except:
                pass
        for names in Names:
            try:
                Password = get_pass_wind_individual(names)
                SAVED_PASSWORDS[names]=Password
            except:
                pass

def get_passwords(**kwargs):
    if 'ssid' in kwargs:
        if os.name=='nt':
            try:
                Password = get_pass_wind_individual(kwargs['ssid'])
                #print ('Network:',kwargs['ssid'],'|''Password:',Password)
                #-----------------------------------------------------------------------------------------------

                if 'plain' in config.drop_type:
                    plain_output_method (kwargs['ssid'],Password, Full)
                    return 'plain'
#               print (name, SAVED_PASSWORDS[name])
                elif 'txt' in config.drop_type:
                    text_output_method(kwargs['ssid'],Password, Half)
                    return 'txt'
                elif 'csv' in config.drop_type:
                    csv_output_method(
                        output_format= 'csv',
                        csv_delimiter= ';',
                        csv_quotechar= '"',
                        )
                csv_writer.writerow(kwargs['ssid'],Password)
                return 'csv'
            #------------------------------------------------------------------------------------------------------


            except:
                print (ERROR+"No Such SSID exists")
        else:
            #print ('Network:',kwargs['ssid'],'|''Password:',SAVED_PASSWORDS[kwargs['ssid']])
            #-------------------------------------------------------------------------------------------------------

            if 'plain' in config.drop_type:
                plain_output_method (kwargs['ssid'], SAVED_PASSWORDS[kwargs['ssid']], Full)
                return 'plain'
#                print (name, SAVED_PASSWORDS[name])
            elif 'txt' in config.drop_type:
                text_output_method(kwargs['ssid'], SAVED_PASSWORDS[kwargs['ssid']], Half)
                return 'txt'
            elif 'csv' in config.drop_type:
                csv_output_method(
                    output_format= 'csv',
                    csv_delimiter= ';',
                    csv_quotechar= '"',
                    )
                csv_writer.writerow(kwargs['ssid'], SAVED_PASSWORDS[kwargs['ssid']])
                return 'csv'
            else:
                return 
            #--------------------------------------------------------------------------------------------------------


    else:
        NAME= ''
        SAVED_PASSW=''
        for name in SAVED_PASSWORDS.keys():
            NAME += str(name)+'\n' 
            SAVED_PASSW += (SAVED_PASSWORDS[name])+'\n'
        #print NAME, SAVED_PASSW
        name_list= ''
        #print ('Network:',name,'|''Password:',SAVED_PASSWORDS[name])

        if 'plain' in config.drop_type:
            valid= plain_output_method (NAME, SAVED_PASSW, Full)
            if valid:
                return 'plain'
#               print (name, SAVED_PASSWORDS[name])
        elif 'txt' in config.drop_type:
            valid= text_output_method(NAME, SAVED_PASSW, Half)
            if valid:
                return 'txt'
        elif 'csv' in config.drop_type:
            csv_output_method(
                output_format= 'csv',
                csv_delimiter= ';',
                csv_quotechar= '"',
                )
            csv_writer.writerow(NAME, SAVED_PASSW)
            return 'csv'
        #----------------------------------------------------------------------------------------------------------

def main():
    if len(sys.argv) < 2:
        make_pass_dict()
        get_format= get_passwords()
        if get_format== 'plain':
            print ('\n')
            print (SUCCESS+'Wifi passwords from {0}[{1}]'.format(platform.node(), platform.system()))
            time.sleep(0.8)
            print ('\n')
            time.sleep(0.8)
        elif get_format== 'txt':
            print ('\n')
            print (SUCCESS+'Wifi passwords from {0}[{1}]'.format(platform.node(), platform.system()))
            time.sleep(0.8)
            print ('\n')
            print(SUCCESS+"Data written to Fang-[Wifi Pass].txt")
            time.sleep(0.8)
        elif get_format== 'csv':
            time.sleep(0.8)
            print ('\n')
            print(SUCCESS+"Data written to Fang-[Wifi Pass].csv")
            time.sleep(0.8)
        else:
            print ('\n')
            print (ERROR+'Supported output formats ...| csv, txt, plain |...')
            time.sleep(0.8)


    else:

        if os.name=='posix':
            make_pass_dict()
        get_format= get_passwords(ssid=sys.argv[1])
        if get_format== 'plain':
            print ('\n')
            print (SUCCESS+'Wifi passwords from {0}[{1}]'.format(platform.node(), platform.system()))
            time.sleep(0.8)
            print ('\n')
            time.sleep(0.8)
        elif get_format== 'txt':
            print ('\n')
            print (SUCCESS+'Wifi passwords from {0}[{1}]'.format(platform.node(), platform.system()))
            time.sleep(0.8)
            print ('\n')
            print(SUCCESS+"Data written to Fang-[Wifi Pass].txt")
            time.sleep(0.8)
        elif get_format== 'csv':
            time.sleep(0.8)
            print ('\n')
            print(SUCCESS+"Data written to Fang-[Wifi Pass].csv")
            time.sleep(0.8)
        else:
            print ('\n')
            print (ERROR+'Supported output formats ...| csv, txt, plain |...')
            time.sleep(0.8)


if __name__ == "__main__":
    main()

