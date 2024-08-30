import random
# List of words to choose from
word_list = ['python', 'java', 'javascript', 'ruby', 'html', 'css']
# Randomly select a word from the list
selected_word = random.choice(word_list)
# Initialize the user's guess
value=True
while(value):
    print("Hello! User this program makes you guess this words")
    print("The following words pyhton, java, javascript, ruby, html, css.")
    print(" ")
    user_guess = input()
    if user_guess==selected_word:
        print("Youve won 1 million pesos venezolanos because you guess right")
    elif user_guess!=selected_word:
        print("you guessed worng try again")
    print(" ")
    print(" ")