###################################################################################
# Names: Avery Grimshaw, Garrett Kitchings, Paul Sakitt                           #
# Description: The file for challenge 3 of the game.                              #
#                                   FINAL PROJECT                                 #
###################################################################################

from Tkinter import *
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
# the LED class; each LED has an assigned pin
class LED(object):
    def __init__(self, pin):
        GPIO.setup(pin, GPIO.OUT)
        self.pin = pin
        
    # allows for an LED to be turned on or off, based on its pin and current state
    def toggle(self):
        if GPIO.input(self.pin):
            GPIO.output(self.pin, GPIO.LOW)
        else:
            GPIO.output(self.pin, GPIO.HIGH)
    # return the pin as an integer so that GPIO commands will play nice with it
    def __str__(self):
        return int(self.pin)

# the Game class
# creates dem buttons and plays dat game
class Game(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        # make the window fill the screen
        master.geometry('{}x{}'.format(800, 480))

    # create the buttons
    # this time, the buttons control different LEDs, sometimes more than 1
    # functions for toggling the proper LEDs are defined at the bottom of the program
    def setupGUI(self):
    
        b1 = Button(self.master, text = "?", width = 12, relief = GROOVE, command = b1toggle)
        b1.grid(row = 1, column = 1)
        
        b2 = Button(self.master, text = "?", width = 12, relief = GROOVE, command = led_5.toggle)
        b2.grid(row = 1, column = 2)

        b3 = Button(self.master, text = "?", width = 12, relief = GROOVE, command = b3toggle)
        b3.grid(row = 1, column = 3)

        b4 = Button(self.master, text = "?", width = 12, relief = GROOVE, command = b4toggle)
        b4.grid(row = 2, column = 1)

        b5 = Button(self.master, text = "?", width = 12, relief = GROOVE, command = b5toggle)
        b5.grid(row = 2, column = 2)

        b6 = Button(self.master, text = "?", width = 12, relief = GROOVE, command = b6toggle)
        b6.grid(row = 2, column = 3)

        b7 = Button(self.master, text = "?", width = 12, relief = GROOVE, command = led_7.toggle)
        b7.grid(row = 3, column = 1)

        b8 = Button(self.master, text = "?", width = 12, relief = GROOVE, command = b8toggle)
        b8.grid(row = 3, column = 2)

        b9 = Button(self.master, text = "?", width = 12, relief = GROOVE, command = b9toggle)
        b9.grid(row = 3, column = 3)

        # put an empty space between rows 3 and 5
        # purely for aesthetic reasons
        emptyspace = Label(self.master)
        emptyspace.grid(row = 4, column = 1, columnspan = 3)

        # turn all the LEDs back off
        resetButton = Button(self.master, text = "Reset", width = 12, relief = GROOVE, command = resetLEDs)
        resetButton.grid(row = 5, column = 1)

        # check if the player is successful
        checkButton = Button(self.master, text = "Check", width = 12, relief = GROOVE, command = checkSolution)
        checkButton.grid(row = 5, column = 2)
        
        # quit the game
        quitButton = Button(self.master, text = "Quit", width = 12, relief = GROOVE, command = quitGame)
        quitButton.grid(row = 5, column = 3)
    
    # play the game (make the GUI)
    def play(self):
        self.setupGUI()
        resetLEDs()

# the function for quitting the game
# used by the "Quit" button
def quitGame():
    resetLEDs()
    GPIO.cleanup()
    quit()
    
# the function for resetting the LEDs in case the user wants to start over in a level
# used by the "Reset" button
def resetLEDs():
    for led in leds:
        GPIO.output(led, GPIO.LOW)
        led += 1

# check if every light is turned on (challenge is complete)
# used by the "Check" button
def checkSolution():
    # if all the lights are on, move to next challenge
    if GPIO.input(led_1.pin and led_2.pin and led_3.pin and led_4.pin and led_5.pin and led_6.pin and led_7.pin and led_8.pin and led_9.pin):
        from Challenge5 import challenge
        window.title("Level 5")
        resetLEDs()
        challenge()

# functions for toggling the proper LEDs when buttons are pressed
# button 1 toggles 3, 6, 7
def b1toggle():
    led_3.toggle()
    led_6.toggle()
    led_7.toggle()

# button 3 toggles all
def b3toggle():
    led_1.toggle()
    led_2.toggle()
    led_3.toggle()
    led_4.toggle()
    led_5.toggle()
    led_6.toggle()
    led_7.toggle()
    led_8.toggle()
    led_9.toggle()

# button 4 toggles 2, 4, 9
def b4toggle():
    led_2.toggle()
    led_4.toggle()
    led_9.toggle()

# button 5 toggles 1, 3, 5, 6, 7, 8
def b5toggle():
    led_1.toggle()
    led_3.toggle()
    led_5.toggle()
    led_6.toggle()
    led_7.toggle()
    led_8.toggle()

# button 6 toggles 4, 6, 8
def b6toggle():
    led_4.toggle()
    led_6.toggle()
    led_8.toggle()

# button 8 toggles 1, 2, 7, 9
def b8toggle():
    led_1.toggle()
    led_2.toggle()
    led_7.toggle()
    led_9.toggle()

# button 9 toggles 4, 5
def b9toggle():
    led_4.toggle()
    led_5.toggle()
    
# instantiate the LEDs and give them meaningful names
led_1 = LED(5)              # the top left LED
led_2 = LED(19)             # the top center LED
led_3 = LED(6)              # the top right LED
led_4 = LED(26)             # the middle left LED
led_5 = LED(13)             # the middle center LED
led_6 = LED(12)             # the middle right LED
led_7 = LED(21)             # the bottom left LED
led_8 = LED(16)             # the bottom center LED
led_9 = LED(20)             # the bottom right LED
# make a list of the LEDs
leds = [led_1.pin, led_2.pin, led_3.pin, led_4.pin, led_5.pin, led_6.pin, led_7.pin, led_8.pin, led_9.pin]

window = Tk()
window.title("Level 4")

game = Game(window)
game.play()

window.mainloop()
