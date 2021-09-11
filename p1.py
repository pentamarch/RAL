import webbrowser
import subprocess
import platform
import os
import socket

def get_Host_name_IP():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        print("\nHostname :  ",host_name)
        print("\nIP : ",host_ip)
    except:
        print("Unable to get Hostname and IP")

while True:
    print("\nWhich operations")
    print("1. open web browser")
    print("2. open notepad")
    print("3. Display os information")
    choice = input("Enter choice: ")

    if choice == '1':
        url = input("Enter url : ")
        webbrowser.open(url,new=2)
    elif choice == '2':
      
        filename = input("Enter file name : ")
        proc = subprocess.Popen(['gedit',filename])

    elif choice == '3':
        print("Name of the operating system",os.name)
        print("\nName of the platform",platform.system())
        print("\nRelease of operating system",platform.release())
        print("\nVersion of operating system",platform.version())
        get_Host_name_IP()
    else:
        break