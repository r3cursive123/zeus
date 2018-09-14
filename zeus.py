import os
from sys import platform
import ssl_auditor
import soc_dates
import file_parse

# NEED TO FIX ISSUE WHEN YOU CHOOSE ANOTHER OPTION OTHER THAN SOC DATE GENERATOR - DEFAULTS FAIL!!!!

# Additional packages required for full functionality:
#   [] nmap must be installed on the machine (ssl audit)
#           - if you are on Windows - please add nmap to your System Env Variables!
#           - also - the following scripts must be in your nmap scripts directory
#                - ssl-cert
#                - ssl-cert-intaddr
#                - sslv2
#                - ssl-enum-ciphers
#                - ssl-known-key
#                - ssl-dh-params
#                - ssl-ccs-injection
#                - ssl-poodle
#                - ssl-heartbleed
#                - sslv2-drown
#                - tls-ticketbleed
#   [] pip2 install holidays (soc date generator)
#

global default_soc_start
global default_soc_end
global soc_start
global soc_end

# check what this fool is running..
def check_platform():
    if platform == "linux" or platform == "linux2":
        if os.geteuid() != 0:
            print('You must run this script as root!!!')
            exit()
        else:
            os.system('clear')
    elif platform == "darwin":
        if os.geteuid() != 0:
            print('You must run this script as root!!!')
            exit()
        else:
            os.system('clear')
    elif platform == "win32":
        os.system('cls')

# main menu
def main_menu():

    print("""
                     *
           *                        *  
     _____               *     *
    / _  /  ___  _   _  ___ 
    \// /  / _ \| | | |/ __|
     / //\|  __/| |_| |\__ \      *
    /____/ \___| \__,_||___/
                      _/  /
    *                /  _/
                   _/  /         *
                  / __/
                _/ /
               /__/
              //
             /'
                  
    1. Whois Lookup
    2. SSL Audit
    3. Firewalk
    4. Generate Random Dates (SOC Type2)
    5. Parse a File
    6. Quit
    
    """)

    ans = raw_input("zeus>> ")
    if ans == "1":
        print("""
     __    __  _             _      
    / / /\ \ \| |__    ___  (_) ___ 
    \ \/  \/ /| '_ \  / _ \ | |/ __|
     \  /\  / | | | || (_) || |\__ \\
      \/  \/  |_| |_| \___/ |_||___/
    
    
    This module will perform a whois lookup on the domain/ip you enter. 
    
    If you decide to read IPs from a file make sure it's formatted properly:
    127.0.0.1
    192.168.1.1
    ...
    
        """)
        op = raw_input("Do you want to run this module (y/n) >> ")
        if op == "y":
            opp = raw_input("Do you want to read IPs from a file? (y/n) >> ")
            if opp == 'y':
                infile = raw_input("Enter full path and filename with extension >> ")
                with open(infile, 'r') as f:
                    for line in f:
                        victim = line.rstrip("\n")
                        ssl_auditor.do_whois(cwd, victim)
            else:
                victim = raw_input("Enter domain name or IP address: ")
                ssl_auditor.do_whois(cwd, victim)
            main_menu()
        else:
            main_menu()
    elif ans == "2":
        print("""
     __     __       __      _               _  _  _   
    / _\   / _\     / /     /_\   _   _   __| |(_)| |_ 
    \ \    \ \     / /     //_\\\\ | | | | / _` || || __|
    _\ \   _\ \   / /___  /  _  \| |_| || (_| || || |_ 
    \__/   \__/   \____/  \_/ \_/ \__,_| \__,_||_| \__|
    
    
    This module will run the following nmap scripts against the target ip/port specified.
    
        - ssl-cert                  - ssl-dh-params             - tls-ticketbleed
        - ssl-cert-intaddr          - ssl-ccs-injection
        - sslv2                     - ssl-poodle
        - ssl-enum-ciphers          - ssl-heartbleed
        - ssl-known-key             - sslv2-drown
    
    Results are written to ./%s/sslout.txt
    
    If you decide to read IPs from a file make sure it's formatted properly:
    127.0.0.1,443
    127.0.0.1,80
    ...
    
        """) % cwd
        op = raw_input("Do you want to run this module (y/n) >> ")
        if op == 'y':
            opp = raw_input("Do you want to read IP/Port from a file? (y/n) >> ")
            if opp == 'y':
                infile = raw_input("Enter full path and filename with extension >> ")
                with open(infile, 'r') as f:
                    for line in f:
                        (victim_ip, victim_port) = line.split(",")
                        ssl_auditor.do_ssl(cwd, victim_ip, victim_port)
            else:
                victim_ip = raw_input("Enter IP: ")
                victim_port = raw_input("Enter Port: ")
                ssl_auditor.do_ssl(cwd, victim_ip, victim_port)
            main_menu()
        else:
            main_menu()
    elif ans == "3":
        print("""    
      __  _                               _  _    
     / _|(_) _ __   ___ __      __  __ _ | || | __
    | |_ | || '__| / _ \\\\ \ /\ / / / _` || || |/ /
    |  _|| || |   |  __/ \ V  V / | (_| || ||   < 
    |_|  |_||_|    \___|  \_/\_/   \__,_||_||_|\_\\
                                              
    
    This module will attempt to enumerate firewall rules using an IP TTL expiration technique known as firewalking.
    
        """)
        op = raw_input("Do you want to run this module (y/n) >> ")
        if op == 'y':
            victim_ip = raw_input("Enter IP: ")
            ssl_auditor.do_firewalk(victim_ip)
            main_menu()
        else:
            main_menu()

    elif ans == "4":
        print("""
                          _       _                                         _             
     ___  ___   ___    __| | __ _| |_ ___    __ _  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
    / __|/ _ \ / __|  / _` |/ _` | __/ _ \  / _` |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
    \__ \ (_) | (__  | (_| | (_| | ||  __/ | (_| |  __/ | | |  __/ | | (_| | || (_) | |   
    |___/\___/ \___|  \__,_|\__,_|\__\___|  \__, |\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                            |___/                                         
                       
                       
    This module will generate random dates for sampling based on a start - end range
    
        - 20 random days
        - 5 additional random days
        - 5 random weeks
        - 2 random months
        - 2 random quarters
                    
                """)
        op = raw_input("Do you want to run this module (y/n) >> ")
        if op == 'y':

            soc_start = raw_input("Enter starting date (mm-dd-yyyy): ")
            if soc_start == "":
                soc_start = default_soc_start
            soc_end = raw_input("Enter ending date (mm-dd-yyyy): ")
            if soc_end == "":
                soc_end = default_soc_end
            soc_dates.get_vars(soc_start, soc_end)
            main_menu()
        else:
            main_menu()


    elif ans == "5":
        print("""
      __ _ _                                       
     / _(_) | ___   _ __   __ _ _ __ ___  ___ _ __ 
    | |_| | |/ _ \ | '_ \ / _` | '__/ __|/ _ \ '__|
    |  _| | |  __/ | |_) | (_| | |  \__ \  __/ |   
    |_| |_|_|\___| | .__/ \__,_|_|  |___/\___|_|   
                   |_|                             


    This module will parse a file for IP, email address, and URL

    Results will not be written to a file - only to stdout
    
        """)
        op = raw_input("Do you want to run this module (y/n) >> ")
        if op == 'y':
            print("")
            file_to_parse = raw_input("Enter path and filename (C:\Users\source.txt) : ").replace("'","").replace(" ","")
            file_parse.f_parse(file_to_parse)
            main_menu()
        else:
            main_menu()
    elif ans == "6":
        quit()
    else:
        print("Incorrect input!")
        quit()

