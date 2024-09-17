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
def stars(mess):
    print(f"**********{mess}*****")
def space():
    print("  ")
    print("  ")
def rots():
    global TIES
    t="Its a tie!"
    stars(t)
    space()
    TIES+=1
def win():
    global SCORE
    t="You Win"
    stars(t)
    space()
    SCORE+=1
def loose():
    global PROGRAM_SCORE
    t="You loose, I Win!!!!!!"
    stars(t)
    z=selected+" is what i chose"
    stars(z)
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
        stzs="Here are the statistics"
        stars(stzs)
        space()
        print(f"Your score is {SCORE}")
        print(f"This is my score {PROGRAM_SCORE}")
        print(f"These are ties or null points and the number is {TIES}")
        space()
        cont_game=input("Do you wanna play more (y/n)?")
        if cont_game=="y":
            continue
        elif cont_game=="n":
            do="It was my pleasure serving you my lord"
            stars(do)
            space()
            break