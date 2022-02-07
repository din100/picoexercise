import machine

#Setup 2 didgital imputs for buttons
But  tonA = machine.Pin(0,machine.Pin.IN,
                        machine.Pin.PULL_DOWN)
ButtonB = machine.Pin(1,machine.Pin.IN,
                        machine.Pin.PULL_DOWN)
#Setup a PWM out put
Buzzer = machine.PWM(machine.Pin(15))
Buzzer.duty_u16(32767) # make it 50% duty cycle
Frequency= 1000

def ButtonIRQHandler(pin):
    global Frequency
    if pin == ButtonA: #up the frequency
        if Frequency < 2000:
            Frequency += 50
        elif pin == ButtonB: #lower the freqncy
            if Frequency > 100:
                frequency -=50

#setup the IRQ and the hock it to the nadlers
ButtonA.irq(trigger = machine.Pin.IRQ_RISING,
            handler = ButtonIRQHandler)
ButtonB.irq(trigger = machine.Pin.IRQ_RISING,
            handler = ButtonIRQHandler)

while True:
    Buzzer.freq(Frequency) to 500