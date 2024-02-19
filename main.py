#it's cold as balls outside
#let's make a fireplace
import random
import time
import aspose.words as aw
import ctypes
from pynput import keyboard

break_program = False
cap = False


def FirePrinter(size, spacing):
    if size == 0:
        with open('fire.txt', 'a', encoding='utf-8') as f:
            for i in range(10):
                print(file=f)
    if size == 30 or size == 31:
        with open('fire.txt', 'a', encoding='utf-8') as f:
            stones = "ø                           ø"
            print(stones.center(80, " "), file=f)
            stones = "ø                ø"
            print(stones.center(80, " "), file=f)
            stones = "         ø         "
            print(stones.center(80, " "), file=f)

        return
    characters = []
    for i in range(size):
        characters.append(chr(makeAscii()))
    printing = ''.join(str(j) for j in characters)
    if size < 10:
        spacing = random.randint(spacing, 80)
        printing = printing.center(spacing, " ")
        with open('fire.txt', 'a', encoding='utf-8') as f:
            print(printing, file=f)
        return FirePrinter(size + 2, spacing)
    else:
        printing = printing.center(80, " ")
        with open('fire.txt', 'a', encoding='utf-8') as f:
            print(printing, file=f)
        return FirePrinter(size + 4, 70)



def makeAscii():
    while True:
        number = random.randint(32, 255)
        if number != 12:
            return number


if __name__ == "__main__":
    while not cap:
        open('fire.txt', 'w').close()
        FirePrinter(0, 70)
        time.sleep(.01)
        fire = aw.Document("fire.txt")
        fire.save("fire.jpg")
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, r"C:\Users\callu\PycharmProjects\FirePlace\fire.jpg", 0)