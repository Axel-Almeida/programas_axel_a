import json

def read_store(filename):
    students={}
    with open(filename, "r") as file:
        reader=json.load(file)
        for student_id, student_info in reader.items():
            student = student_info[0]
            name=student['name']
            grade=student['grade']
            group=student['group']
            students[student_id]=[name,grade,group]
    return students
def main():
    filename='3term/data.json'
    gor=read_store(filename)
    
    print()
    print("Student display list.")
    print()

    for item in gor:
        print(f"Number ID: {item}")
        print(f"Name: {gor[item][0]}")
        print(f"Grade: {gor[item][1]}")
        print(f"Group: {gor[item][2]}")
        print()
        

main()
