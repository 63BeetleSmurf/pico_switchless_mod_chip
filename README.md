# Pico Switchless Mod Chip
This is a Raspberry Pi Pico based switchless mod chip that can be easily customised to suite a number of uses.

Using the reset button and LED, any number of modes can be cycled through easily. Each mode will set any number of pins to a specified value.

Eamples below show how to setup the code to suite different functions for different consoles.
# How It Works
## Startup
1. Console is switched on
2. Pico keeps reset button held
3. Pico applies previously set mode
4. Pico lets go of reset button so console can boot
5. Pico flashes LED to show what mode has been applied
## Changing Mode
1. Hold reset button for 1 second
2. Pico will start to cycle though each mod flashing the LED
3. Let go of the reset button and the pico will apply the mode and reset the console if needed
## Normal Reset
Pressing the reset button normally will reset the console as long as you let go of it within 1 second
## LED Flashes
The number of times the LED flashes for a mode is that modes position in the modes list.

In the Mega Drive example below, 1 = US, 2 = JP, 3 = EU.
# Examples
## SEGA Mega Drive Switchless Region Mod
```
# Should the console be reset after mode change?
RESET_ON_MODE_CHANGE = True

# List of ouput pins
OUTPUT_PINS = [
    Pin(14, Pin.OUT), # Language
    Pin(15, Pin.OUT), # Region
    ]

# List of modes
# - Each entry is a list of vaules to set output pins to
MODES = [
    [1, 1], # US - Language = 1, Region = 1
    [0, 1], # JP - Language = 0, Region = 1
    [1, 0], # EU - Language = 1, Region = 0
    ]
```
## SEGA Master System Switchless Region Mod / Nintendo 64 N64RGB Switchless De-Blur
```
# Should the console be reset after mode change?
RESET_ON_MODE_CHANGE = False

# List of ouput pins
OUTPUT_PINS = [
    Pin(14, Pin.OUT), # Region / N64RGB De-blur
    ]

# List of modes
# - Each entry is a list of vaules to set output pins to
MODES = [
    [0], # NTSC - Region = 0 / De-blur On
    [1], # PAL  - Region = 1 / De-blur Off 
    ]
```
