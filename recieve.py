from microbit import *
import radio
import music
radio.config(group=88)
radio.on()

def logo (label):
    start = running_time()
    display.scroll(label, delay=75)
    while running_time() - start < 3000:
        if pin_logo.is_touched():
            radio.send("+1 Score")
            display.scroll("Correct!", delay=75)
    music.play(music.WAWAWAWAA)
    display.scroll("Wrong")
    
def shake1(Label, gesture):
    start = running_time()
    display.scroll(Label, delay=75)
    while running_time() - start < 3000:
     if accelerometer.was_gesture(gesture):
         radio.send("+1 Score")
         display.scroll("Correct!", delay=75)
    
     music.play(music.WAWAWAWAA)
    display.scroll("Wrong")
    
def wait_for_button(button, label):
    
    start = running_time()
    display.show(label)
    while running_time() - start < 3000:
        if button.is_pressed():
            radio.send("+1 Score")
            display.scroll("Correct!", delay=75)
            return
    music.play(music.WAWAWAWAA)
    display.scroll("Wrong", delay=75)

while True:
    input = radio.receive()
    if input == "A":
        wait_for_button(button_a, "A")
    elif input == "B":
        wait_for_button(button_b, "B")
    elif input == "C":
        shake1("SHAKE!", "shake")
    elif input == "D":
        logo("Logo!")
