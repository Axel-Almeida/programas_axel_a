#this program guesses a number between 1 and 10
value=True
while(value):
    print("Hello, guess a number between 1-10")
    number=input()
    if int(number)==3:
        print("You got me, youve guessed, try again")
    elif int(number)<3:
        print("Try again, youre not smart enough")
    elif int(number)<10:
        print("Try again, I recomend you going again to elementary school again")
    elif int(number)<=11:
        print("Nah, you will not fool me, you little devil, try again")
