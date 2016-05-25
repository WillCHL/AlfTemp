#!/usr/bin/python
import time
import os.path
from datetime import datetime #, deltatime
import numpy as np

#Set sleep time in seconds
sleeptime=1

#Max attempts variable
maxattempts=5

fullpath = "/home/pi/Documents/TempLog/"

# ID's: waterproof probe 1, chip, waterproof probe 2
#sensorids = ["28-01159070bcff","28-0215637a92ff", "28-000007c6d33f"]
a,b=np.loadtxt(fullpath + 'sensors1.csv',dtype=([('ID', str,15),('Active',bool)]),delimiter=',',skiprows=1,usecols=(0,2),unpack=True)
sensorids=a
active=b
sensorids=list(sensorids[active])

#function to create new file
def newFile(filenm):
	headers=["Date","Time","SensorID","Attempts", "Temperature"]
	print headers
	f=open("./data/"+filenm,'a')
	f.write(','.join(headers)+'\n')
	f.close()

now=datetime.now()
starttime=now

writefile=now.strftime('%Y-%m-%d')+"Test.csv"

# Write headers for new data file do this every ?? days
if not os.path.exists("./data/" + writefile):
        newFile(writefile)

# Loop to collect data
#while True:
for i in range(10):
	now=datetime.now()
	avgtemperatures = []
	for sensor in range(len(sensorids)):
		temperatures = []
		for polltime in range(0,3):
				temperature=""
				text = '';
				attempts=0
				while text.split("\n")[0].find("YES") == -1:
						if attempts==maxattempts:
							temperature='NA'
							break
						try:
							tfile = open("/sys/bus/w1/devices/"+ sensorids[sensor] +"/w1_slave")
							text = tfile.read()
							tfile.close()
						except IOError:
							print 'Sensor not found: ', sensorids[sensor]
						time.sleep(1)
						attempts += 1
	 			if temperature != 'NA':
					secondline = text.split("\n")[1]
					temperaturedata = secondline.split(" ")[9]
					temperature = float(temperaturedata[2:])
					temperature= temperature / 1000
				#print repr(( sensor,", ",temperature))
	# Generate list of time and temperature values and write to file

	#print "Avg Temp: ",avgtemperatures
	# timevalue=time.asctime(time.localtime(time.time()))
	# print timevalue
	# output_vec = [timevalue]
				output_vec = [now.strftime('%Y-%m-%d'),now.strftime('%H:%M:%S'), sensorids[sensor],attempts, temperature]
				#output_vec.extend(temperature)
				print output_vec

				f=open("./data/" + writefile,'a')
				c=1
				for item in output_vec:
					if c==1:
						char=""
						c=0
					else:
						char=", "
					f.write(char+str(item))
				f.write("\n")
				#f.write(str(temperature)+"\n")
				f.close()

	time.sleep(sleeptime)

