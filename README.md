# DE2-FM-Radio (Raspberry Pi Pico)

[![MicroPython](https://img.shields.io/badge/MicroPython-1.22+-blue.svg)](https://micropython.org/)
[![Platform](https://img.shields.io/badge/Platform-Raspberry%20Pi%20Pico-red.svg)](https://www.raspberrypi.com/products/raspberry-pi-pico/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

FM Radio Receiver embedded systems term project for the **Digital Electronics 2 (DE2)** course at the **Faculty of Electrical Engineering and Communication (FEEC), Brno University of Technology (BUT)**.

---

## 👥 Team Members & Responsibilities

| Name | Role / Focus Area |
|---|---|
| **Lukáš Katrňák** | README,  |
| **Aitken Alisher** | Source code,  |
| **Murat Assiya** | Poster, Design |

---

## 📖 Project Overview

## 1. Project overview

This project develops a compact FM receiver with digital tuning. A Raspberry Pi Pico WH controls an **Si4703 FM tuner** through I²C. A rotary encoder provides frequency and menu control, while an OLED display presents frequency, volume and signal information. A 4-digit display may be used as an optional secondary readout.
### Problem Statement
[Popsat projekt. Např.: Cílem projektu je vytvořit digitálně laditelný FM přijímač, který nahradí nepřesné analogové ladění a umožní přehledné zobrazení informací uživateli.]

### Solution Summary
The **FM Radio Receiver** is based on the **Raspberry Pi Pico** running MicroPython. It:
1. Tunes FM frequencies using an I2C tuner module (e.g., [Typ modulu]).
2. Displays the current frequency on a [Typ displeje] display.
3. Allows frequency tuning and station selection using a rotary encoder.

---
## 2. Features and scope

### Minimum working scope
- Tune the receiver using a KY-040 rotary encoder.
- Display the selected frequency on an OLED screen.
- Route audio from the Si4703 headphone jack to headphones or a powered amplifier.

### Planned extensions
- Show signal quality / RSSI (as supported by the tuner).
- Save and select station presets.
- Automatically seek stations.
- Optional second 4-digit display.

*These are project goals, not claims of completed or tested functionality.*

## 3. Hardware
## 🛠️ Hardware Inventory & Wiring
## 4. Repository layout

```text
pico_fm_radio_2026/
├── README.md
├── LICENSE
├── .gitignore
├── src/
│   ├── main.py
│   ├── config.py
│   ├── si4703.py
│   ├── oled_ui.py
│   ├── rotary_encoder.py
│   └── presets.py
├── hardware/
│   ├── README.md
│   ├── bom.csv
│   └── pin_mapping.md
├── tests/
│   ├── README.md
│   ├── test_i2c_scan.py
│   ├── test_encoder.py
│   ├── test_display.py
│   └── test_radio.py
├── docs/
│   ├── architecture.md
│   ├── test_results.md
│   └── team_roles.md
└── media/
    └── README.md
```
## 5. Software architecture

- `src/si4703.py` — tuner control and readout (to implement).
- `src/oled_ui.py` — OLED rendering (to implement).
- `src/rotary_encoder.py` — rotary and button input (to implement).
- `src/presets.py` — saved station list (to implement).
- `src/main.py` — application integration (to implement).

The MicroPython OLED library and tuner initialization procedure will be selected after verifying the exact boards.

## 6. Testing plan

1. Verify 3.3 V power and ground wiring.
2. Scan the I²C bus; confirm responding devices and addresses.
3. Test the encoder and button independently.
4. Test OLED text output.
5. Initialize the Si4703 and tune a known local FM station.
6. Check audio, seek behavior and user-interface response.

Results and photos will be added after testing.
### Bill of Materials (BOM)
| Component | Description / Specifications | Interface / Protocol |
|---|---|---|
| **Raspberry Pi Pico** | RP2040 microcontroller | Core controller |
| **FM Module** | Si4703 FM Tuner | I2C |
| **Display** | 1.3" OLED (SH1106 driver, 128x64 px) | I2C (SDA/SCL) |
| **Rotary Encoder** | KY-040 (with push-button) | Digital GPIO |


## 7. Project Progress & Checklist

- [ ] **Design & Preparation:** Create a system block diagram, complete the Bill of Materials (BOM), and verify logic levels (3.3V) for safe wiring.
- [ ] **Hardware Bring-up:** Assemble the circuit on a breadboard and perform basic I2C communication tests with the FM module and display.
- [ ] **Software Drivers:** Create or adapt reusable MicroPython classes for the display, rotary encoder, and Si4703 FM tuner.
- [ ] **Core Integration:** Connect the logic so that turning the encoder tunes the receiver and the display shows the selected frequency.
- [ ] **Multitasking:** Ensure a responsive application and button debouncing by using cooperative multitasking (`uasyncio`) or hardware timers.
- [ ] **Extension (Optional):** Implement reading and displaying Radio Data System (RDS) text (e.g., station name) on the screen.
- [ ] **Code Documentation:** Set up and generate technical API documentation for your classes using Sphinx (in the `docs/` folder).
- [ ] **Final Deliverables:** Complete the repository (final README), design the A3 poster, and record a short 1-2 minute demonstration video.
