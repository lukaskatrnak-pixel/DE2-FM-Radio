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
### Bill of Materials (BOM)
| Component | Description / Specifications | Interface / Protocol |
|---|---|---|
| **Raspberry Pi Pico** | RP2040 microcontroller | Core controller |
| **[Doplnit FM modul]** | [Např. Si4703 FM Tuner] | I2C |
| **Display** | 1.3" OLED (SH1106 driver, 128x64 px) | I2C (SDA/SCL) |
| **Rotary Encoder** | KY-040 (with push-button) | Digital GPIO |
