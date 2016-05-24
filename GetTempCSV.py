#!/usr/bin/python
import time
import os.path
from datetime import datetime #, deltatime
import numpy as np

#Max attempts variable
maxattempts=3

#Set days per file
ndays=7

#Base File Name
basefname="Temp1.csv"

# ID's: waterproof probe, chip
sensorids = ["28-01159070bcff", "28-0215637a92ff"]
fullpath = "/home/pi/Documents/TempLog/data/"
# filenames = os.listdir(fullpath) Used if doing multi dy files
# filenames = [i for i in filenames if i.endswith(basefname)]

#function to create new file
def newFile(filenm):
	headers=["Date","Time"]
	headers.extend(sensorids)
	print headers
	f=open(fullpath+filenm,'a')
	f.write(','.join(headers)+'\n')
	f.close()

now=datetime.now()

writefile=now.strftime('%Y-%m-%d') + basefname

# Write headers for new data file if file with todays date does not exist
if not os.path.exists(fullpath + writefile):
        newFile(writefile)

# Loop to collect data
avgtemperatures = []
for sensor in range(len(sensorids)):
	temperatures = []
	for polltime in range(0,3):
			text = '';
			attempts=0
			temperature=[]
			while text.split("\n")[0].find("YES") == -1:
					if attempts==maxattempts:
						temperature=np.nan
						break
					try:
						tfile = open("/sys/bus/w1/devices/"+ sensorids[sensor] +"/w1_slave")
						text = tfile.read()
						tfile.close()
					except IOError:
						print 'Sensor not found: ', sensorids[sensor]
					time.sleep(1)
					attempts += 1
 
			if not np.isnan(temperature):
				secondline = text.split("\n")[1]
				temperaturedata = secondline.split(" ")[9]
				temperature = float(temperaturedata[2:])
			temperatures.append(temperature / 1000)
	
	avgtemperatures.append("%.2f" % round(sum(temperatures) / float(len(temperatures)),2))

# Generate list of time and temperature values and write to file

timevalue=time.asctime(time.localtime(time.time()))
output_vec = [now.strftime('%Y-%m-%d'),now.strftime('%H:%M:%S')]
output_vec.extend(avgtemperatures)
print output_vec

f=open(fullpath + writefile,'a')
c=1
for item in output_vec:
	if c==1:
		char=""
		c=0
	else:
		char=","
	f.write(char+str(item))
f.write("\n")
f.close()



