"""Step 1: expect Si4703 0x10 on I2C0 and OLED 0x3c on I2C1."""
from machine import I2C, Pin
import config
from si4703 import Si4703
radio = Si4703()
print('I2C0 (radio):', [hex(x) for x in radio.i2c.scan()])
oled_bus = I2C(config.OLED_I2C_ID, sda=Pin(config.OLED_SDA),
               scl=Pin(config.OLED_SCL), freq=400_000)
print('I2C1 (OLED): ', [hex(x) for x in oled_bus.scan()])
