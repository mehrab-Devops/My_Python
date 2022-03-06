import getpass
import telnetlib

user = input("Enter your remote account : ")
password = getpass.getpass()

for y in range(186,190):
    HOST = "172.32.1." + str(y)
    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"enable\n")
    tn.write(b"cisco\n")
    tn.write(b"conf t\n")
    tn.write(b"hostname sw" + str(y).encode('ascii') + b"\n")

    for x in range(2,6):
        tn.write(b"vlan " + str(x).encode('ascii') + b"\n")
        tn.write(b"name vlan_" + str(x).encode('ascii') + str(x).encode('ascii') + b"\n")
        tn.write(b"exit\n")
   
    tn.write(b"end\n")
    tn.write(b"wr\n")
    tn.write(b"exit\n")

    print(tn.read_all().decode('ascii'))
