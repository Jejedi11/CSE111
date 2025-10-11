"""
Author: James Michelson
Purpose: To calculate the volume of a tire.
"""
import math
from datetime import datetime
w = float(input("Enter the width of the tire in mm (ex 205): "))
a = float(input("Enter the aspect ratio of the tire (ex 60): "))
d = float(input("Enter the diameter of the wheel in inches (ex 15): "))
pi = math.pi

volume = (pi* w * w * a * (w * a + 2540 * d)) / (10000000000)

date = datetime.now()
print(f"The approximate volume is {volume:.2f} liters.")
with open("volume.txt", mode="at") as volume_file:
    print(f"{date:%Y/%m/%d}, {w}, {a}, {d}, {volume:.2f}", file=volume_file)