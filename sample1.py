print("Hello World")
print(2**3)

print(type(5))
print(type(2.455))
print(type(True))
print(type("Hello World"))
print(type([2, 3, 4, 5]))



thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(type(thisdict))
print(int(4.567))


# STRINGS ::::::::::::::::::::::::::::::::::::::::::::::::::::::::
this_string = 'Simon\'s skateboard is in the garage.'
print(this_string)
print(len("ababa") / len("ab"))
print('this' in 'this is a string')

my_string = "Carlos"
print(my_string.islower())
print(my_string.count('a'))
print(my_string.find('a'))
print("Mohammed has {} balloons".format(27))

a = "Hello, World!"
print('-----------------------')
print(a[1])
print("He" in a)

b = "Hello, World!"
print(b[2:5])

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"
print(len(a))

a = "Hello, World!"
print(a.lower())

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

animal = "dog"
action = "bite"
print("Does your {} {}?".format(animal, action))

new_str = "\n".join(["fore", "aft", "starboard", "port"])
print(new_str)


# LISTS ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

list_of_random_things = [1, 3.4, 'a string', True]
print(list_of_random_things[0])


# Membership operators
print(5 not in [1, 2, 3, 4, 6])

a = [2, 3, 4, 5]
print(3 in a)

letters = ['a', 'b', 'c', 'd']
letters.append('z')
print(letters)

# Sorting a list
sizes = [15, 6, 89, 34, 65, 35]
print(sorted(sizes))
print(sorted(sizes), reversed)

# Removing list items
colors = ["red", "green", "blue"]
colors.pop() # removes last item

colors = ["red", "green", "blue"]
colors.pop(1) # removes "green" item

colors = ["red", "green", "blue"]
colors.remove("green") # removes "green" item

colors = ["red", "green", "blue"]
colors.clear() # removes all items

# Ordering list items
colors = ["red", "green", "blue"]
colors.sort()
colors.sort(reverse=True)

# Getting list item index
colors = ["red", "green", "blue"]
print(colors.index("red"))

# Counting the number of times an element is in a list
colors = ["red", "green", "blue", "red"]
print(colors.count("red"))


# To add an item at the specified index, use the insert() method:

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# joining list items
# Only strings can be joined
nautical_directions = "-".join(thislist)
print(nautical_directions)

# append() adds items at the end
thislist.append("Bloody Python")
print(thislist)

# Convert a tuple to a list
numbers_list = list((1, 2, 3, 4))

# Loop Through a List

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

# adds the last element of the card_deck list to the hand list
# until the values in hand add up to 17 or more
while sum(hand)  < 17:
    hand.append(card_deck.pop())


# SETS ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# A set is a mutable data structures
colors = {"Red", "Green", "Blue"}
print("#####################")
print(type(colors)) # <class 'set'>
print("Red" in colors)
colors.add("Violet")
colors.remove("Red")
colors.clear()
del colors

# We can create a set from a list
thislist = ["apple", "banana", "cherry"]
thislist_set = set(thislist)

print("apple" in thislist_set)

# instead of append( ), sets have the add( ) method
thislist_set.add("pineapple")

# To add more than one item to a set use the update() method.
thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])

thisset = {"apple", "banana", "cherry"}

print(len(thisset))

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

thisset = {"apple", "banana", "cherry"}
del thisset

locations = {
    (12.344, 321.12): "Tokyo",
    (44.344, -56.12): "New York"
}



# For sets, the pop( ) method removes a random element from the set
fruit = {"apple", "banana", "orange", "grapefruit"}  # define a set

print("watermelon" in fruit)  # check for element

fruit.add("watermelon")  # add an element
print(fruit)

print(fruit.pop())  # remove a random element
print(fruit)

numbers = [1, 2, 6, 3, 1, 1, 6]
unique_nums = set(numbers)
print(unique_nums)

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)




# TUPLES ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

x = (1, 2, 3)
print(x)
print(type(x))
print(dir(x))

y = (1) # This is not considered a tuple
print(type(y)) # <class 'int'>

z = (1,)  # This is now a tuple

x = (1, 2, 3)
print(x[1])

manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]

# the code breaks the loop when weight exceeds or reaches the limit
print("METHOD 1")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking loop now!")
        break
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))



# DICTIONARIES ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

x = thisdict.get("model")

# Dictionaries can have keys of any immutable type, like integers or tuples, not just strings.
elements = {"hydrogen": 1, "helium": 2, "carbon": 6}

print("carbon" in elements)
x = elements.get("dilithium")  # None if value is not found
print(x is None)
print(x is not None)
elements.get('kryptonite', 'There\'s no such element!') # "There's no such element!"

population = {'Shanghai': 17.8,
              'Istanbul': 13.3,
              'Karachi': 13.0,
              'Mumbai': 12.5}
print(population.keys()) # dict_keys(['Shanghai', 'Istanbul', 'Karachi', 'Mumbai'])
print(population.items()) #

animals = {'dogs': [20, 10, 15, 8, 32, 15], 'cats': [3,4,2,8,2,4], 'rabbits': [2, 3, 3], 'fish': [0.3, 0.5, 0.8, 0.3, 1]}

elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}

cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

for key, value in cast.items():
    print("Actor: {}    Role: {}".format(key, value))


squares = [x**2 for x in range(9) if x % 2 == 0]


squares2 = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]



print(x)
if 5 > 2:
  print("Five is greater than two!")


