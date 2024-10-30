#this program ask the user to pu t an integer and tells if its a prime number
value=True
while(value):
    print("Hello user, please tell a number and i will tell you if its a prime number")
    print("hint: a whole number greater than 1 that cannot be exactly divided by any whole number other than itself and 1.")
    user_num=int(input())
    if user_num > 1:
        for i in range(2,user_num):
            if (user_num/i) ==0:
                print("thats is not a prime number try again")
                break
        else:
            print("thats a prime number")
    else:
        print("is not a prime number")

    print("              ")
    print("              ")
    print("              ")
    print("              ")
    print("              ")
