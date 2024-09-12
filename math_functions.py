import math
import time
import random
#this porgram calculates the factorial of these numbers 6/11/15/22
print("these program select a number in order to make it factorial")
print("the chosen numbers are 6,11,15,22")
print(" ")
time.sleep(2)
select=[6, 11, 15, 22]
randsc=random.choice(select)
x=randsc
def seld1(x):
    ed=1
    for i in range(1,x+1):
        ed*=i
    print(f"these is the result of {x} is {ed}")
    print(f"this is to check if the result above is corect, "+ str(math.factorial(x)))
    time.sleep(1)
    print(" ")
for elem in select:
    seld1(elem)
print("now your time select a number")
choice=int(input("enter your number:"))
y=choice
def seld2(y):
    ed=1
    for i in range(1,y+1):
        ed*=i
    print(f"these is the result of {y} is {ed}")
    print(f"this is to check if the result above is correct, "+str(math.factorial(y)))
    print(" ")
seld2(y)
time.sleep(3)
print("also these program returns the division remainders")
print("the chosen numbers are 3/2, 21/4, 131/19, 81/9")
print(" ")
time.sleep(2)
a=[3,21,131,81]
b=[2,4,19,9]
def reaminder(a,b):
    return(a-((a//b)*b))
def list(list1,list2):
    n=0
    for i in a:
        print(f"the reminder of {a[n]}/{b[n]} is "+str(reaminder(i,b[n])))
        n +=1
list(a,b)
print(" ")
print(" ")
def reaminder2(a,b):
    return(a%b)
def list2(list1,list2):
    n=0
    for i in a:
        print(f"these is to check above if its correct the reminder of {a[n]}/{b[n]} is "+str(reaminder(i,b[n])))
        n +=1
list2(a,b)
print(" ")
time.sleep(3)
print("now your time to use it")
z=int(input("select your number:"))
z2=int(input("select your second number:"))
def reminder3(z,z2):
    return(z%z2)
print(f"the reminder of {z}/{z2} is "+str(reminder3(z,z2)))