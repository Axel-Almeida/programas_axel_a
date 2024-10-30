#this program calculates the area of a square
print("Hello Usser! tell the size of your square and triangle, and i will tell you the area")

print("   ")

def area():
    size=int(input("Enter the size of your square:"))
    square=size*size
    print(f"The area of you square is {square} in suare units")

area()

print("   ")

def traingle():
    base=int(input("Tell here your base for triangle area:"))
    longitude=int(input("Tell here your longitude of the triangle:"))
    trisize=(base*longitude)/2
    print(f"here is the size of your triangle {trisize} in square units")

traingle()