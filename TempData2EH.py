# GrovePi + Grove Temperature Sensor
import time
import grovepi
from azure.servicebus import ServiceBusService

key_name ='RootManageSharedAccessKey' # SharedAccessKeyName from Azure Portal
key_value='s2mHOGi2IoHNhHG9m2v9TDSa+atCtJtgVZb0oQi0RpI=' # SharedAccessKey from Azure Portal
sbs = ServiceBusService('asatestsn', shared_access_key_name=key_name, shared_access_key_value=key_value)
sbs.create_event_hub('hubcreationfromlinux')

# Connect the Grove Temperature Sensor to analog port D4
sensor_port = 4
deviceId = "device-1"
#Declare direction to the pin.
#grovepi.pinMode (Temp_sensor,"INPUT")
while True:
    try:
        [temp,hum] = grovepi.dht(sensor_port,0)
        CurrentTime = str(time.localtime(time.time()).tm_hour) + ":" + str(time.localtime(time.time()).tm_min) + ":"+ str(time.localtime(time.time()).tm_sec)
        print "Temperature : ", temp , "Humidity : ", hum, "RecordTime : ", CurrentTime  
        sbs.send_event('hubcreationfromlinux', '{ "DeviceId":"' + deviceId + '", "Temperature":"' + str(temp) +'", "Humidity":"' + str(hum) +'", "RecordTime":"' + str(CurrentTime) +'"}')
        # sbs.send_event('hubcreationfromlinux', '{ "DeviceId":"' + deviceId + '", "Temperature":"' + temperature +'"}')
        time.sleep(1.0)
    except IOError:
        print "Error"
