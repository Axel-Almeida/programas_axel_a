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
while(value):
    selected = random.choice(word_list)
    choice=input("Enter your choice in lowercase:")
    def rots():
        print("Its a tie!")
        print("  ")
        print("  ")
        ties+=1
    def win():
            print("You Win")
            print("  ")
            print("  ")
            score+=1
    def loose():
        print("You loose, I Win!!!!!!")
        print(selected+" is what i chose")
        print("  ")
        print("  ")
        program_score+=1
    def stonks():
        print("Here are the statistics")
        print("   ")
        print(f"Your score is {score}")
        print(f"This is my score {program_score}")
        print(f"These are ties or null points and the number is {ties}")
        cont_game=input("Do you wanna play more (y/n)?")
        if cont_game=="y"or "yes":
            continue
        else:
            print("It was my pleasure serving you my lord")
            print("   ")
            print("   ")
            break
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
    if selected==choice:
        rots()
    elif choice == 'rock':
        konga()
    elif choice== 'paper':
        makemake()
    elif choice == 'scissors':
        troya()
    elif choice == "stacs":
        stonks