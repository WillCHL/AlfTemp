# This code is to enable DS18B20 one wire temperature logging using a raspeberry pi

# GetTempCSV.py
-This file reads the temperature of all listed sensors and returns the date at time to the command line and to a file.  A new file is created every day.
-The file will read the temperature of each sensor 3 times and return the average of these measurements.
-If a sensor can't be read then 3 attempts will be made to read it before reaturnign a 'nan' value.
-This file can be run at regular intervals using crontab: 'crontab -e'

# LogTempCSV.py
-The file was originally set-up to complete all of the logging however at initially crontab reboot call wasn't working so the GetTemp file was created.
-This file could be reimplemented if needed.
-Major changes that should be made are: 
	-add number attempts if sensor can't be found
	-check for full file path references
	-improve the file name/date checking procedure
	-possible implement the create file function in GetTempCSV.py

# TempDataTest.py
-This file was created to check the outputs and data integrity quickly.
-It includes the attempts function to check for sensor.
-It write to the command line and to a csv file.


# Planned improvements
-Read in a list of sensor rather than have them hard coded
-Write a function that searches for the last ? days of logging before starting a new file
-More documentation.
