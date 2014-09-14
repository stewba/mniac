#!/usr/bin/python


from SerialSensor import SerialSensor


sen = SerialSensor("SerialSensorTest","nectar.wilde.id.au",6379,0)
sen.startAcquisition()

