import math
pi=3.141592653589793
def volume():
    w=int(input("Enter the width of the tire in mm:"))
    a=int(input("Enter the aspect ratio of the tire:"))
    d=int(input("Enter the diameter of the wheel in inches:"))
    print(" ")
    h=(w*a+2540*d)
    j=a*h
    w2=w*w
    v2=(pi*w2*j)
    v=v2/10000000000
    print(f"The proximate volume of your tire is {v:.2f} liters")
    print(" ")

print("Hello User!, im a program that calculates the volume in liters of a tire."
      "The size of a car tire in the United States is represented with three numbers like this: 205/60R15."
      "The first number is the width of the tire in millimeters."
      "The second number is the aspect ratio."
      "The third number is the diameter in inches of the wheel that the tire fits.")

while(True):
    volume()