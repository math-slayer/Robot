#Author: Akhil Nallacheruvu
#The purpose of this program is to test the motor drive integrated circuit and verify that the motors and IC function effectively
import RPi.GPIO as GPIO      #The 5V inputs from the sensors are outputted at 3.3V from the Raspberry Pi GPIO.
import time
motors=[13,19,26,12,23,24]    #GPIO pins being used to control motor
r_enable=12      #Enables Right Motor
r_for=24         #Drives Right Motor Forward
r_rev=23        #Drives Right Motor Backward
l_enable=13      #Enables Left Motor
l_for=19         #Drives left motor forward
l_rev=26         #Drives Left Motor Backward
GPIO.setmode(GPIO.BCM)
GPIO.setup(motors,GPIO.OUT)
GPIO.output(motors, GPIO.LOW)
GPIO.output(r_enable,1)
GPIO.output(l_enable,1)
def drive_motor(pin):      #this function controls the direction of the motor's motion
    print(pin)
    GPIO.output(pin,1)
    time.sleep(1)       #Motor drives for 1 second
    GPIO.output(pin,0)
    time.sleep(0.5)     #Robot motors rest for 0.5 seconds

#Implementation of Function
drive_motor(r_for)
drive_motor(r_rev)
drive_motor(l_for)
drive_motor(l_rev)

GPIO.cleanup()
    
    
