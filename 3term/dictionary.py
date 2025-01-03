import csv

def local_contacts(filename):
    contacts={}
    with open(filename,'r', newline='') as file:
        reader= csv.reader(file)
        for row in reader:
            first_name=row[0]
            last_name=row[1]
            phone_number=row[2]
            emailaddres=row[3]
            contacts[first_name]= [last_name, phone_number, emailaddres]
    return contacts

def display_contact_info(last_name, contact_info):
    if contact_info:
        print("Contact Information:\n")
        print(f"Full Name: {contact_info[0]} {last_name}")
        print(f"Phone NUmber: {contact_info[1]}")
        print(f"Eamil Addres: {contact_info[2]}")
    else:
        print("No contact information for this last name.")

def main():
    filename='3term\CSV.csv'

    contacts=local_contacts(filename)

    last_name= input("Please enter the last name to look up:").strip()
    contact_info= contacts.get(last_name)

    display_contact_info(last_name, contact_info)

main()