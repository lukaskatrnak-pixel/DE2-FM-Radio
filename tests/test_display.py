"""Step 3: OLED only (no radio needed)."""
from oled_ui import OLEDUI
OLEDUI().render(99.5, 5, 0, 'TEST')
print('OLED test drawn')
