import time
import board
import busio
import RPi.GPIO as GPIO
from adafruit_ads1x15.ads1x15 import ADS1x15
from adafruit_ads1x15.ads1115 import ADS1115
from adafruit_ads1x15.analog_in import AnalogIn

# --- Configuración GPIO ---
DIGITAL_PIN = 17  # DOUT del sensor
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIGITAL_PIN, GPIO.IN)

# --- Configuración I2C y ADC ---
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS1115(i2c)
chan = AnalogIn(ads, 0)  # Canal A0 del ADS1115

print("Probando sensor de humedad del suelo (analógico + digital)...\n")

try:
    while True:
        # Lectura analógica
        value = chan.value
        volts = chan.voltage
        humedad = round(100 - (value / 32767.0) * 100, 2)

        # Lectura digital
        estado = GPIO.input(DIGITAL_PIN)
        estado_str = "HÚMEDO" if estado == 0 else "SECO"

        print(f"Analog: {value} | {volts:.2f} V | Humedad estimada: {humedad}% | Digital: {estado_str}")
        time.sleep(1)

except KeyboardInterrupt:
    print("\nPrueba interrumpida por el usuario.")
    GPIO.cleanup()

except Exception as e:
    print(f"Error: {e}")
    GPIO.cleanup()
