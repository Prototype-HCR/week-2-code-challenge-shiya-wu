import board
import time
from digitalio import DigitalInOut, Direction, Pull
import neopixel

# create a neopixel object
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
pixels.brightness = 0.1
# create a color as a tuple value
ac_orange = 0xfc4600
pixels[9] = ac_orange
pixels[1] = 0x0000ff
time.sleep(5)

# declare a digitial input
button_a = DigitalInOut(board.BUTTON_A)
button_a.switch_to_input(pull=Pull.DOWN)

button_b = DigitalInOut(board.BUTTON_B)
button_b.switch_to_input(pull=Pull.DOWN)

# A variable to track the LED led state
led_astate = True
led_bstate = True
led_abstate = True


while True:
    # gather all input values from sensors
    # print the value of our button_a object
    button_a_read = button_a.value
    #print("button a read is:", button_a_read)

    button_b_read = button_b.value
    #print("button b read is:", button_b_read)


    if button_a_read and button_b_read:
        led_astate = False
        led_bstate = False
        led_abstate = True

    elif button_a_read:
        led_astate = True
        led_bstate = False
        led_abstate = False
    elif button_b_read:
        led_bstate = True
        led_astate = False
        led_abstate = False
    else:
        led_astate = False
        led_bstate = False
        led_abstate = False


    if led_abstate:
        pixels.fill(ac_orange),

    elif led_astate:
        pixels.fill((255,255,0)),

    elif led_bstate:
        pixels.fill((0,255,255)),
    else:
        pixels.fill(0)
