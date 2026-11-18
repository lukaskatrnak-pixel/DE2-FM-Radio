"""Step 2: tune and read signal strength."""
from si4703 import Si4703
radio = Si4703()
print('RSSI:', radio.signal_strength())
print('Tuned to:', radio.set_frequency(99.5), 'MHz')
