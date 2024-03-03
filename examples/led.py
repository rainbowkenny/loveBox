#import the GPIO and time package
import RPi.GPIO as GPIO
import time
led_pin = 8
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT)
# loop through 50 times, on/off for 1 second
for i in range(50):
    print("ON")
    GPIO.output(led_pin,GPIO.HIGH)
    time.sleep(1)
    print("OFF")
    GPIO.output(led_pin,GPIO.LOW)
    time.sleep(1)
GPIO.cleanup()
