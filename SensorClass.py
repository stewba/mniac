__author__ = 'stew'
import time
import os,sys,signal
import redis
import socket,struct
import SerialSensor

class Sensor:
    """A generic sensor class"""

    def __init__(self, sensorName="GenericSensor", hostname="127.0.0.1", portnum=6379, dbnum=0):
        self.db = redis.StrictRedis(host=hostname, port=portnum, db=dbnum)
        self.name = sensorName
        self.host = "127.0.0.1"
        self.port = 50000
        self.lastMessageTime = time.time()
        self.lastMessage = ""

        self.initSensorDB()

    def analyseMessage(self, message=""):
        outputVars = dict()
        return outputVars

    def read(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((self.db.get(self.name+":config:host"), int(self.db.get(self.name+":config:port"))))
        while(1):
            self.lastMessage = s.recvfrom(1024)
            self.lastMessageTime = time.time()
            self.db.set(self.name+":data:time", self.lastMessageTime)
            self.db.set(self.name+":data:value", self.lastMessage)
            time.sleep(1)

    def write(self):
        redis = 0

    def startAcquisition(self):
        newpid = os.fork()
        if newpid == 0:
            self.read()
        else:
            print "Started listening, process id:", newpid
            print "Press y and enter if you want to stop"
            s = sys.stdin.readline();
            while s != 'y\n' :
                s = sys.stdin.readline()
            os.kill(int(newpid), signal.SIGTERM)

    def initSensorDB(self):
        self.db.setnx(self.name+":config:port", self.port)
        self.db.setnx(self.name+":config:host", self.host)

# you can test the sensor udp with : echo -n "test data" | nc -4u -w1 <host> <udp port>
