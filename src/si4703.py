"""Basic Si4703 I2C FM receiver driver for MicroPython / RP2040.

Based on the Si4703 programming sequence described by Silicon Labs AN230
and the SparkFun Si4703 hookup guide; implementation is original for this project.
"""
from machine import Pin, I2C
from time import sleep_ms, ticks_ms, ticks_diff
import config


class Si4703:
    ADDRESS = config.RADIO_ADDRESS

    def __init__(self):
        self.registers = [0] * 16
        self.i2c = None
        self._reset_into_i2c()
        self._initialize()

    def _reset_into_i2c(self):
        # Pull SDIO low while reset is released: selects 2-wire mode.
        # On this breakout, SEN is already pulled up on the PCB.
        reset = Pin(config.RADIO_RST, Pin.OUT, value=0)
        sdio = Pin(config.I2C_SDA, Pin.OUT, value=0)
        sleep_ms(2)
        reset.value(1)
        sleep_ms(2)
        sdio.init(Pin.IN, Pin.PULL_UP)
        self.i2c = I2C(config.I2C_ID,
                       sda=Pin(config.I2C_SDA),
                       scl=Pin(config.I2C_SCL),
                       freq=config.I2C_FREQ)
        sleep_ms(10)
        if self.ADDRESS not in self.i2c.scan():
            raise OSError('Si4703 not found at I2C address 0x10')

    def _read(self):
        # Read 0x0A...0x0F then 0x00...0x09 (no register address byte).
        data = self.i2c.readfrom(self.ADDRESS, 32)
        for n in range(16):
            index = (0x0A + n) & 0x0F
            self.registers[index] = (data[2*n] << 8) | data[2*n+1]

    def _write(self):
        # Writes always begin at register 0x02, continuing through 0x07.
        data = bytearray(12)
        for i, reg in enumerate(range(0x02, 0x08)):
            value = self.registers[reg]
            data[2*i] = (value >> 8) & 0xFF
            data[2*i + 1] = value & 0xFF
        self.i2c.writeto(self.ADDRESS, data)

    def _initialize(self):
        self._read()
        # Enable internal oscillator, then wait for stabilization.
        self.registers[0x07] = 0x8100
        self._write()
        sleep_ms(500)
        self._read()
        self.registers[0x02] = 0x4001     # DMUTE + ENABLE
        self.registers[0x04] |= 0x0800    # DE = 50us (Europe)
        self.registers[0x05] &= ~0x00F0   # clear BAND and SPACE bits
        self.registers[0x05] |= 0x0010    # 87.5-108MHz, 100kHz spacing
        self.registers[0x05] = (self.registers[0x05] & ~0x000F) | config.START_VOLUME
        self._write()
        sleep_ms(120)
        self.set_frequency(config.START_FREQUENCY)

    def _wait_stc(self, required, timeout_ms=1500):
        start = ticks_ms()
        while ticks_diff(ticks_ms(), start) < timeout_ms:
            self._read()
            if bool(self.registers[0x0A] & 0x4000) == required:
                return
            sleep_ms(10)
        raise OSError('Si4703 tuning timeout; check wiring and antenna')

    def set_frequency(self, mhz):
        mhz = round(max(config.FREQ_MIN, min(config.FREQ_MAX, mhz)), 1)
        channel = int(round((mhz - 87.5) * 10))
        self._read()
        self.registers[0x03] = 0x8000 | (channel & 0x03FF)
        self._write()
        try:
            self._wait_stc(True)
        finally:
            self.registers[0x03] &= ~0x8000
            self._write()
        self._wait_stc(False)
        return mhz

    def signal_strength(self):
        self._read()
        return self.registers[0x0A] & 0xFF

    def set_volume(self, value):
        value = max(0, min(15, int(value)))
        self._read()
        self.registers[0x05] = (self.registers[0x05] & ~0x000F) | value
        self._write()
        return value
