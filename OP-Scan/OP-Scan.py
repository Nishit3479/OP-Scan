import pyfiglet
from datetime import datetime
import socket

op_scan = pyfiglet.figlet_format("OP - SCAN")
print(op_scan)
print("-" * 60)
try:
	target = input("Enter URL/IP : ")
	q1 = input("Would you like to scan '"+target+"' (y/n) -- ")
	if q1[0] == "N" or q1[0] == "n":
		print("\nSession Terminated !!!")
		exit()
	else:
		Sport = 1
		Eport = 65535
	q2 = input("Would you like to scan all (1-65535) ports (y/n) -- ")
	if q2[0] == "Y" or q2[0] == "y":
		Stime=datetime.now()
		print("Scan Started at : "+str(Stime))
	else:
		Sport = int(input("Enter Starting Port : "))
		Eport = int(input("Enter Ending Port : "))
		Stime=datetime.now()
		print("Scan Started at : "+str(Stime))
	print("-" * 60)
	try:
		ip = socket.gethostbyname(target)
	except socket.gaierror:
	        print("\nHostname Could Not Be Resolved !!!!")
	        exit()
	c = 0
	print("PORT\tSTATUS\tSERVICE")
	for port in range(Sport,Eport+1):
		i = 0
		try:
			sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sck.settimeout(0.1)
		except socket.error:
	       		print("\nServer not responding !!!!")
	        	exit()
		try:	
			sck.connect((ip, port))
			sck.settimeout(None)
			i = 1
		except Exception as e:
			i = 0;
		if i == 1:
			ser = socket.getservbyport(port)
			print(str(port)+"\tOpen\t"+ser)
			c = c+1
	if c == 0:
		print("\nNo Open Ports Found")
	Etime = datetime.now()
	duration = Etime - Stime
	duration_in_s = duration.total_seconds()
	hours   = divmod(duration_in_s, 3600)
	minutes = divmod(hours[1], 60)     
	seconds = divmod(minutes[1], 1)
	print("\nScan Successfully Ended at : "+str(Etime))
	print("Scan Duration : "+str(int(hours[0]))+"h - "+str(int(minutes[0]))+"m - "+str(int(seconds[0]))+"s")
	print("The Target IP : "+str(ip)+" has "+str(c)+" open ports") 
except KeyboardInterrupt:
        print("\nSession Terminated !!!")
        exit()


