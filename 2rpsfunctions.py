import random
word_list=['rock', 'paper', 'scissors']
def intro():
    print("Hello User! Im a program that will gonna play with you rock, paper, scissors.")
    print("If your tired type stacs and you will exit to the window of statistics")
intro()
value=True
SCORE=0
PROGRAM_SCORE=0
TIES=0
def space():
    print("  ")
    print("  ")
def rots():
    global TIES
    print("Its a tie!")
    space()
    TIES+=1
def win():
    global SCORE
    print("You Win")
    space()
    SCORE+=1
def loose():
    global PROGRAM_SCORE
    print("You loose, I Win!!!!!!")
    print(selected+" is what i chose")
    space()
    PROGRAM_SCORE+=1
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
        print(f"Your score is {SCORE}")
        print(f"This is my score {PROGRAM_SCORE}")
        print(f"These are ties or null points and the number is {TIES}")
        space()
        cont_game=input("Do you wanna play more (y/n)?")
        if cont_game=="y":
            continue
        elif cont_game=="n":
            print("It was my pleasure serving you my lord")
            break