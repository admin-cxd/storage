from microbit import *
import radio

radio.config(group=88)
radio.on()

def shake1(Label, gesture):
    display.scroll(Label, delay=125)
    start = running_time()
    while running_time() - start < 5000:
     if accelerometer.was_gesture(gesture):
         display.scroll("Correct", delay=125)
    
def wait_for_button(button, label):
    display.show(label)
    start = running_time()
    
    while running_time() - start < 5000:
        if button.is_pressed():
            display.scroll("Correct!", delay=125)
            return
    display.scroll("Wrong", delay=125)

while True:
    input = radio.receive()
    if input == "A":
        wait_for_button(button_a, "A")
    elif input == "B":
        wait_for_button(button_b, "B")
    elif input == "C":
        shake1("SHAKE!", "shake")
