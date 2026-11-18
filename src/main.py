"""Run on Pico after uploading required modules (including ssd1306.py)."""
from time import sleep_ms, ticks_ms, ticks_diff
import config
from si4703 import Si4703
from oled_ui import OLEDUI
from rotary_encoder import RotaryEncoder


def main():
    radio = Si4703()  # Reset tuner first (2-wire mode).
    display = OLEDUI()
    encoder = RotaryEncoder()
    frequency = config.START_FREQUENCY
    volume = config.START_VOLUME
    mode = 'TUNE'
    updated = True
    last_refresh = ticks_ms()
    while True:
        step, pressed = encoder.read()
        if pressed:
            mode = 'VOL' if mode == 'TUNE' else 'TUNE'
            updated = True
        if step:
            if mode == 'TUNE':
                frequency = radio.set_frequency(frequency + step * config.STEP)
            else:
                volume = radio.set_volume(volume + step)
            updated = True
        if updated or ticks_diff(ticks_ms(), last_refresh) > 1000:
            strength = radio.signal_strength()
            display.render(frequency, volume, strength, mode)
            last_refresh = ticks_ms()
            updated = False
        sleep_ms(5)


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print('FM Radio error:', exc)
        raise
