from datetime import datetime
current_date_and_time=datetime.now()
day_of_week=current_date_and_time.weekday()

def sub_disc():
    subtotal=custal*.9
    total=subtotal*1.06
    print(f"Here is your total of ${total:.2f}, how will you pay it")

def payment_disc():
    choice=int(input("Enter 1 for credit/card or enter 2 for cash."))
    if choice==1:
        enter=input("Swipe or enter your credit information to pay.")
        print(f"Your information {enter} is now being using at shein for paying child labor.")
        print("Thanks for shopping on walmart." 
              "Have a nice day!")
    elif choice==2:
        total=custal*1.06
        rok=int(input("Enter the amount of cash you wanna pay:"))
        t2=rok-total
        print(f"Here is your change the amount is ${t2:.2f}"
                "Thanks for shopping on walmart." 
                "Have a nice day!")

def sub_tax():
    total=custal*1.06
    print(f"Here is your total of ${total:.2f}, how will you pay it")

def payment_tax():
    choice=int(input("Enter 1 for credit/debit card or enter 2 for cash: "))
    if choice==1:
        enter=input("Swipe or enter your credit information to pay: ")
        print(f"Your information {enter} is now being using at shein for paying child labor.")
        print("Thanks for shopping on walmart." 
                "Have a nice day!")
    elif choice==2:
        total=custal*1.06
        pay=int(input("Enter the amount of cash you wanna pay:"))
        t2=pay-total
        print(f"Here is your change the amount is ${t2:.2f}"
                "Thanks for shopping on walmart."
                "Have a nice day!")

def sub_less():
    print("Helo, Customer before you pay."
            "Today we have a discount of 10 percent less in shopping more than $50 dollars.")

value=True
while(value):
    custal=float(input("Enter your subtotal in shopping experience:"))
    if custal>49:
        if day_of_week == 1 or day_of_week == 2:
            sub_disc()
            payment_disc()
        else:
            sub_tax()
            payment_tax()
    elif custal<50:
        if day_of_week == 1 or day_of_week == 2:
            sub_less()
            fg=int(input("Doy you want to continue shopping or iniciate form of payment? (1/2):"))
            if fg==1:
                continue
            elif fg==2:
                sub_tax()
                payment_tax()
        else:
            sub_tax
            payment_tax