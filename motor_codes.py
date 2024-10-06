import RPi.GPIO as GPIO
import time

steps_per_rev = 200

GPIO.setmode(GPIO.BCM)  
motor1 = 17  
motor1_direction_pin = 27
motor2 = 23  
motor2_direction_pin = 24
GPIO.setup(motor1, GPIO.OUT)
GPIO.setup(motor1_direction_pin, GPIO.OUT)
GPIO.setup(motor2, GPIO.OUT)
GPIO.setup(motor2_direction_pin, GPIO.OUT)


def rotate_motor(mot, steps, dir = 'clockwise'):
    if mot == motor1:
        direction_pin = motor1_direction_pin
    elif mot == motor2:
        direction_pin = motor2_direction_pin

    if dir == "clockwise":
        GPIO.output(direction_pin, GPIO.HIGH)
    elif dir == "anticlockwise":
        GPIO.output(direction_pin, GPIO.LOW)
    
    step_count = 0
    while (step_count < steps):
        GPIO.output(mot, GPIO.HIGH)
        time.sleep(0.008)  
        GPIO.output(mot, GPIO.LOW)
        time.sleep(0.008)  
        step_count += 1

def test_motor1():
    rotate_motor(motor1, 200)
    time.sleep(1)
    rotate_motor(motor1, 200, 'anticlockwise')
    time.sleep(1)

def test_motor2():
    rotate_motor(motor2, 200)
    time.sleep(1)
    rotate_motor(motor2, 200, 'anticlockwise')
    time.sleep(1)

