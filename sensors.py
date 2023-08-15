import RPi.GPIO as GPIO
import time

def ultrasonic(echopin, trigpin):
    GPIO.setmode(GPIO.BCM)
    ECHO = echopin
    TRIG = trigpin
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.output(TRIG, GPIO.LOW) 
    time.sleep(0.000002) 
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.000010)
    GPIO.output(TRIG, GPIO.LOW)
    while GPIO.input(ECHO)==0: 
        start_time = time.time() 
    while GPIO.input(ECHO)==1: 
        return_time = time.time() 
    pulse_duration = return_time - start_time 
    distance = pulse_duration * 0.034/2