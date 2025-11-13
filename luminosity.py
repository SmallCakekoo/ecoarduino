import smbus2
import time

# Dirección del sensor (0x23 por defecto, o 0x5C si el pin ADDR está a VCC)
BH1750_ADDRESS = 0x23

# Comandos del sensor
BH1750_CONTINUOUS_HIGH_RES_MODE = 0x10

# Inicia bus I2C
bus = smbus2.SMBus(1)

def read_light():
    # Envía comando para modo continuo de alta resolución
    bus.write_byte(BH1750_ADDRESS, BH1750_CONTINUOUS_HIGH_RES_MODE)
    time.sleep(0.2)
    data = bus.read_i2c_block_data(BH1750_ADDRESS, 0x00, 2)
    light_level = ((data[0] << 8) | data[1]) / 1.2  # Conversión a lux
    return light_level

if __name__ == "__main__":
    print("Midiendo luminosidad... (Ctrl+C para detener)")
    try:
        while True:
            lux = read_light()
            print(f"Luminosidad: {lux:.2f} lx")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nMedición detenida.")
