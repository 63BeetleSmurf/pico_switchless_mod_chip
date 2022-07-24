from machine import Pin
import utime

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

# Setup base pins
PIN_LED = Pin(25, Pin.OUT, value=1)
PIN_RESET = Pin(16, Pin.OUT)
PIN_RESET_BUTTON = Pin(17, Pin.IN, Pin.PULL_UP)

CURRENT_MODE = 0

# Function to check button is held for specified time
def button_held(button_pin, time, hold_value=0):
    start_time = utime.ticks_ms()
    while utime.ticks_diff(utime.ticks_ms(), start_time) < time:
        if button_pin.value() != hold_value:
            return False
    return True

# Function to set output pins from mode
def set_mode(mode):
    global OUTPUT_PINS
    for index, value in enumerate(mode):
        OUTPUT_PINS[index].value(value)

# Function to flash LED a specified number of times
def flash_led(count):
    for i in range((count + 1) * 2):
        PIN_LED.toggle()
        utime.sleep_ms(200)

# Load last mode if file exists
try:
    with open('mode.dat', 'r') as fh:
        CURRENT_MODE = int(fh.read())
except OSError:
    pass
# Apply mode
set_mode(MODES[CURRENT_MODE])
# Let go of reset button
PIN_RESET.value(1)
# Flash LED to display current mode
utime.sleep_ms(1000)
flash_led(CURRENT_MODE);

# Loop forever
while True:
    # If reset button is pressed
    if PIN_RESET_BUTTON.value() == 0:
        # Debounce
        utime.sleep_ms(20)
        # If button is held for 1 second
        if button_held(PIN_RESET_BUTTON, 1000):
            # Cycle mode while button is being held
            new_mode = CURRENT_MODE
            while PIN_RESET_BUTTON.value() == 0:
                if new_mode < len(MODES) - 1:
                    new_mode += 1
                else:
                    new_mode = 0
                # Flash LED to show current mode
                flash_led(new_mode)
                # Wait 1 second between cycles if button still held
                button_held(PIN_RESET_BUTTON, 1000)
            # Update mode if changed
            if new_mode != CURRENT_MODE:
                CURRENT_MODE = new_mode
                set_mode(MODES[CURRENT_MODE])
                # Save current mode
                with open('mode.dat', 'w') as fh:
                    fh.write(str(CURRENT_MODE))
                # Skip rest of loop if no reset needed
                if not RESET_ON_MODE_CHANGE:
                    continue
        # Reset console
        PIN_RESET.value(0)
        utime.sleep_ms(200)
        PIN_RESET.value(1)
