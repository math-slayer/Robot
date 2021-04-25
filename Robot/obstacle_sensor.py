#Author: Akhil Nallacheruvu
#The purpose of this program is to program the obstacle sensors to detect obstacles and send a signal to the motor to avoid them
import RPi.GPIO as GPIO
import time
trigger=20    #This is the GPIO pin location of the signal that is sent to the motors from the IC connections between the sensors and motors
echo=21    #ultrasonic obstacle sensor's GPIO pin location
motors=[12,24,23,13,19,26]
r_enable=12
r_for=24
r_rev=23
l_enable=13
l_for=19
l_rev=26
obs_left=22
obs_right17
r_speed=60
l_speed60
turn_delay=0.5       #The motor will turn 0.5 seconds after detecting obstacle so that it doesn't overheat
GPIO.setmode(GPIO.BCM)
GPIO.setup(trigger, GPIO.OUT)     #The signal has been set as an output
GPIO.setup(echo,GPIO.IN)          #the ultrasonic obstacle sensor has been set as an input
GPIO.setup(motors,GPIO.OUT)     #The motors have been set as an output
GPIO.setup(obs_left,GPIO.IN)
GPIO.setup(obs_right,GPIO.IN)      #The corner obstacle sensors(left and right) have been set as inputs
r_pwm=GPIO.PWM(r_enable,1000)
r_pwm.start(r_speed)
l_pwm=GPIO.PWM(l_enable,1000)
l_pwm.start(l_speed)

def range_check():
    GPIO.output(trigger, True)
    time.sleep(0.00001)
    GPIO.output(trigger, False)
    start_timer=time.time()
    while GPIO.input(echo)==True:
        stop_timer=time.time()
    elapsed_time= stop_timer-start_timer
    distance=(elpased_time*34300)/2
    return distance
#The purpose of this function is to determine the distance away from the obstacle when the robot would have to activate the trigger

def stop():
    GPIO.output(r_for,0)
    GPIO.output(l_for,0)
    GPIO.output(r_rev,0)
    GPIO.output(l_rev,0)
    time.sleep(0.1)
#This function is used to stop the robot when an obstacle is faced

def reverse():
    stop()
    GPIO.output(r_rev,1)
    GPIO.output(l_rev,1)
    time.sleep(0.5)
    stop()

try:
    while True:
        distance=range_check()
        if(distance<=10):
            stop()
            print("Emergency Stop")
            raise SystemExit()      #The robot stops if it encounters obstacles 10cm or less away from it
        elif(distance>10 and distance<20):
            reverse()
            GPIO.output(r_for,1)
            GPIO.output(l_rev,1)
            time.sleep(turn_delay)
            stop()
            #The robot reverses and turns left when faced with an obstacle 10-20cm away from it
       elif GPIO.input(obs_right)==False:
           reverse()
           GPIO.output(r_for,1)
           GPIO.output(l_rev,1)
           time.sleep(turn_delay)
           stop()         #The robot turns left if there is no signal from right obstacle sensor

        elif GPIO.input(obs_left)==False:
            reverse()
            GPIO.output(r_rev,1)
            GPIO.output(l_for,1)
            time.sleep(turn_delay)
            stop()                #The robot turns right if there is no signal from left obstacle sensor
    
        else:
            GPIO.output(r_for,1)
            GPIO.output(l_for,1)
        time.sleep(0.05)
except(KeyboardInterrupt, SystemExit):
    stop()
    GPIO.cleanup()

 
