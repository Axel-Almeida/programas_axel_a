import random
word_list=['rock', 'paper', 'scissors']
def intro():
    print("Hello User! Im a program that will gonna play with you rock, paper, scissors.")
    print("If your tired type stacs and you will exit to the window of statistics")
intro()
value=True
score=0
program_score=0
ties=0
def space():
    print("  ")
    print("  ")
def rots():
    print("Its a tie!")
    space()
    ties+=1
def win():
    print("You Win")
    space()
    score+=1
def loose():
    print("You loose, I Win!!!!!!")
    print(selected+" is what i chose")
    space()
    program_score+=1
def konga():
        if selected == 'paper':
            loose()
        else:
             win     
def troya():
    if selected == 'rock':
        loose()
    else:
        win()
def makemake():
    if selected == 'scissors':
        loose()
    else:
        win()
while(value):
    selected = random.choice(word_list)
    choice=input("Enter your choice in lowercase:")
    if selected==choice:
        rots()
    elif choice == 'rock':
        konga()
    elif choice== 'paper':
        makemake()
    elif choice == 'scissors':
        troya()
    elif choice == "stacs":
        print("Here are the statistics")
        space()
        print(f"Your score is {score}")
        print(f"This is my score {program_score}")
        print(f"These are ties or null points and the number is {ties}")
        cont_game=input("Do you wanna play more (y/n)?")
        if cont_game=="y"or "yes":
            continue
        else:
            print("It was my pleasure serving you my lord")
            space()
            break