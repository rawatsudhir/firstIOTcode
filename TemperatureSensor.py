# GrovePi + Grove Temperature Sensor
import time
import grovepi
# Connect the Grove Temperature Sensor to analog port A0
Temp_sensor = 0
#Declare direction to the pin.
grovepi.pinMode (Temp_sensor,"INPUT")
while True:
    try:
        sensor_value = grovepi.analogRead(Temp_sensor)
        print "sensor_value =", sensor_value
        time.sleep(.5)
    except IOError:
        print "Error"
