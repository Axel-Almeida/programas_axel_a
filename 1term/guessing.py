#this progrma makes the user guess any number and could go out the guessing action
import random
value=True
while(value):
    print("Hello User!, guess any number between 1-100")
    print("Please DO NOT USE LETTERS youre gonna break me")
    print("     ")
    num=input("Enter 0 if you wnat to quit:")
    my_num=random.randint(1,100)
    if int(num)==my_num:
        print("You´ve guessed correctly, now youve won 1 million pesos venezolanos")
    elif 0<int(num)<my_num:
        print("Your guess is so low, you need to higher it up, you can do it")
    elif int(num)>my_num>0:
        print("Your guess is so high; you need to lower it up, you can do it")
    elif int(num)<=101 and int(num)<0:
        print("Nah, you little devil, youre not fooling me again, type something else")
    elif int(num)==0:
        print("Goodbye sir its was my pleasure serving you today")
        break
    print("          ")
    print("          ")
    print("          ")
    print("          ")
    print("          ")
    print("          ")
    print("          ")
    print("          ")
    print("          ")
    print("          ")
