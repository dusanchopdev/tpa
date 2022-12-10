import requests
from weather import *
from note import note
print("Hello what would you like to do?(input the number next to the option)")
print("1. Weather \n2. TPA Note\n3. Exit")
term = input()
running = 1
while running == 1:
    match term:
        case "1":
            weather()
        case "2":
            note()
        case "3":
            running = 0
            done()
