import os
import sys

from pip._vendor.distlib.compat import raw_input


def inputNumber(message):
    while True:
        try:
            choice = int(input(message))
        except ValueError:
            print("Not an integer! Please reenter")
            continue
        else:
            return choice
            break


def menuselect():
    menu = ["1.Find information about IP/domain", "2.Display host IP information", "3.NS Lookup", "4.Traceroute", "5.Ping an IP",
            "6.Nmap network scan", "7.DNS lookup","8.Exit"]

    for i in menu:
        print(i)

    while True:
        select = inputNumber("Choose from menu: ")
        if select < 1 or select > 8:
            print("Out of range!")
        else:
            break
    return select


while True:
    selected = menuselect()
    if selected == 1:
        print("List information of IP/domain")
        host = raw_input("Enter domain name/IP address : ")
        os.system("host -a " + host)
    elif selected == 2:
        print("Displaying host information...")
        os.system("ifconfig")
    elif selected == 3:
        print("Performing name server lookup...")
        host = raw_input("Enter domain name/IP address : ")
        os.system("nslookup -query=any " + host)
    elif selected == 4:
        print("Tracerouting...")
        host = raw_input("Enter domain name/IP address : ")
        os.system("traceroute " + host)
    elif selected == 5:
        print("Pinging an address...")
        host = raw_input("Enter domain name/IP address: ")
        response = os.system("ping -c 1 " + host)
        if response == 0:
            print("Ping Success!")
        else:
            print("Ping failed!")
    elif selected == 6:
        print("Performing NMAP network scan...")
        host = raw_input("Enter IP address with CIDR: ")
        os.system("sudo nmap -sn " + host)
    elif selected == 7:
        print("DNS lookup...")
        host = raw_input("Enter domain name/IP address : ")
        os.system("host -a " + host)
    elif selected == 8:
        sys.exit("Exiting program...")
