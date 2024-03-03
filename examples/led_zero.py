#import the GPIO and time package
from gpiozero import LED,PWMLED,Button
from signal import pause
import time
led_pin ="8" 
button_pin ="10" 
# red = LED("BOARD"+"8")
led = PWMLED("BOARD"+led_pin)
def pulseLED():
    led.pulse()
    printInfo()
def printInfo():
    print("hi")
button = Button("BOARD"+button_pin,hold_repeat=True)
button.when_pressed = pulseLED
# red.blink()
pause()
