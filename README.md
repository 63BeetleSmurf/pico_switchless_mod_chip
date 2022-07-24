# Pico Switchless Mod Chip
A Raspberry Pi Pico based switchless mod chip that can be easily customised for a number of uses.
Using a consoles reset button and LED, any number of modes can be cycled through easily. Each mode will set any number of pins to a specified value.
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
## SEGA Master System Switchless Region Mod ##
```
# Should the console be reset after mode change?
RESET_ON_MODE_CHANGE = True

# List of ouput pins
OUTPUT_PINS = [
    Pin(14, Pin.OUT), # Region
    ]

# List of modes
# - Each entry is a list of vaules to set output pins to
MODES = [
    [0], # NTSC - Region = 0
    [1], # PAL  - Region = 1
    ]
```
## Nintendo 64 N64RGB Switchless De-Blur
```
# Should the console be reset after mode change?
RESET_ON_MODE_CHANGE = False

# List of ouput pins
OUTPUT_PINS = [
    Pin(14, Pin.OUT), # N64RGB De-blur
    ]

# List of modes
# - Each entry is a list of vaules to set output pins to
MODES = [
    [0], # On
    [1], # Off
    ]
```
