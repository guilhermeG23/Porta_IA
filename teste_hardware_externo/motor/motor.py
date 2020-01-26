import RPi.GPIO as GPIO
import time

servo_pin = 18

deg_0_pulse = 0.5
deg_180_pulse = 2.5
f = 50.0

period = 1000/f
k = 100/period
deg_0_duty = deg_0_pulse*k
pulse_range = deg_180_pulse - deg_0_pulse
duty_range = pulse_range * k

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
pwm = GPIO.PWM(servo_pin, f)
pwm.start(0)

def set_angle(angle):
    duty = deg_0_duty + (angle/180.0) * duty_range
    pwm.ChangeDutyCycle(duty)
    print(duty)

try:
    while True:
        angle = int(input("Entre com o valor:"))
        set_angle(angle)

finally:
    print("limp")
    GPIO.cleanup()
