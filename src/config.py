"""GPIO configuration for the Pico FM radio (matches the real wiring)."""
# Si4703 tuner on I2C0
I2C_ID = 0
I2C_SDA = 4          # GP4, physical pin 6
I2C_SCL = 5          # GP5, physical pin 7
I2C_FREQ = 100_000
RADIO_RST = 18        # GP18, physical pin 24
RADIO_ADDRESS = 0x10

# OLED on its own bus I2C1
OLED_I2C_ID = 1
OLED_SDA = 2         # GP2, physical pin 4
OLED_SCL = 3         # GP3, physical pin 5
OLED_WIDTH = 128
OLED_HEIGHT = 64

# KY-040 rotary encoder
ENC_CLK = 14
ENC_DT = 15
ENC_SW = 16

START_FREQUENCY = 99.5
FREQ_MIN = 87.5
FREQ_MAX = 108.0
STEP = 0.1
START_VOLUME = 5
