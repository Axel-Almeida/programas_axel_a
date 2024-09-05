#Ask the user to make a choice (rock/paper/scissors). Have the computer make a random choice. Tell the user what the computer's choice was, and who won
import random
word_list=['rock', 'paper', 'scissors']
print("Hello User! Im a program that will gonna play with you rock, paper, scissors.")
print("If your tired type stacs and you will exit to the window of statistics")
value=True
score=0
program_score=0
ties=0
while(value):
    selected = random.choice(word_list)
    choice=input("Enter your choice in lowercase:")
    if selected == choice:
        print("Its a tie!")
        print("  ")
        print("  ")
        ties+=1
    elif choice == 'rock':
        if selected == 'paper':
            print("You loose, I Win!!!!!!")
            print(selected+" is what i chose")
            print("  ")
            print("  ")
            program_score+=1
        else:
            print("You Win")
            print("  ")
            print("  ")
            score+=1
    elif choice == 'paper':
        if selected == 'scissors':
            print("You loose, I Win!!!!!!")
            print(selected+" is what i chose")
            print("  ")
            print("  ")
            program_score+=1
        else:
            print("You Win")
            print("  ")
            print("  ")
            score+=1
    elif choice == 'scissors':
        if selected == 'rock':
            print("You loose, I Win!!!!!!")
            print(selected+" is what i chose")
            print("  ")
            print("  ")
            program_score+=1
        else:
            print("You Win")
            print("  ")
            print("  ")
            score+=1
    elif choice == "stacs":
        print("Here are the statistics")
        print("   ")
        print(f"Your score is {score}")
        print(f"This is my score {program_score}")
        print(f"These are ties or null points and the number is {ties}")
        cont_game=input("Do you wanna play more (y/n)?")
        if cont_game=="y":
            continue
        else:
            print("It was my pleasure serving you my lord")
            print("   ")
            print("   ")
            break