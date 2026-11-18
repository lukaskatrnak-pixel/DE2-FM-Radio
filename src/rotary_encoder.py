"""Simple polled KY-040 rotary encoder (no IRQ allocations)."""
from machine import Pin
from time import ticks_ms, ticks_diff
import config


class RotaryEncoder:
    def __init__(self):
        self.clk = Pin(config.ENC_CLK, Pin.IN, Pin.PULL_UP)
        self.dt = Pin(config.ENC_DT, Pin.IN, Pin.PULL_UP)
        self.sw = Pin(config.ENC_SW, Pin.IN, Pin.PULL_UP)
        self.last_clk = self.clk.value()
        self.last_button = self.sw.value()
        self.last_press_ms = ticks_ms()

    def read(self):
        """Return (step, pressed), step is -1, 0, or +1."""
        step = 0
        current = self.clk.value()
        if current != self.last_clk and current == 0:
            step = 1 if self.dt.value() != current else -1
        self.last_clk = current

        pressed = False
        now = ticks_ms()
        button = self.sw.value()
        if button == 0 and self.last_button == 1 and ticks_diff(now, self.last_press_ms) > 200:
            pressed = True
            self.last_press_ms = now
        self.last_button = button
        return step, pressed
