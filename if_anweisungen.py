# IF Statement (Simple Condition)

# password = input("Password...: ")

# if password == "abc123":
#     print("nice password!")       # condition True
# else:
#     print("try again")            # condition False


# IF / ELIF / ELSE Chain

# die_deutschen = input("Bewerte Die Deutschen (podcast <1-6>): ")

# if die_deutschen == "1":
#     print("Beste")
# elif die_deutschen == "2":
#     print("Gut")
# elif die_deutschen == "3":
#     print("Ok")
# elif die_deutschen == "4":
#     print("Buuhh")
# elif die_deutschen == "5":
#     print("Bösartig")
# else:
#     print("Grausam")              # default when no case matches


# MATCH Statement (String Input)

# note = input("Gib die Note ein: ")

# match note:
#     case "1":
#         print("Sehr gut!")
#     case "2":
#         print("Gut!")
#     case "3":
#         print("Befriedigend.")
#     case "4":
#         print("Ausreichend.")
#     case "5":
#         print("Mangelhaft!")
#     case _:
#         print("Ungenügend!!")     # default case (_ acts like "else")


# MATCH Statement (Integer Input)

# note = int(input("Gib die Note ein: "))

# match note:
#     case 1:
#         print("Sehr gut!")
#     case 2:
#         print("Gut!")
#     case 3:
#         print("Befriedigend.")
#     case 4:
#         print("Ausreichend.")
#     case 5:
#         print("Mangelhaft!")
#     case 6:
#         print("Ungenügend!!")


# MATCH Statement (List Pattern)

# note = [1, 2, 3]

# match note:
#     case [1, 2, 3]:
#         print("wooww!")           # matches exact list pattern
#     case 2:
#         print("Gut!")
#     case 3:
#         print("Befriedigend.")
#     case 4:
#         print("Ausreichend.")
#     case 5:
#         print("Mangelhaft!")
#     case 6:
#         print("Ungenügend!!")


# FOR Loop (Simple)

# passwords = ["abc123", "gehe1m", "test", "123456"]

# for password in passwords:
#     print(password)
#     break                        # stops after first item

# Output:
# abc123


# FOR Loop with Break Condition

# for password in passwords:
#     print(password)
#     if len(password) < 5:
#         break                     # stops when password shorter than 5

# Output:
# abc123
# gehe1m
# test


# WHILE Loops (Basics)

# level = 25
# round = 0

# Infinite loop (level never changes)
# while level > 0:
#     print(f"Round: {round}")
#     round += 1

# Controlled loop (stops when level = 0)
# while level > 0:
#     print(f"Round: {round}")
#     round += 1
#     level -= 1


# WHILE Loop with User Input

# name = input("enter a name!, x to stop: ")
# namelist = []

# while name != "x":
#     namelist.append(name)         # adds name to list
#     print(namelist)
#     name = input("enter a name!, x to stop: ")  # repeat until 'x'


# Infinite Loop Example (Break)

# userlist = []
# user = input("please give user...(X): ")
# i = 0

# while user != "X":
#     userlist.append(user)
#     print(userlist)

# while True:                      # endless loop
#     userlist.append(user)
#     print(userlist)
#     if i == 3:
#         break                    # stop after 3
# print(userlist)


# Walrus Operator (:=)

# Old method (without walrus operator)
# userlist = []
# user = input("please give user...(X): ")

# while user != "X":
#     userlist.append(user)
#     user = input("please give user...(X): ")
# print(userlist)


# New method (with walrus operator)
# userlist = []

# while (user := input("please give user...(X): ")) != "X":
#     userlist.append(user)

# print(userlist)