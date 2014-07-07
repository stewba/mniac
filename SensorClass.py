__author__ = 'stew'
import time
import os,sys
import redis
import socket,struct

class Sensor:
    """A generic sensor class"""

    def __init__(self, name="GenericSensor", host="127.0.0.1", port=50000):
        self.db = redis.StrictRedis(host='localhost', port=6379, db=0)
        self.name = name
        self.host = host
        self.port = port
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

    def initSensorDB(self):
        self.db.setnx(self.name+":config:port", self.port)
        self.db.setnx(self.name+":config:host", self.host)

sen = Sensor()
sen.startAcquisition()

