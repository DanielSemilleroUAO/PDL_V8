import ASUS.GPIO as GPIO

class SensorPIR(object):
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.ASUS)     
        self.PirSensor   = 257
        GPIO.setup(self.PirSensor,GPIO.IN)
    def LeerSensor(self):
        try:
            if(GPIO.input(self.PirSensor)):
                return True
            else:
                return False
        except:
            return False