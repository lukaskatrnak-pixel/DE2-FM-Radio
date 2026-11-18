"""Step 4: turn the knob / press the button, watch the console."""
from rotary_encoder import RotaryEncoder
from time import sleep_ms
enc = RotaryEncoder()
while True:
    step, pressed = enc.read()
    if step or pressed:
        print('step:', step, 'press:', pressed)
    sleep_ms(5)
