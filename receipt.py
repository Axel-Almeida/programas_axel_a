import csv
from datetime import datetime
current_date_and_time=datetime.now()
import random as rand

def read_prod(filename):
    products={}
    with open(filename, 'r', newline='') as csv_file:
        reader=csv.reader(csv_file)
        next (reader)

        for row in reader:
            key=row[0]
            prod_desc=row[1]
            prod_price=row[2]
            products[key]=[prod_desc, prod_price]

        return products

def read_order(filename):
    products_ids=[]
    quantities=[]
    with open(filename, 'rt') as csv_request:
        reader=csv.reader(csv_request)
        next(reader)

        for row in reader:
            products_ids.append(row[0])
            quantities.append(row[1])

    return products_ids,quantities

def sub_tax(subtotal):
    print(f"The subtotal is about ${subtotal:.2f}, but is aplying the 6% tax.")
    total=subtotal*1.06
    print(f"Here is your total of ${total:.2f}, how will you pay it")

def payment_tax(subtotal):
    num=[1,2]
    choice=int(input("Enter 1 for credit/debit card or enter 2 for cash: "))
    if choice==1:
        enter=input("Swipe or enter your credit information to pay: ")
        rnd=rand.choice(num)
        if rnd==1:
            print(f"Your information {enter} is now being using at shein for paying child labor.")
            print(f"Thanks for shopping on Mini Super El Chapo." 
                    "Have a nice day!")
        elif rnd==2:
            print(f"Your card is have been declined."
                    "If you cant pay your groceries go to other place.")
    elif choice==2:
        total=subtotal*1.06
        pay=int(input("Enter the amount of cash you wanna pay:"))
        t2=pay-total
        if t2 < 0:
            print(f"Youre short of payment."
                  "Please enter more cash.")
        else:
            print(f"Here is your change the amount is ${t2:.2f}")
            print(f"Thanks for shopping on Mini Super El Chapo."
                    "Have a nice day!")

def capitalize(string):
    return string.capitalize()

def cont_itms(ttitms):
    print(f"The numebr of items are {ttitms}")

def main():
    products=read_prod("3term\products.csv")
    products_ids=read_order("3term/request.csv")[0]
    quantities=read_order("3term/request.csv")[1]
    
    print()
    print("Mini Super El Chapo")
    print()
    print(f"Current Date and Time: {current_date_and_time}")
    print()

    subtotal=0
    ttitms=0
    print("Items on check:")
    for item in range(len(products_ids)):
        product=products[products_ids[item]]
        name=product[0]
        price=float(product[1])
        quantity=quantities[item]
        print(f"{capitalize(name)}: {quantity} @ {price}")
        subtotal= subtotal+(float(quantity)*float(price))
        ttitms+=int(quantity)
    print()
    cont_itms(ttitms)
    print()
    sub_tax(subtotal)
    print()
    payment_tax(subtotal)
    
if __name__ == "__main__":
    main()