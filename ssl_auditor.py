import os
import re

def do_whois(dir, args):
    """Whois lookup based on domain name or ip"""
    print ("""

    ******************************************************
    Obtaining Whois information for %s
    ******************************************************

    """) % args
    is_ip = re.match("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", args)
    if is_ip:
        os.system('nmap --script whois-ip ' + args + ' >> ' + './' + dir + '/' + args + '_whois.txt')
        print("Whois info written to " + args + "_whois.txt")
    else:
        os.system('nmap --script whois-domain ' + args + ' >> ' + './' + dir + '/' + args + '_whois.txt')
        print("Whois info written to " + args + "_whois.txt")

def do_ssl(dir, ip, port):
    """Runs a number of nmap scripts for SSL info"""

    print ("""
    
    ******************
    Obtaining SSL Cert
    ******************
    
    """)
    print('nmap --script ssl-cert ' + ip + ' -p ' + port.rstrip("\n") + ' >> ' + './' + dir + '/' + ip + '-' + port.rstrip("\n") + '-' + 'sslout.txt')
    print ("""

    ***********************************
    Checking for internal ip disclosure
    ***********************************

                """)
    os.system('nmap --script ssl-cert-intaddr ' + ip + ' -p ' + port.rstrip("\n") + ' >> ' + './' + dir + '/' + ip + '-' + port.rstrip("\n") + '-' + 'sslout.txt')
    print ("""

    ******************************
    Checking if SSLv2 is supported
    ******************************

                """)
    os.system('nmap --script=sslv2 ' + ip + ' -p ' + port.rstrip("\n") + ' >> ' + './' + dir + '/' + ip + '-' + port.rstrip("\n") + '-' + 'sslout.txt')
    print ("""

    ***********************
    Enumerating SSL ciphers 
    ***********************
    
                """)
    os.system('nmap --script=ssl-enum-ciphers ' + ip + ' -p ' + port.rstrip("\n") + ' >> ' + './' + dir + '/' + ip + '-' + port.rstrip("\n") + '-' + 'sslout.txt')
    print ("""

    *****************************
    Checking for problematic keys
    *****************************
    
                """)
    os.system('nmap --script=ssl-known-key ' + ip + ' -p ' + port.rstrip("\n") + ' >> ' + './' + dir + '/' + ip + '-' + port.rstrip("\n") + '-' + 'sslout.txt')
    print ("""

    ********************************
    Checking for weak Diffie-Hellman
    ********************************

                """)
    os.system('nmap --script=ssl-dh-params ' + ip + ' -p ' + port.rstrip("\n") + ' >> ' + './' + dir + '/' + ip + '-' + port.rstrip("\n") + '-' + 'sslout.txt')
    print ("""

    *******************************
    Checking for CCS Injection Vuln
    *******************************
    
                """)
    os.system('nmap --script=ssl-ccs-injection ' + ip + ' -p ' + port.rstrip("\n") + ' >> ' + './' + dir + '/' + ip + '-' + port.rstrip("\n") + '-' + 'sslout.txt')
    print ("""

    ************************
    Checking for POODLE vuln
    ************************
    
                """)
    os.system('nmap --script=ssl-poodle ' + ip + ' -p ' + port.rstrip("\n") + ' >> ' + './' + dir + '/' + ip + '-' + port.rstrip("\n") + '-' + 'sslout.txt')
    print ("""

    ****************************
    Checking for Heartbleed vuln
    ****************************

                """)
    os.system('nmap --script=ssl-heartbleed ' + ip + ' -p ' + port.rstrip("\n") + ' >> ' + './' + dir + '/' + ip + '-' + port.rstrip("\n") + '-' + 'sslout.txt')
    print ("""

    *****************************
    Checking for Drown SSLv2 vuln
    *****************************

                """)
    os.system('nmap --script=sslv2-drown ' + ip + ' -p ' + port.rstrip("\n") + ' >> ' + './' + dir + '/' + ip + '-' + port.rstrip("\n") + '-' + 'sslout.txt')
    print ("""

    ************************************
    Checking for F5 Ticketbleed bug vuln
    ************************************

                """)
    os.system('nmap --script=tls-ticketbleed ' + ip + ' -p ' + port.rstrip("\n") + ' >> ' + './' + dir + '/' + ip + '-' + port.rstrip("\n") + '-' + 'sslout.txt')

    print("SSL results written to " + ip + "-" + port.rstrip("\n") + "-sslout.txt")

def do_firewalk(ip):
    """Use nmap firewalk script against target ip"""
    print ("""

                *************************
                Executing firewalk script
                *************************

                            """)
    os.system('nmap --script firewalk --traceroute ' + ip + ' >> ' + ip + '_firewalker.txt')


# NOT YET IMPLEMENTED
#def do_shodan(args):
#    """Run ip address against shodan database"""
#    if len(args) == 0:
#        print "You must enter an ip address (Example: firewalk 127.0.0.1)"
#    else:
#        print ("""
#
#        *************************
#        Running ip against shodan
#        *************************
#
#                    """)
#        os.system("nmap --script shodan-api --script-args 'shodan-api.target=" + args + ",shodan-api.apikey=" + SHODANAPIKEY + "'")


