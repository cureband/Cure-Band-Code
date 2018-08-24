import os
import time
import serial

ser = serial.Serial('/dev/ttyACM0',9600)
s = [0]
while True:
	read_serial=ser.readline()
	s[0] = str(int (ser.readline(),16))
	print s[0]
	i[0] = int(s[0])

	if i[0]< 250:
		os.system("sudo rm /home/pi/Desktop/rate.txt")
		os.system("sudo echo -n "" > rate.txt")
		with open("/home/pi/Desktop/rate.txt", "a") as f:
			f.write("{}".format(s[0]))


	else:
		read_serial=ser.readline()
		s[1] = str(int (ser.readline(),16))
		print (s[1])
		i[1] = int(s[1])

		time.sleep(5)

		read_serial=ser.readline()
		s[2] = str(int (ser.readline(),16))
		print (s[2])
		i[2] = int(s[2])

		time.sleep(5)

		read_serial=ser.readline()
		s[3] = str(int (ser.readline(),16))
		print (s[3])
		i[3] = int(s[3])

		time.sleep(5)

		read_serial=ser.readline()
		s[4] = str(int (ser.readline(),16))
		print (s[4])
		i[4] = int(s[4])

		time.sleep(5)

		read_serial=ser.readline()
		s[5] = str(int (ser.readline(),16))
		print (s[5])
		i[5] = int(s[5])

		if i[1]+i[2]+i[3]+i[4]+i[5] > 1800:
			print("Ventricular Fibrillation is suspected to be occuring at the Moment. Alerting Amublances NOW")
			os.system("sudo python")#Insert python for text now










