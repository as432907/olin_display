import time
import board
import neopixel

# Configuration for NeoPixels
LED_PIN = board.D18         # GPIO pin connected to the NeoPixels
NUM_PIXELS = 8              # Number of NeoPixels
ORDER = neopixel.GRB        # Pixel color order

# Initialize NeoPixels
pixels = neopixel.NeoPixel(LED_PIN, NUM_PIXELS, brightness=1, auto_write=False, pixel_order=ORDER)

def turn_on():
    pixels.fill((255, 255, 255))  # White color
    pixels.show()
    print("turn on")

def turn_off():
    pixels.fill((0, 0, 0))        # Turn off all pixels
    pixels.show()
    print("turn off")

def blink():
    for _ in range(5):            # Blink 5 times
        pixels.fill((255, 0, 0))  # Red color
        pixels.show()
        time.sleep(0.5)
        pixels.fill((0, 0, 0))    # Off
        pixels.show()
        time.sleep(0.5)
    print("blinking")

def color_cycle():
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Red, Green, Blue
    for color in colors:
        pixels.fill(color)
        pixels.show()
        time.sleep(1)
    turn_off()  # Turn off after cycling


