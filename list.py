""" #this are examples from the websites in the assigment
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
print(result) """

cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']
city = 'New York'
if city in cities:
    result = cities.index(city)
    print(f"The {city} has an index of {result}.")
else:
    print(f"{city} doesn't exist in the list.")

""" #class work about lists begins now
list1=[]

#homogenous list
integers=[1,2,3,8,33]
animals=["dog","cat","goat"]
names=["John","Felix","Jose"]
floats=[2.5,3.8,15.78,98.124]

#heterogenous list
numbers_animals_numbers=[2, "cat",33.3, "Pablo"]
list_lists=[[1,2,3],["cats","horses","dolphin"]]

#how access a element in a list
list=[3,22,30,5.3,20]
print(list[2])
print(list[0])
print(list[1])
print(list[4])

random_words = ["apple", "banana", "grape", "orange", "strawberry",
    "kiwi", "mango", "peach", "plum", "pear",
    "apricot", "blackberry", "blueberry", "cantaloupe", "cherry",
    "coconut", "fig", "date", "pineapple", "pomegranate",
    "lemon", "lime", "tangerine", "nectarine", "melon",
    "papaya", "passionfruit", "dragonfruit", "raspberry", "watermelon",
    "carrot", "potato", "onion", "garlic", "pepper",
    "spinach", "kale", "broccoli", "cauliflower", "zucchini",
    "tomato", "cucumber", "eggplant", "pumpkin", "beet",
    "lettuce", "celery", "radish", "turnip", "parsnip",
    "cabbage", "asparagus", "artichoke", "sweetcorn", "greenbean",
    "peas", "chickpea", "lentil", "quinoa", "barley",
    "rice", "oats", "wheat", "millet", "sorghum",
    "sugar", "salt", "pepper", "vinegar", "oil",
    "butter", "cheese", "yogurt", "milk", "cream",
    "egg", "chicken", "beef", "pork", "fish",
    "shrimp", "crab", "lobster", "scallop", "clam",
    "squid", "octopus", "tofu", "seitan", "tempeh",
    "bread", "roll", "croissant", "bagel", "biscuit",
    "cake", "cookie", "brownie", "pie", "tart",
    "pudding", "jelly", "syrup", "candy", "chocolate",
    "donut", "popcorn", "snack", "chip", "crackers",
    "cereal", "granola", "muesli", "scone", "waffle",
    "pancake", "smoothie", "juice", "tea", "coffee",
    "soda", "water", "beer", "wine", "whiskey",
    "vodka", "rum", "gin", "champagne", "cocktail",
    "sangria", "punch", "shake", "malt", "ale",
    "cider", "seltzer", "kombucha", "herb", "spice",
    "oregano", "basil", "thyme", "rosemary", "sage",
    "cilantro", "parsley", "dill", "chili", "cumin",
    "turmeric", "ginger", "mustard", "ketchup", "salsa",
    "barbecue", "mayonnaise", "relish", "sriracha", "wasabi",
    "honey", "maple", "sugarcane", "molasses", "cornstarch",
    "flour", "yeast", "baking", "salt", "peppercorn",
    "cocoa", "chili", "nutmeg", "vanilla", "almond",
    "walnut", "hazelnut", "peanut", "cashew", "pistachio",
    "chestnut", "macadamia", "pecan", "coconut", "pine",
    "acorn", "cereal", "barley", "corn", "rye",
    "oat", "sesame", "sunflower", "pumpkin", "flax",
    "chia", "hemp", "spelt", "millet", "amaranth",
    "buckwheat", "quinoa", "wildrice", "brownrice", "whiterice",
    "sorghum", "teff", "polenta", "grits", "porridge",
    "creamcheese", "ricotta", "feta", "gorgonzola", "brie",
    "cheddar", "parmesan", "mozzarella", "bluecheese", "asiago",
    "provolone", "fontina", "pecorino", "cottage", "goatcheese",
    "soy", "almondmilk", "coconutmilk", "oatmilk", "rice",
    "cashewmilk", "hempmilk", "milkshake", "icecream", "gelato"]
print(random_words[-1])

#list slicing
list=[3,22,30,5.3,20]
print(list[1:3])
print(list[1:4])
print(list[2:-1])

#update list elements
science=["art","chemistry","math"]
science[0]="biology"
print(science)
science[-1]="geology"
print(science)
integers=[2,5,9,20,27]
integers.remove(5)
integers.remove(27)
print(integers)
integers.pop()
print(integers)

#pop, remove, del
list_fruit=["mango","strawberry","apple","melon"]
del list_fruit[0]
print(list_fruit)
lsit_nams=["john","ron","jerry"]
lsit_nams.append("george")
print(lsit_nams)
 """