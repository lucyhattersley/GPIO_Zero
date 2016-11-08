from gpiozero import LED, Button 
from signal import pause

led = LED(17) 
button = Button(21)

button.when_pressed = led.on
button.when_released = led.off

pause()