# License : GPLv2.0
# copyright (c) 2023  Steve Iliopoulos
# Author: Steve Iliopoulos (steveiliop56, @steveiliop56)

import board
import displayio
import terminalio
from adafruit_display_text import label
from adafruit_display_shapes.rect import Rect
from adafruit_display_shapes.circle import Circle
import time
from digitalio import *

# Define the payloads

payload = "payloads/payload.dd"
payload1 = "payloads/payload1.dd"
payload2 = "payloads/payload2.dd"
payload3 = "payloads/payload3.dd"

# Define the colors
BACKGROUND_COLOR = 0x000000
TEXT_COLOR = 0xFFFFFF
CURSOR_COLOR = 0xFFFFFF

# Define the options
OPTIONS = ["Payload 1", "Payload 2", "Payload 3", "Payload 4"]

# Define the button pins
UP_BUTTON_PIN = DigitalInOut(board.SWITCH_UP)
DOWN_BUTTON_PIN = DigitalInOut(board.SWITCH_DOWN)
SELECT_BUTTON_PIN = DigitalInOut(board.SWITCH_PRESS)

# Define the font and font size
FONT = terminalio.FONT
FONT_SIZE = 24

# Define the cursor position
cursor_position = 0

def display_menu():
    # Create the display
    display = board.DISPLAY

    # Create the group that holds all the elements
    group = displayio.Group()

    # Create the background rectangle
    background_rect = Rect(0, 0, display.width, display.height, fill=BACKGROUND_COLOR)
    group.append(background_rect)

    # Create the title label
    title_label = label.Label(FONT, text="Payload Selector", color=TEXT_COLOR, scale=2)
    title_label.anchor_point = (0.5, 0)
    title_label.anchored_position = (display.width // 2, 10)
    group.append(title_label)

    # Create the option labels
    option_labels = []
    for i, option in enumerate(OPTIONS):
        option_label = label.Label(FONT, text=option, color=TEXT_COLOR, scale=1)
        option_label.anchor_point = (0.5, 0.1)
        option_label.anchored_position = (display.width // 2, 60 + i * 45)
        group.append(option_label)
        option_labels.append(option_label)

    # Create the cursor
    cursor_circle = Circle(0, 0, 8, fill=CURSOR_COLOR)
    group.append(cursor_circle)

    # Center the cursor on the first option
    cursor_position = 0
    cursor_circle.x = option_labels[cursor_position].x - 30
    cursor_circle.y = option_labels[cursor_position].y + 10 - 20

    # Add the group to the display
    display.show(group)

    # Loop until a selection is made
    while True:
        # Check for button presses
        if not UP_BUTTON_PIN.value:
            cursor_position = max(cursor_position - 1, 0)
            cursor_circle.x = option_labels[cursor_position].x - 40
            cursor_circle.y = option_labels[cursor_position].y + 10 - 20
            time.sleep(0.2)

        if not DOWN_BUTTON_PIN.value:
            cursor_position = min(cursor_position + 1, len(OPTIONS) - 1)
            cursor_circle.x = option_labels[cursor_position].x - 40
            cursor_circle.y = option_labels[cursor_position].y + 10 - 20
            time.sleep(0.2)

        if not SELECT_BUTTON_PIN.value:
           break 

    # Hide the group from the display
    display.show(None)

    # Return the selected option
    return OPTIONS.index(OPTIONS[cursor_position])

def selectPayload(startup):
    if startup == True:
        return "payloads/payload.dd"
    else:
        option = display_menu()
        if option == 0:
            return "payloads/payload.dd"
        else:
            return f"payloads/payload{str(option)}.dd"
