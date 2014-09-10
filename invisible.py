
# invisible driver...

import RPi.GPIO as io
import time

def quick_setup(pins,i):
    for pin in pins:
        io.setup(pin,i)

def quick_set(pins,v):
    debug = ""
    for i in range(0,len(pins)):
        debug+=str((v>>i)&1)
        #if pins[i]==3:
        #    print(str(pins[i])+":"+str((v>>i)&1))
        #time.sleep(0.1)
        io.output(pins[i],(v>>i)&1)
    #print(debug)

def quick_read(pins):
    for i in range(0,len(pins)):
        t = io.input(pins[i])
        print("pin "+str(i)+" is "+str(t))
        
def value_read(pins):
    v = 0
    for i in range(0,len(pins)):
        # low is 1, pull up resistor
        t = not io.input(pins[i])

        #print("pin:"+str(pins[i])+" is "+str(io.input(pins[i])))

        v |= t<<i
    return v

value_pins = [7,8,25,24,23,18,15,14]
address_pins = [27,17,4,3]
enable_pin = 2

def read_addr(addr):
    quick_set(address_pins, addr)
    return value_read(value_pins)

def read_code():
    r = []
    for i in range(0,15):
        r.append(read_addr(i))
    return r


try:
    io.setmode(io.BCM)

    # enable for the entire board (0=on)
    io.setup(enable_pin,io.OUT)
    io.output(enable_pin,False)

    quick_setup(value_pins, io.IN)
    quick_setup(address_pins, io.OUT)
    
    quick_set(address_pins, 0)


    
    addr = 0
    while (1):
        print(read_code())
        #value_read(value_pins)
        time.sleep(0.1)
              
finally:
    io.cleanup()

