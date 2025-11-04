#SCRIPT FOR LED 8X8: max7219
from time import sleep
from luma.core.interface.serial import spi
from luma.led_matrix.device import max7219
from luma.core.render import canvas

serial = spi(port=0, device=0)
device = max7219(serial, cascaded=1, block_orientation=0, rotate=0)

# Define una "1" pixelada 8x8
# 1 = encendido, 0 = apagado
heart = [
    [0,0,1,0,0,1,0,0],
    [0,1,1,1,1,1,1,0],
    [1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1],
    [0,1,1,1,1,1,1,0],
    [0,0,1,1,1,1,0,0],
    [0,0,0,1,1,0,0,0],
    [0,0,0,0,0,0,0,0]
]

while True:
    for i in heart:
        with canvas(device) as draw:
            for y, row in enumerate(heart):
                for x, pixel in enumerate(row):
                    if pixel:
                        draw.point((x, y), fill="white")
        sleep(1)
        device.clear()