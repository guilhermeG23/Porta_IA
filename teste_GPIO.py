#Use -> Python 3

#Libs
import RPi .GPIO as GPIO
import picamera
import time

#GPIO rasp
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN) #Porta do sensor PIR

#Modulo de camera
camera = picamera.PiCamera()

#Loop
try:
    #Loop
    while True:
        time.sleep(5)
        
        #Se tiver sinal, resulta em TRUE
        if GPIO.input(23):
            #Captura quando tiver true
            print("movimento detectado...\nCapturando momento!")
            camera.capture("teste.jpg")
        else:
            print("Nada detectado...")

#Deu errado, sai e limpa a config do GPIO
except:
    GPIO.cleanup()