#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from libnmap.process import NmapProcess
import subprocess



def user_prompt():
    myprompt = raw_input("[>] zeus >> ")
    return myprompt

def user_prefs():
    """ Get user preferences """
    target = raw_input("Enter lhost: ")

def dependents():
    """ Package dependencies """

def ssl_audit(target_ip,target_port):
    #print ("""

     #           ******************
     #           Obtaining SSL Cert
     #           ******************

     #           """)


    #            ***********************************
    #            Checking for internal ip disclosure
    #            ***********************************

    #                        """)



    ssl_scripts = ["ssl-cert", "ssl-cert-intaddr","sslv2","ssl-enum-ciphers","ssl-known-key","ssl-dh-params","ssl-ccs-injection","ssl-poodle","ssl-heartbleed","sslv2-drown","tls-ticketbleed"]
    for script in ssl_scripts:
        myoptions = "nmap --script " + script + " -p " + target_port + " " + target_ip + " >> ssl_out.txt"
        #os.system(myoptions)
        output = subprocess.check_output(myoptions, shell=True)
        print output

        print ("""
    
                    ******************************
                    Checking if SSLv2 is supported
                    ******************************
    
                                """)

        print ("""
    
                    ***********************
                    Enumerating SSL ciphers 
                    ***********************
    
                                """)

        print ("""
    
                    *****************************
                    Checking for problematic keys
                    *****************************
    
                                """)

        print ("""
    
                    ********************************
                    Checking for weak Diffie-Hellman
                    ********************************
    
                                """)

        print ("""
    
                    *******************************
                    Checking for CCS Injection Vuln
                    *******************************
    
                                """)

        print ("""
    
                    ************************
                    Checking for POODLE vuln
                    ************************
    
                                """)

        print ("""
    
                    ****************************
                    Checking for Heartbleed vuln
                    ****************************
    
                                """)

        print ("""
    
                    *****************************
                    Checking for Drown SSLv2 vuln
                    *****************************
    
                                """)

        print ("""
    
                    ************************************
                    Checking for F5 Ticketbleed bug vuln
                    ************************************
    
                                """)




def main_menu():
    print("""
    Menu:

        1.  SSL Audit
        2.  Quit

        """)

def ssl_banner():
    print("""


    [>] SSL Audit


                    """)

def main():
    """ Main program """
    # Code goes over here.
    main_menu()
    choice = user_prompt()
    if int(choice) == 1:
        try:
            ssl_banner()
            target_ip = raw_input("[>] zeus >> [RHOST]: ")
            target_port = raw_input("[>] zeus >> [RPORT]: ")
            ssl_audit(target_ip,target_port)
            print("[i] SSL output saved to ssl_out.txt")
        except:
            pass
    else:
        exit(1)
    main_menu()
    return 0

if __name__ == "__main__":
    main()