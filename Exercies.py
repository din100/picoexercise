import machine
#Setup the onboard LED as a output
LED = machine.Pin(25,machine.Pin.OUT)
Button = machine.Pin(0,machine.Pin.IN,machine.Pin.PULL_DOWN)
while True:
    LED.value(Button.value())