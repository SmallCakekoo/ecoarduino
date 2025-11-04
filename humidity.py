from time import sleep
import RPi.GPIO as GPIO

YL69_DO = 17  # Cambia al GPIO que uses para el pin digital DO

GPIO.setmode(GPIO.BCM)
GPIO.setup(YL69_DO, GPIO.IN)

try:
    while True:
     if GPIO.input(YL69_DO) == 0:  # Sensor detecta humedad (LOW)
      print("Húmedo")
    else:  # Sensor detecta seco (HIGH)
      print("Seco")
    sleep(1)  # Espera 1 segundo
except KeyboardInterrupt:
    print("Programa detenido")
finally:
    GPIO.cleanup()
