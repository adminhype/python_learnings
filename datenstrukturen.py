# LISTS (Arrays in Python)

# empty list
# list = []

# list with mixed data types
# list = [42, "Adminhype", True]
# print(len(list)) # 3, number of elements in list

# list with numbers
# list2 = [0, 2, 4, 6, 8, 10]
# print(len(list2)) # 6, length of list

# access by index (starts at 0)
# list3 = [0, 2, 4, 6, 8, 10]
# print(list3[2]) # 4, third element (index 2)

# negative index = from the end
# list4 = [0, 2, 4, 6, 8, 10]
# print(list4[-1]) # 10, last element

# slicing (from start to index 3, exclusive)
# list5 = [0, 2, 4, 6, 8, 10]
# print(list5[:3]) # [0, 2, 4], first three elements

# slicing with start and end index
# list6 = [0, 2, 4, 6, 8, 10]
# print(list6[2:6]) # [4, 6, 8, 10], elements from index 2 to 5

# invalid index (out of range)
# list7 = [0, 2, 4, 6, 8, 10]
# print(list7[28]) # IndexError, list index out of range







# LIST OPERATIONS (Add, Combine, Multiply)

# numbers = [1, 2, 5, 6, 9]
# more_numbers = [0, 10, 12, 12]

# total = numbers + more_numbers
# total = numbers + [10, 20, 30]
# print(total) # combines two lists

# bits = [0, 1]
# print(bits * 3) # [0, 1, 0, 1, 0, 1], repeats list 3 times


# APPEND (add single element)
# numbers = [1, 2, 5, 6, 9]
# numbers.append(10)
# numbers.append(10, 11, 12) # error, append adds only one element
# print(numbers)


# SORT and COUNT
# numbers = [2, 6, 7, 9, 8, 2, 1]
# numbers.sort() # ascending order
# numbers.sort(reverse=True) # descending order
# print(numbers)
# print(numbers.count(8)) # 1, counts how many times 8 appears


# REMOVE
# types = [8, 3, 2, "World", True, False, 3, 5, "NuN"]
# types.remove(True) # removes first occurrence of True
# print(types)


# INSERT
# numbers = [0, 1, 2, 4, 5, 6, 7]
# numbers.insert(3, 3) # inserts 3 at index 3
# numbers.insert(3, "three") # inserts "three" at index 3
# print(numbers)


# CLEAR vs COPY

# Both refer to same list (copy = numbers)
# numbers = [0, 1, 2, 4, 5, 6, 7]
# copy = numbers
# copy.clear() # clears both because same reference
# print(numbers) # []

# Independent copy
# numbers = [0, 1, 2, 4, 5, 6, 7]
# copy = numbers.copy()
# copy.clear()
# print(numbers) # original unchanged


# INDEX and IN
# numbers = [0, 1, 2, 4, 5, 6, 7]
# position = numbers.index(5)
# print(position) # 4, position of number 5

# numbers = [0, 1, 2, 4, 5, 6, 7]
# print(3 in numbers) # False, checks if 3 is in list


# JOIN (only works with strings)
# numbers = [0, 1, 2, 4, 5, 6, 7]
# print(";".join(numbers)) # TypeError, elements must be strings

# numbers = ["1", "2", "3"]
# print(";".join(numbers)) # 1;2;3, joins list with ";"

# numbers = ["A", "D", "O"]
# print("".join(numbers)) # ADO, joins without separator





# TUPLES (immutable lists)

# print(()) # (), empty tuple
# print((1, 2, 3)) # (1, 2, 3), tuple with 3 elements

# test = (1, 2, 5, 7, 28, 29)
# print(len(test)) # 6, number of elements in tuple

# test = (1, 2, 3, 4, 5, 6, 20)
# print(test[2]) # 3, third element (index 2)

# print((1, 2, 3, 4, 5, 6, 20)[-4]) # 4, 4th from the end

# function returning multiple values
# def add(a, b):
#     sum = a + b
#     return a, b, sum  # returns a tuple

# total = add(1, 4)
# print(total) # (1, 4, 5), tuple of results
# print(type(total)) # <class 'tuple'>

# total = (1, 2, 3) + (4, 5)
# print(total)

# tupel = (2, 3, 5, 7, 9, 11, 13, 2, 5, 7, 7 , 0)
# n = tupel.count(7)
# print(n)

# tupel = (2, 3, 5, 7, 9, "name", 11, 13, 2, 5, 7, 7 , 0)
# n = tupel.index("name")
# print(n)

# numbers = (1, 2, 3, 4, 5)
# print(list(numbers))
# print(type(list(numbers)))

