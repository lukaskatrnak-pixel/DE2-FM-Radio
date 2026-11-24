# GPIO Pin Mapping (Raspberry Pi Pico W)

This pinout matches the current hardware configuration defined in `src/config.py`.

| Module | Module Pin | Pico GPIO | Physical Pin | Bus / Mode | Power |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Si4703 FM Tuner** | SDIO (SDA) | `GP4` | Pin 6 | `I2C0` (100 kHz, addr `0x10`) | 3.3 V (Pin 36) |
| **Si4703 FM Tuner** | SCLK (SCL) | `GP5` | Pin 7 | `I2C0` (100 kHz, addr `0x10`) | 3.3 V (Pin 36) |
| **Si4703 FM Tuner** | RST | `GP18` | Pin 24 | Digital OUT (2-wire I²C init) | — |
| **OLED 128×64** | SDA | `GP2` | Pin 4 | `I2C1` (400 kHz, addr `0x3C` / `0x3D`) | 3.3 V (Pin 36) |
| **OLED 128×64** | SCL (SCK) | `GP3` | Pin 5 | `I2C1` (400 kHz, addr `0x3C` / `0x3D`) | 3.3 V (Pin 36) |
| **KY-040 Encoder** | CLK | `GP14` | Pin 19 | Digital IN (`Pin.PULL_UP`) | 3.3 V (Pin 36) |
| **KY-040 Encoder** | DT | `GP15` | Pin 20 | Digital IN (`Pin.PULL_UP`) | — |
| **KY-040 Encoder** | SW | `GP16` | Pin 21 | Digital IN (`Pin.PULL_UP`) | — |
| **All Modules** | GND | `GND` | Pin 3, 8, 13, 18, 23, 28, 33, 38 | Common Ground | GND |

## Power & Wiring Notes
* **Logic & Supply Voltage:** All connected modules operate at **3.3 V logic** powered from the Pico W `3V3(OUT)` pin (Pin 36) and must share a common `GND`.
* **Separate I²C Buses:** The Si4703 uses its own bus (`I2C0`, 100 kHz) because its startup sequence pulls `SDIO` low while releasing `RST` to enter 2-wire I²C mode. Keeping the OLED on `I2C1` (400 kHz) prevents bus conflicts and allows faster screen updates.
* **Audio & Antenna:** Connect headphones or a powered amplifier directly to the Si4703 3.5 mm audio jack (never to a Pico GPIO). The headphone cable acts as the FM antenna.
* **Optional Extensions:** The optional 4-digit secondary display pinout remains TBD.
