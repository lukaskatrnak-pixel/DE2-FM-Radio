"""OLED UI. Requires the standard MicroPython ssd1306.py driver on the Pico."""
import config


class OLEDUI:
    def __init__(self, i2c=None):
        from machine import I2C, Pin
        from ssd1306 import SSD1306_I2C
        if i2c is None:
            i2c = I2C(config.OLED_I2C_ID, sda=Pin(config.OLED_SDA),
                      scl=Pin(config.OLED_SCL), freq=400_000)
        addresses = i2c.scan()
        if 0x3C not in addresses and 0x3D not in addresses:
            raise OSError('OLED not found at 0x3C / 0x3D')
        address = 0x3C if 0x3C in addresses else 0x3D
        self.oled = SSD1306_I2C(config.OLED_WIDTH, config.OLED_HEIGHT, i2c, addr=address)

    def render(self, frequency, volume, rssi, mode):
        d = self.oled
        d.fill(0)
        d.text('PICO FM RADIO', 0, 0)
        d.text('{:.1f} MHz'.format(frequency), 0, 18)
        d.text('RSSI: {}'.format(rssi), 0, 36)
        d.text('Vol:{} Mode:{}'.format(volume, mode), 0, 52)
        d.show()
