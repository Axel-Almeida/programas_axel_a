empty_list=[]
todo_list=['Learn Python List','How to manage List elements']
numbers=[1,3,2,7,9,4]
print(numbers)

colors=['red','green','blue']
print(colors)

cordinates=[[0,0],[100,100],[200,200],]
print(cordinates)

print(numbers[0])
print(numbers[1])
print(numbers[-1])
print(numbers[-2])
numbers[0]=10
print(numbers)

numbers=[1,3,2,7,9,4]
numbers[1]=numbers[1]*10
print(numbers)

numbers=[1,3,2,7,9,4]
numbers[2]/=2
print(numbers)

numbers=[1,3,2,7,9,4]
numbers.append(100)
print(numbers)

numbers=[1,3,2,7,9,4]
numbers.insert(2,100)
print(numbers)

numbers=[1,3,2,7,9,4]
del numbers[0]
print(numbers)

numbers=[1,3,2,7,9,4]
last=numbers.pop()
print(last)
print(numbers)

numbers = [1, 3, 2, 7, 9, 4]
second = numbers.pop(1)
print(second)
print(numbers)

numbers = [1, 3, 2, 7, 9, 4, 9]
numbers.remove(9)
print(numbers)

cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']
result = cities.index('Mumbai')
print(result)

cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']
city = 'Osaka'
if city in cities:
    result = cities.index(city)
    print(f"The {city} has an index of {result}.")
else:
    print(f"{city} doesn't exist in the list.")
