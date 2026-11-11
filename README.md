# DE2-FM-Radio (Raspberry Pi Pico)

[![MicroPython](https://img.shields.io/badge/MicroPython-1.22+-blue.svg)](https://micropython.org/)
[![Platform](https://img.shields.io/badge/Platform-Raspberry%20Pi%20Pico-red.svg)](https://www.raspberrypi.com/products/raspberry-pi-pico/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

FM Radio Receiver embedded systems term project for the **Digital Electronics 2 (DE2)** course at the **Faculty of Electrical Engineering and Communication (FEEC), Brno University of Technology (BUT)**.

---

## 👥 Team Members & Responsibilities

| Name | Role / Focus Area |
|---|---|
| **Lukáš Katrňák** | [README, ] |
| **Aitken Alisher** | [Role] |
| **Murat Assiya** | [Poster, Design] |

---

## 📖 Project Overview

### Problem Statement
[Popsat projekt. Např.: Cílem projektu je vytvořit digitálně laditelný FM přijímač, který nahradí nepřesné analogové ladění a umožní přehledné zobrazení informací uživateli.]

### Solution Summary
The **FM Radio Receiver** is based on the **Raspberry Pi Pico** running MicroPython. It:
1. Tunes FM frequencies using an I2C tuner module (e.g., [Typ modulu]).
2. Displays the current frequency on a [Typ displeje] display.
3. Allows frequency tuning and station selection using a rotary encoder.

---

## 🛠️ Hardware Inventory & Wiring

### Bill of Materials (BOM)
| Component | Description / Specifications | Interface / Protocol |
|---|---|---|
| **Raspberry Pi Pico** | RP2040 microcontroller | Core controller |
| **[Doplnit FM modul]** | [Např. Si4703 FM Tuner] | I2C |
| **[Doplnit displej]** | [Např. Nokia 5110 / OLED SH1106] | [SPI / I2C] |
| **Rotary Encoder** | KY-040 (with push-button) | Digital GPIO |
