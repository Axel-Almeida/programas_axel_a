#this program ask the user his first and last name  to be used in these program
value=True
while(value):
    print("Hello User! Nice to meet you, could you tell me your first and last name")
    first=input("Tell here your first name:")
    last=input("Tell here your last name:")
    print('Hello '+last+','+first+'! Your name has '+str(len(first+last))+
          ' letters, and your initials are '+str(first[0])+str(last[0]))
    junk= last [::-1]
    output=""
    for i in (first):
        output = output + i*2
    print(output + ", your name spelled backwards is "+ junk)
    print("")
    print("")
    print("")
    print("")