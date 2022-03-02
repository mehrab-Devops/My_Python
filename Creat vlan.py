import getpass
import telnetlib

HOST = input("Enter your IP Address : ")
user = input("Enter your remote user : ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")
tn.write(b"hostname mysw\n")

for x in range(2,6):
    vlan = input("Enter your vlan name : ")
    tn.write(b"vlan " + str(x).encode('ascii') + b"\n")
    tn.write(b"name " + str(vlan).encode('ascii') + str(x).encode('ascii') + b"\n")
    tn.write(b"exit\n")
   
tn.write(b"end\n")
tn.write(b"wr\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
