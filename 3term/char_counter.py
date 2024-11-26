import tkinter

def count_occurrences():
    user_input=entry.get().lower().replace(" ", "")
    char_count={}
    for char in user_input:
        current_count=char_count.get(char, 0)
        char_count[char]=current_count +1
    result.config(text=char_count)

root=tkinter.Tk()
root.geometry("400x400")
root.title("Character Counter")

instructions=tkinter.Label(root, text="Enter  your text:")
instructions.pack(pady=10)

entry=tkinter.Entry(root)
entry.pack(pady=10)

bttn=tkinter.Button(root, text="Count Occurances", command=count_occurrences)
bttn.pack(pady=10)

result=tkinter.Label(root, text="")
result.pack(pady=10)

root.mainloop()