# main()
# find out what we're working with
check_platform()

# set a working directory real quick - #organization
cwd = raw_input("Enter name for working directory: ")
# if the directory exists - who cares - let's keep working!!
if platform == "linux":
    whatiwant = "mkdir " + cwd + " 2> /dev/null"
    os.system(whatiwant)
else:
    whatiwant = "mkdir " + cwd + " 2> nul"
    os.system(whatiwant)

# main - ish..
print("""
                     *
           *                        *  
     _____               *     *
    / _  /  ___  _   _  ___ 
    \// /  / _ \| | | |/ __|
     / //\|  __/| |_| |\__ \      *
    /____/ \___| \__,_||___/
                      _/  /
    *                /  _/
                   _/  /         *
                  / __/
                _/ /
               /__/
              //
             /'

    1. Whois Lookup
    2. SSL Audit
    3. Firewalk
    4. Generate Random Dates (SOC Type2)
    5. Parse a File
    6. Quit

    """)



ans = raw_input("zeus>> ")
if ans == "1":

    print("""
     __    __  _             _      
    / / /\ \ \| |__    ___  (_) ___ 
    \ \/  \/ /| '_ \  / _ \ | |/ __|
     \  /\  / | | | || (_) || |\__ \\
      \/  \/  |_| |_| \___/ |_||___/


    This module will perform a whois lookup on the domain/ip you enter. 
    
    If you decide to read IPs from a file make sure it's formatted properly:
    127.0.0.1
    192.168.1.1
    ...
    
    """)
    op = raw_input("Do you want to run this module (y/n) >> ")
    if op == "y":
        opp = raw_input("Do you want to read IPs from a file? (y/n) >> ")
        if opp == 'y':
            infile = raw_input("Enter full path and filename with extension >> ")
            with open(infile, 'r') as f:
                for line in f:
                    victim = line.rstrip("\n")
                    ssl_auditor.do_whois(cwd, victim)
        else:
            victim = raw_input("Enter domain name or IP address: ")
            ssl_auditor.do_whois(cwd, victim)
        main_menu()
    else:
        main_menu()
