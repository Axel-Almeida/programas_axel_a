import time

# Initial list of students
student=["Alice","Bob","Charlie","Diana","Ethan","Fiona","George","Hannah","Isaac","Jasmine"]
def display_students():
    print(f"_____________________________________")
    print(f"Current students:\n")
    for i in student:
        print(i)
    print(f"_____________________________________") 

# Add a new student to the list
def add_student():
    new_nm=input("Enter the new name:")
    student.append(new_nm)
    display_students() 

# Remove a student from the list by name
def remove_student():
    st_nm=input("Select the name of the student you wnat to delete:")
    if st_nm in student:
        student.remove(st_nm)
        display_students()
    else:
        print(f"The name of {st_nm} is not in the student list.")
        display_students()

# remove a student from the end of the list
def pop_student():
    print("This action will remove the last student.")
    if student==[]:
        print("There are no more student to remove or erase left.")
    else:
        remo=student.pop()
        print(f"These is the student name removed {remo}.")
        display_students()

# Update a student's name in the list
def update_student():
    tren=input("Enter the name of the student you want to update:")
    if tren in student:
        troya=input("Enter the new name of the student you want to update:")
        remo=student.index(tren)
        student[remo]=troya
        display_students()
    else:
        print(f"{tren} doesnt exist on the list of students.")
        display_students()

# Menu to manage student operations
def menu():
    while True:
        print("\nMenu:")
        print("1. Add a student")
        print("2. Remove a student")
        print("3. Pop a student")
        print("4. Update a student's name")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice==1:
            add_student()
        elif choice==2:
            remove_student()
        elif choice==3:
            pop_student()
        elif choice==4:
            update_student()
        elif choice==5:
            fern=input("Do you wanna exit (y/n)?")
            if fern=="y":
                print("You are gona exit now, see you next time")
                time.sleep(5)
                break
            else: 
                continue

# Start the program
menu()