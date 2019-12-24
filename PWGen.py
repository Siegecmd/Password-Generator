import string
import random
import sys
import os

# PW Gen.
# Need to change rules for enforcing Capital and special char
from pip._vendor.distlib.compat import raw_input

def generatePassword(num):
    password = ''
    for n in range(num):
        x = random.randint(0, 36)
        password += string.printable[x]
    return password

print("Your password is:")
print(generatePassword(12))

#Rerun the script?
def restart():
    python = sys.executable
    os.execl(python, python, *sys.argv)

if __name__ == "__main__":
    answer = raw_input("Generate another? (y/n)")
    if answer.lower().strip() in "y yes".split():
        restart()
        if answer.lower().strip() in "n no".split():
            exit()

