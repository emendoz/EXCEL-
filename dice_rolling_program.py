# Dice Rolling Program
import random
print("This is a dice rolling program")
print("Press enter to roll")
input()
number = random.randint(1,6)
if number == 1:
    print("[-------------]")
    print("[-           -]")
    print("[-     O     -]")
    print("[-           -]")
    print("[-------------]")
if number == 2:
    print("[-------------]")
    print("[-  O        -]")
    print("[-           -]")
    print("[-        O  -]")
    print("[-------------]")
if number == 3:
    print("[-------------]")
    print("[-  O        -]")
    print("[-     O     -]")
    print("[-        O  -]")
    print("[-------------]")
if number == 4:
    print("[-------------]")
    print("[-  O     O  -]")
    print("[-           -]")
    print("[-  O     O  -]")
    print("[-------------]")
if number == 5:
    print("[-------------]")
    print("[-  O     O  -]")
    print("[-     O     -]")
    print("[-  O     O  -]")
    print("[-------------]")
if number == 6:
    print("[-------------]")
    print("[-  O     O  -]")
    print("[-  O     O  -]")
    print("[-  O     O  -]")
    print("[-------------]")
    
