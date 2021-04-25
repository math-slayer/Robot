#Author: Akhil Nallacheruvu
#The purpose of this program is to calibrate the sensors to follow any black line that is drawn on a paper at the given speeds. Code is reused from IC test programs because GPIO pins are the same
import RPi.GPIO as GPIO
import time
motors=[13,19,26,12,23,24]
r_enable=12
r_for=24
r_rev=23
l_enable=13
l_for=19
l_rev=26
l_line=27    #Left Line Sensor
r_line=4     #Right Line Sensor
obs_right=17   #Right Obstacle Sensor
end=0
motor_fast=60      #speed of motor when it is going forward
motor_slow=30      #speed of motor when it is going backward
GPIO.setmode(GPIO.BCM)
GPIO.setup(motors,GPIO.OUT)
GPIO.setup(l_line,GPIO.IN)
GPIO.setup(r_line, GPIO.IN)
GPIO.setup(obs_right,GPIO.IN)
l_pwm=GPIO.PWM(l_enable,1000)    
l_pwm.start(motor_fast)       #Left motor duty cycle is enabled and motor starts going at a speed of 60
r_pwm=GPIO.PWM(r_enable,1000)
r_pwm.start(motor_fast)
try:
    while end==0:
        while GPIO.input(l_line)==False:
            r_pwm.ChangeDutyCycle(motor_slow)
            GPIO.output(l_for,0)
            GPIO.output(l_rev,1)
            time.sleep(0.01)
            #The left motor reverses the left wheel and then pauses for 0.01 seconds
       while GPIO.input(r_line)==False:
           l_pwm.ChangeDutyCycle(motor_slow)
           GPIO.output(r_for,0)
           GPIO.output(r_rev,1)
           time.sleep(0.01)
           #The right motor reverses the right wheel and pauses for 0.01 seconds
        if GPIO.input(obs_right)==False:
            GPIO.output(r_for,0)
            GPIO.output(l_for,0)
            GPIO.output(r_rev,0)
            GPIO.output(l_rev,0)
            print("Shutdown")
            end=1
        else:
            r_pwm.ChangeDutyCycle(motor_fast)
            l_pwm.ChangeDutyCycle(motor_fast)
            GPIO.output(l_rev,0)
            GPIO.output(r_rev,0)
            GPIO.output(l_for,1)
            GPIO.output(r_for,1)
finally:
    GPIO.cleanup()


