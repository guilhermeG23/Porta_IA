#Use -> Python 3

#Libs
import RPi .GPIO as GPIO
import time
import Recogniser_Video_EigonFace

#GPIO rasp
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN) #Porta do sensor PIR

#Motor
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18, 100)
pwm.start(5)
 
def motor(angle):
    duty = float(angle) / 10.0 + 2.5
    pwm.ChangeDutyCycle(duty)
    return True

#Loop
try:
    nome = input("Achar quem?: ")
    contador = 1000
    #Loop
    while True:
        time.sleep(5)
        #Se tiver sinal, resulta em TRUE
        if GPIO.input(23):
            #Captura quando tiver true
            print("movimento detectado...")
            resultado = Recogniser_Video_EigonFace.detectar(nome, contador)
            print(resultado)
        else:
            print("Nada detectado...")

#Deu errado, sai e limpa a config do GPIO
except (RuntimeError, TypeError, NameError):
    print("Deu errado")
    GPIO.cleanup()
