from machine import Pin, PWM
from time import sleep

# Inputs and Outputs
ENA = PWM(Pin(1))
M1A = Pin(8,Pin.OUT)
M1B = Pin(9,Pin.OUT)
M2A = Pin(10,Pin.OUT)
M2B = Pin(11,Pin.OUT)
ENB = PWM(Pin(6))
right = Pin(0, Pin.IN)
middle = Pin(7, Pin.IN)
left = Pin(28, Pin.IN)

# values of the sensors
def lineTracking():
    sleep(0.05)
    return[left.value(),middle.value(),right.value()]

# Main function of the robot
def robot():
    sensorValues = lineTracking()
    if sensorValues == [1,1,1]:
        stop()
    elif sensorValues == [0,0,0]:
        stop()
    elif sensorValues == [1,0,1]:
        forward()
    elif sensorValues == [0,1,1]:
        turnLeft()
    elif sensorValues == [0,0,1]:
        turnLeft()
    elif sensorValues == [1,1,0]:
        turnRight()
    elif sensorValues == [1,0,0]:
        turnRight()

# Moves of the robot
def forward():
    M1A.on()
    M1B.off()
    M2A.on()
    M2B.off()
    
def turnRight():
    M1A.on()
    M1B.off()
    M2A.off()
    M2B.on()
    
def turnLeft():
    M1A.off()
    M1B.on()
    M2A.on()
    M2B.off()
    
def stop():
    M1A.off()
    M1B.off()
    M2A.off()
    M2B.off()

# the main programm
if   __name__ == '__main__':
    try:
        while True:
            robot()
    except KeyboardInterrupt:
        stop()
