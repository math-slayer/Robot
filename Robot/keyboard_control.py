#Author: Akhil Nallacheruvu
#The purpose of this program is to control the robot from my keyboard
from tkinter import Tk
import RPi.GPIO as GPIO
motors=[13,19,26,12,23,24]
r_enable=12
r_for=24
r_rev=23
l_enable=13
l_for=19
l_rev=26
r_fast=80
l_fast=80
r_slow=40
l_slow=40
GPIO.setmode(GPIO.BCM)
GPIO.setup(motors,GPIO.OUT)
GPIO.output(motors,GPIO.LOW)
pwm_right=GPIO.PWM(r_enable,1000)
pwm_left=GPIO.PWM(l_enable,1000)
pwm_right.start(r_fast)
pwm_left.start(l_fast)

def on_close():
    print("Quitting Program")
    GPIO.cleanup()
    root.destroy()    #This function quits the program when a certain keyboard key is pressed

def up_arrow(event):
    pwm_right.ChangeDutyCycle(r_fast)
    pwm_left.ChangeDutyCycle(l_fast)
    GPIO.output(r_rev,0)
    GPIO.output(r_for,1)
    GPIO.output(l_rev,0)
    GPIO.output(l_for,1)
    #This function sets up the up arrow to make the robot go forward

def down_arrow(event):
    pwm_right.ChangeDutyCycle(r_fast)
    pwm_left.ChangeDutyCycle(l_fast)
    GPIO.output(r_rev,1)
    GPIO.output(r_for,0)
    GPIO.output(l_rev,1)
    GPIO.output(l_for,0)
    #This function sets up the down arrow to make the robot go backwards

def left_arrow(event):
    pwm_right.ChangeDutyCycle(r_slow)
    pwm_left.ChangeDutyCycle(l_slow)
    GPIO.output(r_rev,0)
    GPIO.output(r_for,1)
    GPIO.output(l_rev,1)
    GPIO.output(l_rev,0)
    #This function makes the left arrow turn the robot to the left

def right_arrow(event):
    pwm_right.ChangeDutyCycle(r_slow)
    pwm_left.ChangeDutyCycle(l_slow)
    GPIO.output(r_rev,1)
    GPIO.output(r_for,0)
    GPIO.output(l_rev,0)
    GPIO.output(l_rev,1)
    #This function makes the right arrow turn the robot to the right

def stop(event):
    GPIO.output(r_rev,0)
    GPIO.output(r_for,0)
    GPIO.output(l_rev,0)
    GPIO.output(l_for,0)
    #This function stops the robot

root=Tk()
root.bind('<Up>', up_arrow)
root.bind('<Down>', down_arrow)
root.bind('<Left>', left_arrow)
root.bind('<Right>',right_arrow)
root.bind('<space>',stop)
root.bind("WM_DELETE_WINDOW",on_close)
root.mainloop()
#The final parts of the program were programmed in shell scripting to correspond computer keys with functions
