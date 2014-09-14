#!/usr/bin/python
from serial import Serial
from SensorClass import Sensor

class SerialSensor(Sensor):
    def __init__(self,sensorName,hostname,port,dbnum):
        Sensor.__init__(self,sensorName,hostname,port,dbnum)

    def read(self):
        try:  
            ser = Serial('/dev/ttyUSB0', 9600)  
        except:  
            print "Failed to connect on /dev/ttyUSB0" 

        if ser.isOpen():
            while True:
                response = ser.readline()
                print(response)