# numbers = (1, 2, 3, 4, 5)
# list = list(numbers)
# list.sort()
# print(list)






# SETS (unordered unique collections)

# {} creates an empty dictionary, not a set
# for an empty set, set()

# print({12, 28, 38, True, 29}[1:3])
# Error: TypeError
# sets are unordered and not subscriptable (no slicing or indexing)

# print(len({12, 28, 38, True, 29})) 
# 5, number of unique elements in the set

# empty set
# seen = set() # empty set ready to store unique values

# SET OPERATIONS (add, remove, clear, copy, convert)

# numbers = {1, 4, 6, 7, 0}
# print(99 in numbers) # False, checks if 99 is in the set

# numbers = {1, 4, 6, 7, 0}
# numbers.add(-1)
# print(numbers) # {0, 1, 4, 6, 7, -1}, adds new element to set

# numbers = {1, 4, 6, 7, 0}
# numbers.add(4)
# print(numbers) # {0, 1, 4, 6, 7}, duplicates are ignored

# prim = {2, 3, 5, 7, 11}
# prim.remove(7)
# print(prim) # {2, 3, 5, 11}, removes element 7

# prim = {2, 3, 5, 7, 11}
# prim.clear()
# print(prim) # set(), removes all elements from set

# prim = {2, 3, 5, 7, 11}
# copy = prim.copy()
# print(prim) # {2, 3, 5, 7, 11}, creates a copy of the set

# prim = {2, 3, 17, 13, 11}
# list = list(prim)
# list.sort()
# print(list) # [2, 3, 11, 13, 17], converts set to sorted list





# DICTIONARIES (key-value pairs)

# book = {
#     "Adem": "0815"
# }
# print(type(book.get("Adem"))) # <class 'str'>, value is a string

# book1 = {
#     "Adem": 28
# }
# print(type(book1.get("Adem"))) # <class 'int'>, value is an integer

# book2 = {
#     "Adem": [0, 1, 2, 3, 4, 5]
# }
# print(book2.get("Adem")) # [0, 1, 2, 3, 4, 5], value is a list

# book3 = {
#     "Adem": [0, 1, 2, 3, 4, 5]
# }
# print(book3["Adem"]) # [0, 1, 2, 3, 4, 5], access directly by key

# book = {
#     "Adem": "0815"
# }
# print(book.get("meda")) # None, key not found (safe, no error)

# book = {
#     "Adem": "0815",
#     "Bremen": "28"
# }
# print(book.get("Bremen")) # 28, returns value for key "Bremen"

# book = {
#     1: "0815",
#     2: "28"
# }
# print(book.get(1)) # 0815, integer keys work fine

# book = {
#     []: "0815",
#     2: "28"
# }
# print(book.get([])) # TypeError, list is unhashable (cannot be used as key)

# book = {
#     False: "0815",
#     True: "28"
# }
# print(book.get(True)) # 28, boolean keys also allowed

# book = {
#     "anime": "death note",
#     "series": "blacklist"
# }
# print(len(book)) # 2, number of key-value pairs





# DICTIONARIES (key-value pairs)

# passwort_hashes = {
#     "abc123": "e99a18c428cb38d5f260853678922e03",
#     "312": "e48e13207341b6bffb7fb1622282247b",
#     "love": "b5c0b187fe309af0f4d35982fd961d7e"
# }

# print(passwort_hashes.get("abc123")) # e99a18..., returns hash for key
# print(passwort_hashes.get("geheiem")) # None, key not found
# print(passwort_hashes.get("geheiem", "2343242342342424")) # custom default if key not found


# numbers = {
#     "adem": "12334",
#     "ado": "13123",
#     "oncu": "2132"
# }

# numbers["adem"] = "22222"
# print(numbers) # {'adem': '22222', 'ado': '13123', 'oncu': '2132'}, updates value

# numbers["eva"] = "11111"
# print(numbers) # adds new key 'eva' with value '11111'

# numbers.update({"Adem": "33333"})
# print(numbers) # adds/updates multiple keys at once

# del numbers["adem"]
# print(numbers) # removes key 'adem' from dictionary

# numbers.clear()
# print(numbers) # {}, removes all elements

# copy = numbers.copy()
# print(numbers) # {}, creates a shallow copy (independent)

# print(type(numbers.keys())) # <class 'dict_keys'>, returns a view of all keys

# print(list(numbers.keys())) # [], converts keys to list

# print(type(numbers.values())) # <class 'dict_values'>, returns a view of all values

# print(list(numbers.values())) # [], converts values to list