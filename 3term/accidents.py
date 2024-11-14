import csv

def load_info(filename):
    accdnt={}
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        next (reader)

        for row in reader:
            year=row[0]
            fatality=row[1]
            injuries=row[2]
            crashes=row[3]
            ftal_crahs=row[4]
            dis_aff_ftal_crahs=row[5]
            ftal_carhs_in_cell=row[6]
            ftal_carhs_in_sped=row[7]
            ftal_carhs_in_alch=row[8]
            ftal_carhs_in_illn=row[9]
            accdnt[year]=[fatality,injuries, crashes, ftal_crahs, dis_aff_ftal_crahs, ftal_carhs_in_cell,ftal_carhs_in_sped,ftal_carhs_in_alch, ftal_carhs_in_illn]

        return accdnt
    
def main():
    filename='accidents.csv'
    info=load_info(filename)

    print()
    print("Search the year. Then it will show the accidents ocurred that year per category. ")
    item=input("Enter the year, the range is from 2010 to 2017:")
    print()

    if item in info:
        print(f"Year: {item}")
        print(f"1. Fatalities.")
        print(f"2. Injuries.")
        print(f"3. Crashes.")
        print(f"4. Fatal Crashes.")
        print(f"5. Distraction Affected Fatal Crashes.")
        print(f"6. Fatal Crashes involving Cell Phone Use.")
        print(f"7. Fatal Crashes involving Excessive Speed.")
        print(f"8. Fatal Crashes whie Driving under the Influence.")
        print(f"9. Fatal Crashes involving Fatigue or Illness.")
        print()
        choice=int(input("Select the number:"))
        if 1 ==choice:
            print(f"Fatalities: {info[item][0]}")
            main()
        elif 2==choice:
            print(f"Injuries: {info[item][1]}")
            main()
        elif 3==choice:
            print(f"Crashes: {info[item][2]}")
            main()
        elif 4==choice:
            print(f"Fatal Crashes: {info[item][3]}")
            main()
        elif 5==choice:
            print(f"Distraction Affected Fatal Crashes: {info[item][4]}")
            main()
        elif 6==choice:
            print(f"Fatal Crashes involving Cell Phone Use: {info[item][5]}")
            main()
        elif 7==choice:
            print(f"Fatal Crashes involving Excessive Speed: {info[item][6]}")
            main()
        elif 8==choice:
            print(f"Fatal Crashes whie Driving under the Influence: {info[item][7]}")
            main()
        elif 5==choice:
            print(f"Fatal Crashes involving Fatigue or Illness: {info[item][8]}")
            main()
    else:
        print(f"{item} is not on the list/is an incorrect number.")
        main()

if __name__ == "__main__":
    main()