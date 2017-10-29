###################################################################################
# Names: Avery Grimshaw, Garrett Kitchings, Paul Sakitt                           #
# Description: A puzzle that makes use of Tkinter buttons to control LEDs. The    #
# game has five levels of increasing difficulty, and makes use of various gates   #
# as a part of the challenge.                                                     #
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

    # each button variable corresponds to the LED it controls
    # b1 controls LED 1, b2 controls LED 2, etc.
    def setupGUI(self):
        b1 = Button(self.master, text = "LED 1", width = 12, relief = GROOVE, command = led_1.toggle)
        b1.grid(row = 1, column = 1)
        
        b2 = Button(self.master, text = "LED 2", width = 12, relief = GROOVE, command = led_2.toggle)
        b2.grid(row = 1, column = 2)

        b3 = Button(self.master, text = "LED 3", width = 12, relief = GROOVE, command = led_3.toggle)
        b3.grid(row = 1, column = 3)

        b4 = Button(self.master, text = "LED 4", width = 12, relief = GROOVE, command = led_4.toggle)
        b4.grid(row = 2, column = 1)

        b5 = Button(self.master, text = "LED 5", width = 12, relief = GROOVE, command = led_5.toggle)
        b5.grid(row = 2, column = 2)

        b6 = Button(self.master, text = "LED 6", width = 12, relief = GROOVE, command = led_6.toggle)
        b6.grid(row = 2, column = 3)

        b7 = Button(self.master, text = "LED 7", width = 12, relief = GROOVE, command = led_7.toggle)
        b7.grid(row = 3, column = 1)

        b8 = Button(self.master, text = "LED 8", width = 12, relief = GROOVE, command = led_8.toggle)
        b8.grid(row = 3, column = 2)

        b9 = Button(self.master, text = "LED 9", width = 12, relief = GROOVE, command = led_9.toggle)
        b9.grid(row = 3, column = 3)

        # put an empty space between rows 3 and 5
        # purely for aesthetic reasons
        emptyspace = Label(self.master)
        emptyspace.grid(row = 4, column = 1, columnspan = 3)

        # turn all the LEDs back off
        resetButton = Button(self.master, text = "Reset", width = 12, relief = GROOVE, command = resetLEDs)
        resetButton.grid(row = 5, column = 1)

        # quit the game
        quitButton = Button(self.master, text = "Quit", width = 12, relief = GROOVE, command = quitGame)
        quitButton.grid(row = 5, column = 3)

        # show the player the current difficulty level
        level = Label(self.master, text = "Level: {}".format(currentLevel))
        level.grid(row = 6, column = 2)
        
    # play the game (make the GUI)
    def play(self):
        self.setupGUI()

# the function for quitting the game
# used by the "Quit" button
def quitGame():
    quit()
    GPIO.cleanup()

# the function for resetting the LEDs in case the user wants to start over in a level
# used by the "Reset" button
def resetLEDs():
    for led in leds:
        GPIO.output(led, GPIO.LOW)
        led += 1
        
currentLevel = 1
# instantiate the LEDs and give them meaningful names
led_1 = LED(5)              # the top left LED
led_2 = LED(6)              # the top center LED
led_3 = LED(13)             # the top right LED
led_4 = LED(19)             # the middle left LED
led_5 = LED(26)             # the middle center LED
led_6 = LED(12)             # the middle right LED
led_7 = LED(21)             # the bottom left LED
led_8 = LED(16)             # the bottom center LED
led_9 = LED(20)             # the bottom right LED
# make a list of the LEDs
leds = [led_1.pin, led_2.pin, led_3.pin, led_4.pin, led_5.pin, led_6.pin, led_7.pin, led_8.pin, led_9.pin]

window = Tk()
window.title("The Game Has No Name")

game = Game(window)
game.play()

window.mainloop()
