# Tracking-Line-Robot-Car
Tracking Line Robot Car
![1717421451749](https://github.com/MTsaoy/Tracking-Line-Robot-Car/assets/169100462/4f5784f8-da3f-4e58-815e-c6a1381d6e68)

For a subject in University, I and my classmate Kleoniki Fragkaki, called to build a Smart Robot Car project that will perceive and follow a black tape with Raspberry Pi Poco in Micropython.

It's a simple project and we just need a few accessories to implement it.

# Accessories:

1x Board

2x Motors

2x Wheels

1x Battery base 80-100mA

1x Maker Raspberry Pi RP2040 

1x 3 Channel IR Infrared Tracking Tracing sensor Module CTRT5000

2x Grove to Female Header Cable

1x Screwdriver

![1717421451700](https://github.com/MTsaoy/Tracking-Line-Robot-Car/assets/169100462/a5749d9e-533f-483c-a4d3-67abdcca79fa)


# 1st Step: Connect the motors to the bottom side of the board and connect the power cables as shown in the picture.

![1717421451706](https://github.com/MTsaoy/Tracking-Line-Robot-Car/assets/169100462/516cb761-00a8-40ba-9d00-aebcd30cfbce)

# 2nd Step: Attach the power supply on the back of the board, along with the Maker Pi board and the wheels.
 
![1717421451716](https://github.com/MTsaoy/Tracking-Line-Robot-Car/assets/169100462/ff1e5941-6292-4d97-8c9c-4149b8b47808)

# 3rd Step: Connect the jumper cables to the board as well as the power cables for the base with the batteries as shown in the picture.
 
![1717421451723](https://github.com/MTsaoy/Tracking-Line-Robot-Car/assets/169100462/73179831-63c2-4330-bc79-9dcfccaa004c)

# 4th Step: Then we also place the rear wheel of the vehicle and the view so far is something like this.
 
![1717421451733](https://github.com/MTsaoy/Tracking-Line-Robot-Car/assets/169100462/6423e18e-c5d9-476f-9115-364632265b41)

# 5th Step: Create a box from a paper and open holes along the length where the sensors are located so that it works as a base.
 
![IMG_20240603_161301](https://github.com/MTsaoy/Tracking-Line-Robot-Car/assets/169100462/fc9ba6d6-abc1-439d-aec8-2cad719c07b6)

# 6th Step: Connect the sensor cables and pass them through the board holes so that they pass through the other side and connect to the Maker Pi.
 
![1717421451740](https://github.com/MTsaoy/Tracking-Line-Robot-Car/assets/169100462/829cbf4b-4074-4722-98ed-e1dff2477d56)

# 7th Step: Finally, we connect the sensor to the Groove positions and the design of the car is ready.
 
Then we have to connect the Robot Car to the computer in order to give it commands through [Micropython](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html).

# The code in Micropython is not complicated and seems like this:

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

# Below there are links to order the Accessories:
https://www.skroutz.gr/s/32863022/Haitronic-2WD-Smart-Robot-Car-Chassis-Kit-for-Arduino-HR0238.html
https://nettop.gr/index.php/raspberry-pi/pico/raspberry-pi-pico-accessories/maker-pi-rp2040-simplifying-robotics-with-raspberry-pi-rp2040.html
https://nettop.gr/index.php/eksartimata/aisthitires/proximity/3-channle-ir-infrared-tracking-tracing-sensor-module-ctrt5000.html

# Cost of the project
The whole cost for the Smart Robot Car it is about 25-28€

The board with the wheels, the motors, and the cables costs 8-10€

The 3 Channel Sensor costs 5.00€

The Maker Pi Poco costs 12.90€
