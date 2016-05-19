#!/usr/bin/python
import time
import os.path
from datetime import datetime #, deltatime

#Set sleep time in seconds
sleeptime=50

#Set days per file
ndays=7

# ID's: waterproof probe, chip
sensorids = ["28-01159070bcff", "28-0215637a92ff"]

#function to create new file
def newFile(filenm):
	headers=["Date","Time"]
	headers.extend(sensorids)
	print headers
	f=open("./data/"+filenm,'a')
	f.write(', '.join(headers)+'\n')
	f.close()

now=datetime.now()
starttime=now

writefile=now.strftime('%Y-%m-%d')+"Temp1.csv"

# Write headers for new data file if file with todays date does not exist
if not os.path.exists("./data/" + writefile):
        newFile(writefile)

# Loop to collect data
#while True:
#for i in range(10):
	now=datetime.now()
	delta=now-starttime
	if delta.days>ndays:
		writefile=now.strftime('%Y-%m-%d')+"Temp1.csv"
		newFile(writefile)
		starttime=now

	avgtemperatures = []
	for sensor in range(len(sensorids)):
		temperatures = []
		for polltime in range(0,3):
				text = '';
				while text.split("\n")[0].find("YES") == -1:
						tfile = open("/sys/bus/w1/devices/"+ sensorids[sensor] +"/w1_slave")
						text = tfile.read()
						tfile.close()
						time.sleep(1)
	 
				secondline = text.split("\n")[1]
				temperaturedata = secondline.split(" ")[9]
				temperature = float(temperaturedata[2:])
				temperatures.append(temperature / 1000)
 	
		avgtemperatures.append("%.2f" % round(sum(temperatures) / float(len(temperatures)),2))

	# Generate list of time and temperature values and write to file

	#print "Avg Temp: ",avgtemperatures
	timevalue=time.asctime(time.localtime(time.time()))
	# print timevalue
	# output_vec = [timevalue]
	output_vec = [now.strftime('%Y-%m-%d'),now.strftime('%H:%M:%S')]
	output_vec.extend(avgtemperatures)
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
	f.close()

#	time.sleep(sleeptime)

