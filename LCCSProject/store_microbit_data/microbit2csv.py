## Uncomment Lines 2 to 6 to find which serial port your microbit is connected to
#import serial.tools.list_ports
# ports = serial.tools.list_ports.comports()
# for port, desc, hwid in sorted(ports):
#         print("{}: {} [{}]".format(port, desc, hwid))

##
import csv
import serial, time
from datetime import datetime

#Enter a Stop Time
stopTime = "2023-12-05 14:48:00"
#convert the string to a datetime class
convertTime = datetime.strptime(stopTime, "%Y-%m-%d %H:%M:%S")
#change this to correct port e.g on windows COM4
port = "/dev/cu.usbmodem14602"
#leave this value
baud = 115200
s = serial.Serial(port)
s.baudrate = baud

# creates this file in same dir as .py file
file = open("temperature2.csv","a",newline="")
db = csv.writer(file)

#While now time is less than the target stoptime
while datetime.now() < convertTime:
   data = s.readline()
   data = int(data[0:4])
   db.writerow([data])
   print(data)
   time.sleep(10)
   
file.close()
