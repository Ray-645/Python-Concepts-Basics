#   Import OS and Delayed Actions
 #  Raymon Shields
  # 7/03/2023

# impost os and import time | This is used for importing different libraries "OS and Time" being one of the pre-installed one.
# time.sleep ()             | This delays the next set of instruction for what however long you want. Put the amount of seconds in ().
# os.system('cls')          | This just clears the screen to declutter the terminal

import os
import time

print("Welcome to the text demo.")

print()

print("Please wait.")
time.sleep (2)

print("..")
time.sleep(1)

print("...")
time.sleep(1)

print()

print("Thanks for waiting.")
time.sleep(1)
print()

print("This is an example of the time.sleep function. This is used to delay certain set instruction.")
print()

print("This ends this demo, on to another. Press ENTER to continue")
input()

os.system('cls')
time.sleep(3)

print("Well, this is the os.system('cls') or clear screen command that clears the screen. Press ENTER to continue.")
input()

print("This concludes this demo. Press Enter to exit the program.")
input()

