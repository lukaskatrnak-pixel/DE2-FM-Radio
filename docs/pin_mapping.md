# Preliminary GPIO mapping — NOT YET VERIFIED

|Module|Signal|Pico GPIO|
|-|-|-|
|Si4703|SDIO / SDA|GP4|
|Si4703|SCLK / SCL|GP5|
|Si4703|RST|GP6|
|OLED I²C|SDA|GP4|
|OLED I²C|SCL (sometimes marked SCK)|GP5|
|KY-040|CLK|GP14|
|KY-040|DT|GP15|
|KY-040|SW|GP16|

All modules must share a common GND and use verified voltage levels. Before connecting, check the exact breakout's pinout and mode-select/initialization requirements. The 4-digit display pinout remains TBD.

