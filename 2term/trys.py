student=["Alice","Bob","Charlie","Diana","Ethan","Fiona","George","Hannah","Isaac","Jasmine"]
def display_students():
    print(f"_____________________________________")
    print(f"Current students:\n")
    for i in student:
        stnm(i)
    print(f"_____________________________________") 

def stnm(i):
    x=len(student)
    
    for c in range(1,x+1):
        kron=str(c)+". "+i
    
    print(kron)

display_students()
