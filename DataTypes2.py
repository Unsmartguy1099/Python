#Sets------------------------------------------

#union (| or .union()): Combines two sets, returning a new set containing all unique elements from both sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # or union_set = set1.union(set2)
# union_set contains {1, 2, 3, 4, 5}

#intersection (& or .intersection()): Returns a new set containing elements that are common to both sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1 & set2  # or intersection_set = set1.intersection(set2)
# intersection_set contains {3}

#difference (- or .difference()): Returns a new set containing elements that are in the first set but not in the second set.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1 - set2  # or difference_set = set1.difference(set2)
# difference_set contains {1, 2}

#symmetric Difference (^ or .symmetric_difference()): Returns a new set containing elements that are in either of the sets but not in both.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
symmetric_difference_set = set1 ^ set2  # or symmetric_difference_set = set1.symmetric_difference(set2)
# symmetric_difference_set contains {1, 2, 4, 5}

#subset (<= or .issubset()) and Superset (>= or .issuperset()): Check if one set is a subset or superset of another.
set1 = {1, 2, 3}
set2 = {1, 2}
is_subset = set2 <= set1  # or is_subset = set2.issubset(set1)
# is_subset is True

is_superset = set1 >= set2  # or is_superset = set1.issuperset(set2)
# is_superset is True

#disjoint (isdisjoint()): Checks if two sets have no common elements.
set1 = {1, 2, 3}
set2 = {4, 5, 6}
is_disjoint = set1.isdisjoint(set2)
# is_disjoint is True because set1 and set2 have no common elements


#List operations-------------------------------------------

#appending Elements (append()): Add an element to the end of the list.
fruits = ["apple", "banana"]
fruits.append("cherry")
# fruits is now ["apple", "banana", "cherry"]

#extending Lists (extend() or +=): Append elements from another iterable to the end of the list.
fruits = ["apple", "banana"]
more_fruits = ["cherry", "orange"]
fruits.extend(more_fruits)
# fruits is now ["apple", "banana", "cherry", "orange"]

#inserting Elements (insert()): Insert an element at a specific index in the list.
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "orange")
# fruits is now ["apple", "orange", "banana", "cherry"]

#removing Elements (remove()): Remove the first occurrence of a specified element from the list.
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
# fruits is now ["apple", "cherry"]

#popping Elements (pop()): Remove and return an element at a specified index. If no index is provided, it removes and returns the last element.
fruits = ["apple", "banana", "cherry"]
popped_fruit = fruits.pop(1)
# fruits is now ["apple", "cherry"], popped_fruit is "banana"

#indexing and Slicing: Access elements by their index or slice a list to extract a portion.
fruits = ["apple", "banana", "cherry"]
first_fruit = fruits[0]
sliced_fruits = fruits[1:3]  # ["banana", "cherry"]

#checking for existence (in): check if an element exists in the list.
fruits = ["apple", "banana", "cherry"]
is_banana_in_list = "banana" in fruits  # True

#counting Occurrences (count()): Count the number of times an element appears in the list.
fruits = ["apple", "banana", "cherry", "banana"]
banana_count = fruits.count("banana")  # 2

#sorting (sort()): Sort the list in ascending order (in-place). Use reverse=True for descending order.
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
numbers.sort()
# numbers is now [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

#reversing (reverse()): Reverse the elements of the list in-place.
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
# fruits is now ["cherry", "banana", "apple"]

#copying Lists: Create a copy of a list using slicing or the copy() method.
original_list = [1, 2, 3]
copied_list = original_list[:]
# or
copied_list = original_list.copy()

#clearing (clear()): Remove all elements from the list.
fruits = ["apple", "banana", "cherry"]
fruits.clear()
# fruits is now []

#Using list as a stack
# Initialize an empty stack using a list
stack = []

# Push elements onto the stack
stack.append(1)
stack.append(2)
stack.append(3)

# Pop elements from the stack (LIFO order)
top_element = stack.pop()  # Removes and returns 3



#Dictionary operations------------------------------------------

#reating a Dictionary:
#   Create an empty dictionary:
my_dict = {}
#   Create a dictionary with key-value pairs:
person = {"name": "John", "age": 30}

#accessing values: 
#   Access the value associated with a specific key:
name = person["name"]  # "John"
#   Use the .get() method to access a value safely, with a default value if the key doesn't exist:
age = person.get("age", 0)  # 30 (default value 0 if "age" key doesn't exist)

#Add a new key-value pair or modify an existing one:
person["city"] = "New York"  # Adds or modifies the "city" key

#Removing Entries (del and .pop()):
#   delete an entry by key using the del statement:
del person["age"]  # Removes the "age" key-value pair
#use the .pop() method to remove and return the value associated with a key:
city = person.pop("city")  # Removes and returns the value of "city"

#Check if a key exists in the dictionary:
has_age = "age" in person  # True

#Get a list of keys, values, or key-value pairs:
keys = person.keys()  # ["name"]
values = person.values()  # ["John"]
items = person.items()  # [("name", "John")]

#Create a shallow copy of a dictionary:
copied_dict = person.copy()
# or
copied_dict = dict(person)

#remove all key-value pairs from a dictionary:
person.clear()

#get the number of key-value pairs in a dictionary:
count = len(person)

#dictionaries can contain other dictionaries as values:
person = {"name": "John", "address": {"street": "123 Main St", "city": "New York"}}
street = person["address"]["street"]  # "123 Main St"
