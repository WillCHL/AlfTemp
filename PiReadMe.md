# Pi Cheat Sheet

## Command Line

*	To load graphical interface:

		$ startx
*	To run python script: 

		$ /usr/bin/python <python script>

*	Log Temperature Code:

		$ /usr/bin/python ~/Documents/TempLog/LogTempCSV.py
*	Test Temperature Code:
	
		$ /usr/bin/python ~/Documents/TempLog/TempDataTest.py

*	End python script:
		
	*	Control + C (keyboard interrupting)
	*	With code

			$ ps -elf | grep python
			$ kill -9 <whatever_the_PID_is>
			$ or: kill -TERM <pid>
			$ keyboard interrupting ,i.e. Control+C

*	Run/edit start up script [This is not currently used]
	*	Now we need to tell the operating system to run the script for the Pi user. In the command prompt or in a terminal window type :

			$ sudo nano /etc/profile
	*	Scroll to the bottom and add the following line :

			$ sudo python /home/pi/myscript.py
	*	where “/home/pi/myscript.py” is the path to your script.

			$ /usr/bin/python ~/Documents/TempLog/TempDataTest.py

*	Cron Job [This method is used]
	*	Open file (sudo means opening the job list for Admin, enter for Pi):

			$ sudo crontab -e
		
	*	Edit file for python script:

			$ */5 * * * * python ~/Documents/TempLog/GetDataCSV.py
		
	*	Edit file for dropbox upload ever 10 min:

			*/10 * * * *  ~/Dropbox-Uploader/dropbox_uploader.sh upload ~/Documents/TempLog/data /

*	GIT
	*	Used to track changes in code

*	GIThub - online version (and backup) for changes in code.
	*	https://github.com/WillCHL/AlfTemp.git
	*	https://github.com/WillCHL/AlfTemp2.git


## Dropbox
*	Dropbox Uploader GitHub
	*	https://github.com/andreafabrizi/Dropbox-Uploader 
*	Upload commands

		$ ~/Dropbox-Uploader/dropbox_uploader.sh upload ~/Documents/TempLog/data /
*	Easiest way to download the code:

		$ git clone https://github.com/andreafabrizi/Dropbox-Uploader/
*	Backup programming files (Need to find code to NOT include subfolders):
	
		$ ~/Dropbox-Uploader/dropbox_uploader.sh upload ~/Documents/TempLog/ /


## Change config file for gpio pins

## Python


