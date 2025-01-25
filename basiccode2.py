import board
import neopixel
import time
import random
import signal

# Configure the NeoPixel strips
PIN1 = board.D18  # GPIO pin for pixels 1-50
PIN2 = board.D21  # GPIO pin for pixels 51-100
NUM_PIXELS = 100
BRIGHTNESS = 1

pixels1 = neopixel.NeoPixel(PIN1, 50, brightness=BRIGHTNESS, auto_write=False)
pixels2 = neopixel.NeoPixel(PIN2, 50, brightness=BRIGHTNESS, auto_write=False)

def set_pixel(index, color):
    if index > 0:
        if index <= 50: #added '=' sign to count 50
            pixels1[index - 1] = color
        else:
            pixels2[index - 51] = color #changed 50 to 51 as second led strips starts from 0 indicaing 51

def show():
    pixels1.show()
    pixels2.show()

def clear():
    pixels1.fill((0, 0, 0))
    pixels2.fill((0, 0, 0))
    show()

# Updated time_display function with gradient effect and exit with CTRL+C
def time_display():
    print("Starting time... Press CTRL+C to exit to main menu.")
    #current_time = time.localtime()
    #hours = current_time.tm_hour % 12
    #minutes = current_time.tm_min
    #seconds = current_time.tm_sec
    #set_pixel(hours, (255, 0, 0))  # Red for hours
    #set_pixel(minutes, (0, 255, 0))  # Green for minutes
    #prev_hours,prev_minutes,prev_seconds =-1,-1,-1
    try:
        while True:
            current_time = time.localtime()
            hours = current_time.tm_hour % 12
            minutes = current_time.tm_min
            seconds = current_time.tm_sec
            '''
            if (hours != prev_hours):
                set_pixel(hours, (255, 0, 0))
                prev_hours=hours
            if (minutes != prev_minutes):
                set_pixel(minutes, (0, 255, 0))
                prev_minutes=minutes
            if (seconds !=prev_seconds):
                set_pixel(seconds, (0, 255, 0))
                prev_seconds=seconds
           '''

		 # Display hours and minutes
            set_pixel(hours, (255, 0, 0))  # Red for hours
            set_pixel(minutes, (0, 255, 0))  # Green for minutes
            set_pixel(seconds, (0, 0, 255))  # Blue for seconds
            #seconds = current_time.tm_sec

            # Gradient effect when hours and minutes overlap
            if hours == minutes:
                for i in range(256):
                    set_pixel(hours, (255 - i, i, 0))  # Gradient from red to green
                    show()
                    time.sleep(0.01)

            show()
            time.sleep(1)
            clear()

    except KeyboardInterrupt:
        print("\nExiting time display. Returning to main menu.")
        clear()

# Glitter function (original)
def glitter():
    print("Glitter function starting: flashing white on and off.")
    for i in range(NUM_PIXELS):
        set_pixel(i, (255, 255, 255))  # White
        show()
        time.sleep(0.1)
        set_pixel(i, (0, 0, 0))  # Off
    show()

# All LEDs on function (original)
def all_on():
    print("All LEDs on - maximum brightness.")
    for i in range(NUM_PIXELS):
        set_pixel(i, (255, 255, 255))  # White
    show()

# New random NeoPixel color function with continuous blit for 10 seconds
def random_pixel():
    print("Random pixel function starting for 10 seconds.")
    start_time = time.time()
    
    while time.time() - start_time < 10:  # Run for 10 seconds
        index = random.randint(0, NUM_PIXELS - 1)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        set_pixel(index, color)
        show()
        time.sleep(0.1)  # Adjust speed of blit
        clear()

    print("Random pixel function ended.")

# Race function with alternating strips
def alternating_race():
    print("Starting alternating race between two strips.")
    for i in range(50):
        set_pixel(i +1, (255, 0, 0))  # Red on strip 1
        set_pixel(i + 51, (0, 0, 255))  # Blue on strip 2
        show()
        time.sleep(0.1)
        clear()

# Main loop
while True:
    choice = input("Enter mode (time/glitter/all_on/random_pixel/race/exit): ")
    if choice == "time":
        time_display()
    elif choice == "glitter":
        glitter()
    elif choice == "all_on":
        all_on()
    elif choice == "random_pixel":
        random_pixel()
    elif choice == "race":
        alternating_race()
    elif choice == "exit":
        clear()
        break
    else:
        print("Invalid choice. Try again.")