elif ans == "2":
    print("""
     __     __       __      _               _  _  _   
    / _\   / _\     / /     /_\   _   _   __| |(_)| |_ 
    \ \    \ \     / /     //_\\\\ | | | | / _` || || __|
    _\ \   _\ \   / /___  /  _  \| |_| || (_| || || |_ 
    \__/   \__/   \____/  \_/ \_/ \__,_| \__,_||_| \__|


    This module will run the following nmap scripts against the target ip/port specified.
    
        - ssl-cert                  - ssl-dh-params             - tls-ticketbleed
        - ssl-cert-intaddr          - ssl-ccs-injection
        - sslv2                     - ssl-poodle
        - ssl-enum-ciphers          - ssl-heartbleed
        - ssl-known-key             - sslv2-drown
                                    
    Results are written to ./%s/sslout.txt

    If you decide to read IPs from a file make sure it's formatted properly:
    127.0.0.1,443
    127.0.0.1,80
    ...
    
    """) % cwd
    op = raw_input("Do you want to run this module (y/n) >> ")
    if op == 'y':
        opp = raw_input("Do you want to read IP/Port from a file? (y/n) >> ")
        if opp == 'y':
            infile = raw_input("Enter full path and filename with extension >> ")
            with open(infile, 'r') as f:
                for line in f:
                    (victim_ip, victim_port) = line.split(",")
                    ssl_auditor.do_ssl(cwd, victim_ip, victim_port)
        else:
            victim_ip = raw_input("Enter IP: ")
            victim_port = raw_input("Enter Port: ")
            ssl_auditor.do_ssl(cwd, victim_ip, victim_port)
        main_menu()
    else:
        main_menu()
elif ans == "3":
    print("""
      __  _                               _  _    
     / _|(_) _ __   ___ __      __  __ _ | || | __
    | |_ | || '__| / _ \\\\ \ /\ / / / _` || || |/ /
    |  _|| || |   |  __/ \ V  V / | (_| || ||   < 
    |_|  |_||_|    \___|  \_/\_/   \__,_||_||_|\_\\

    
    This module will attempt to enumerate firewall rules using an IP TTL expiration technique known as firewalking.

    """)
    op = raw_input("Do you want to run this module (y/n) >> ")
    if op == 'y':
        victim_ip = raw_input("Enter IP: ")
        ssl_auditor.do_firewalk(victim_ip)
        main_menu()
    else:
        main_menu()

elif ans == "4":
    print("""
    
                          _       _                                         _             
     ___  ___   ___    __| | __ _| |_ ___    __ _  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
    / __|/ _ \ / __|  / _` |/ _` | __/ _ \  / _` |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
    \__ \ (_) | (__  | (_| | (_| | ||  __/ | (_| |  __/ | | |  __/ | | (_| | || (_) | |   
    |___/\___/ \___|  \__,_|\__,_|\__\___|  \__, |\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                            |___/                                         
                

    This module will generate random dates for sampling based on a start - end range
    
        - 20 random days
        - 5 additional random days
        - 5 random weeks
        - 2 random months
        - 2 random quarters
                  
        """)
    op = raw_input("Do you want to run this module (y/n) >> ")
    if op == 'y':

        soc_start = raw_input("Enter starting date (mm-dd-yyyy): ")
        default_soc_start = soc_start
        soc_end = raw_input("Enter ending date (mm-dd-yyyy): ")
        default_soc_end = soc_end
        soc_dates.get_vars(soc_start, soc_end)
        main_menu()
    else:
        main_menu()

elif ans == "5":
    print("""
    
      __ _ _                                       
     / _(_) | ___   _ __   __ _ _ __ ___  ___ _ __ 
    | |_| | |/ _ \ | '_ \ / _` | '__/ __|/ _ \ '__|
    |  _| | |  __/ | |_) | (_| | |  \__ \  __/ |   
    |_| |_|_|\___| | .__/ \__,_|_|  |___/\___|_|   
                   |_|                             
    
    This module will parse a file for IP, email address, and URL
    
    Results will not be written to a file - only to stdout
    
    """)
    op = raw_input("Do you want to run this module (y/n) >> ")
    if op == 'y':
        print("")
        file_to_parse = raw_input("Enter path and filename (C:\Users\source.txt) : ").replace("'","").replace(" ","")
        file_parse.f_parse(file_to_parse)
        main_menu()
    else:
        main_menu()
elif ans == "6":
    quit()
else:
    print("Incorrect input!")
    quit()