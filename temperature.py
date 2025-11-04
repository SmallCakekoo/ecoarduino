import time
from w1thermsensor import W1ThermSensor
sensor = W1ThermSensor()

while True:
    temperature = sensor.get_temperature()
    print("the temperature is %s celcius" % temperature)
    time.sleep(1)