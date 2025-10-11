# FUNCTIONS

# print("woooww print!") # simple print example

# example of indentation (Python requires correct indent)
# def say_hello(name):
# |   ← indented block belongs to function

# empty function (does nothing)
# def say_hello(name):
#     pass
# say_hello("dev") # runs but no output

# function with one parameter
# def say_hello(name):
#     print(name)
#     print("better")
# say_hello("no keyword def") # prints name and "better"

# function called with too many arguments
# def say_hello(name):
#     print(name)
#     print("better")
# say_hello("no", "keyword") # TypeError, too many arguments

# function called without required argument
# def say_hello(name):
#     print(name)
#     print("better")
# say_hello() # TypeError, missing required argument


# function with two parameters
# def say_hello(name, surname):
#     print(f"moin {name} {surname}")
# say_hello("adem", "o") # moin adem o


# function with sum (no return)
# def add(a, b):
#     sum = a + b
#     print(sum)
# add(2, 31) # 33, prints sum directly


# function with return value
# def add(a, b):
#     sum = a + b
#     return sum
# print(add(10, 41)) # 51, prints return value


# storing return value in variable
# def add(a, b):
#     sum = a + b
#     return sum
# s = add(21, 20)
# print(f"sum: {s}") # sum: 41


# error example: wrong variable name in print
# def add(a, b):
#     sum = a + b
#     return sum
# s = add(21, 20)
# print(f"sum: {sum}") # NameError, 'sum' not defined (should be 's')





# FUNCTIONS with multiple and variable arguments

# wrong function definition (needs exactly 5 arguments)
# def add(sum1, sum2, sum3, sum4, sum5):
#     sum = sum1 + sum2
#     print(sum)

# add(1, 2, 3, 4, 5) # TypeError, function defined for 5 arguments only uses 2 inside
# add(1, 2)          # missing arguments
# add(1, 2, 42)      # missing arguments


# using *args (variable number of arguments)
# def add(*sum):
#     print(sum)
# add(1, 2, 3) # (1, 2, 3), collects all arguments into a tuple


# function with *args and sum()
# def add(*summand):
#     print(sum(summand))
# add(1, 2, 3) # 6, calculates total sum
# add() # 0, empty tuple → sum = 0


# function printing *args as tuple
# def add(*summand):
#     print(summand)
# add() # (), empty tuple (no arguments passed)


# function with normal and variable arguments
# def add_your_best_game(name, *game):
#     print(f"whats,up? {name}")
#     print(f"your rank!: {game}")
# add_your_best_game("user", "coder") 
# whats,up? user
# your rank!: ('coder',)


# function with two normal parameters + variable arguments
# def add_your_best_game(name, ingame_name, *game):
#     print(f"whats,up? {name} {ingame_name}")
#     print(f"your rank!: {game}")
# add_your_best_game("user", "SP", "coder", "backend")
# whats,up? user SP
# your rank!: ('coder', 'backend')


# no extra game arguments
# def add_your_best_game(name, ingame_name, *game):
#     print(f"whats,up? {name} {ingame_name}")
#     print(f"your rank!: {game}")
# add_your_best_game("user", "SP")
# whats,up? user SP
# your rank!: ()






# FUNCTIONS with **kwargs (keyword arguments)

# def kwars_test(**test):
#     print(test)
# kwars_test()
# {} , empty dictionary (no keyword arguments given)


# def kwars_test(**test):
#     print(test)
# kwars_test(a=1, b=2, c=3)
# {'a': 1, 'b': 2, 'c': 3}, collects keyword arguments into a dictionary


# function with fixed arguments
# def car(model, color, ps, doors):
#     print(f"{model} {color} {ps} {doors}")
# car("Mercedes", "black", "120", "5")
# Mercedes black 120 5


# function with **kwargs
# def car(**data):
#     print(data.get("model"))
# car(model="Mercedes", color="black")
# Mercedes, get() fetches value by key


# def car(**data):
#     model = data.get("model")
#     color = data.get("color")
#     print(f"{model} {color}")
# car(color="Black", model="Mercedes")
# Mercedes Black, order doesn’t matter


# def car(**data):
#     model = data.get("model")
#     color = data.get("color")
#     age = data.get("age")
#     print(f"{model} {color} {age}")
# car(color="Black", model="Mercedes", age=2005)
# Mercedes Black 2005


# def car(**data):
#     model = data.get("model")
#     color = data.get("color")
#     age = data.get("age")
#     doors = data.get("doors", "N/A")
#     print(f"{model} {color} {age} {doors}")
# car(color="Black", model="Mercedes", age=2005)
# Mercedes Black 2005 N/A, default value for missing key


# def car(**data):
#     model = data.get("model", "car")
#     color = data.get("color", "hex")
#     age = data.get("age", "any")
#     doors = data.get("doors", "N/A")
#     print(f"{model} {color} {age} {doors}")
# car(color="doors")
# car doors any N/A, default values used for missing arguments





# VARIABLE SCOPES (Gültigkeitsbereiche)

# level = 0  # global variable (accessible everywhere in this file)

# def level_up():
#     global level          # 'global' allows modification of the global variable
#     level += 1            # increases global 'level' by 1

# level_up()
# level_up()
# level_up()
# print(f"your level {level}") # your level 3, global variable changed inside function





# print("test input programm!") # simple print message

# test = input("give something in: ")
# waits for user input and stores it in variable 'test'
# print(f"idk {test}") # prints the entered text


# year = int(input("what year you born...?\n"))
# converts the input string to an integer using int()

# age = 2025 - year
# calculates the user's age based on birth year

# print(f"you are {age} years old.") # prints calculated ageld.")







# EXEC() — execute dynamic Python code stored as string

# cmd = "file = input('use .exe: ');print(f'hey {file}')"
# exec(cmd) # runs the string as Python code
# input waits for user, then prints result

# Example: running a full tkinter Snake Game dynamically
# cmd = """ (Snake Game code) """
# exec(cmd) # executes the entire multiline string
# runs the Snake game directly from the string variable


# cmd = """
# import tkinter as tk
# import random

# WIDTH = 400
# HEIGHT = 400
# CELL_SIZE = 20

# class SnakeGame:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Snake (tkinter)")

#         self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
#         self.canvas.pack()

#         self.snake = [(100, 100), (80, 100), (60, 100)]
#         self.snake_dir = (CELL_SIZE, 0)
#         self.food = self.place_food()
#         self.running = True
#         self.score = 0

#         self.root.bind("<KeyPress>", self.change_direction)
#         self.update_game()

#     def place_food(self):
#         x = random.randrange(0, WIDTH, CELL_SIZE)
#         y = random.randrange(0, HEIGHT, CELL_SIZE)
#         return (x, y)

#     def change_direction(self, event):
#         key = event.keysym
#         if key == "Up" and self.snake_dir != (0, CELL_SIZE):
#             self.snake_dir = (0, -CELL_SIZE)
#         elif key == "Down" and self.snake_dir != (0, -CELL_SIZE):
#             self.snake_dir = (0, CELL_SIZE)
#         elif key == "Left" and self.snake_dir != (CELL_SIZE, 0):
#             self.snake_dir = (-CELL_SIZE, 0)
#         elif key == "Right" and self.snake_dir != (-CELL_SIZE, 0):
#             self.snake_dir = (CELL_SIZE, 0)

#     def update_game(self):
#         if not self.running:
#             return

#         new_head = (self.snake[0][0] + self.snake_dir[0],
#                     self.snake[0][1] + self.snake_dir[1])

#         if (new_head[0] < 0 or new_head[0] >= WIDTH or
#             new_head[1] < 0 or new_head[1] >= HEIGHT or
#             new_head in self.snake):
#             self.running = False
#             self.canvas.create_text(WIDTH//2, HEIGHT//2, text="GAME OVER",
#                                     fill="red", font=("Arial", 24))
#             return

#         self.snake.insert(0, new_head)

#         if new_head == self.food:
#             self.score += 1
#             self.food = self.place_food()
#         else:
#             self.snake.pop()

#         self.draw()
#         self.root.after(120, self.update_game)

#     def draw(self):
#         self.canvas.delete("all")

#         x, y = self.food
#         self.canvas.create_rectangle(x, y, x+CELL_SIZE, y+CELL_SIZE,
#                                     fill="red")

#         for i, (x, y) in enumerate(self.snake):
#             color = "green" if i > 0 else "lime"
#             self.canvas.create_rectangle(x, y, x+CELL_SIZE, y+CELL_SIZE,
#                                         fill=color)

#         self.canvas.create_text(40, 10, text=f"Score: {self.score}",
#                                 fill="white", font=("Arial", 12))

# root = tk.Tk()
# game = SnakeGame(root)
# root.mainloop()
# """
# exec(cmd)


# import base64
# cmd = "aW1wb3J0IHRraW50ZXIgYXMgdGs..."  # base64 encoded Python code
# exec(base64.b64decode(cmd))  # decode and execute the code
# decodes the text, then runs it as normal Python code


# import base64

# cmd = "aW1wb3J0IHRraW50ZXIgYXMgdGsNCmltcG9ydCByYW5kb20NCg0KV0lEVEggPSA0MDANCkhFSUdIVCA9IDQwMA0KQ0VMTF9TSVpFID0gMjANCg0KY2xhc3MgU25ha2VHYW1lOg0KICAgIGRlZiBfX2luaXRfXyhzZWxmLCByb290KToNCiAgICAgICAgc2VsZi5yb290ID0gcm9vdA0KICAgICAgICBzZWxmLnJvb3QudGl0bGUoIlNuYWtlICh0a2ludGVyKSIpDQoNCiAgICAgICAgc2VsZi5jYW52YXMgPSB0ay5DYW52YXMocm9vdCwgd2lkdGg9V0lEVEgsIGhlaWdodD1IRUlHSFQsIGJnPSJibGFjayIpDQogICAgICAgIHNlbGYuY2FudmFzLnBhY2soKQ0KDQogICAgICAgIHNlbGYuc25ha2UgPSBbKDEwMCwgMTAwKSwgKDgwLCAxMDApLCAoNjAsIDEwMCldDQogICAgICAgIHNlbGYuc25ha2VfZGlyID0gKENFTExfU0laRSwgMCkNCiAgICAgICAgc2VsZi5mb29kID0gc2VsZi5wbGFjZV9mb29kKCkNCiAgICAgICAgc2VsZi5ydW5uaW5nID0gVHJ1ZQ0KICAgICAgICBzZWxmLnNjb3JlID0gMA0KDQogICAgICAgIHNlbGYucm9vdC5iaW5kKCI8S2V5UHJlc3M+Iiwgc2VsZi5jaGFuZ2VfZGlyZWN0aW9uKQ0KICAgICAgICBzZWxmLnVwZGF0ZV9nYW1lKCkNCg0KICAgIGRlZiBwbGFjZV9mb29kKHNlbGYpOg0KICAgICAgICB4ID0gcmFuZG9tLnJhbmRyYW5nZSgwLCBXSURUSCwgQ0VMTF9TSVpFKQ0KICAgICAgICB5ID0gcmFuZG9tLnJhbmRyYW5nZSgwLCBIRUlHSFQsIENFTExfU0laRSkNCiAgICAgICAgcmV0dXJuICh4LCB5KQ0KDQogICAgZGVmIGNoYW5nZV9kaXJlY3Rpb24oc2VsZiwgZXZlbnQpOg0KICAgICAgICBrZXkgPSBldmVudC5rZXlzeW0NCiAgICAgICAgaWYga2V5ID09ICJVcCIgYW5kIHNlbGYuc25ha2VfZGlyICE9ICgwLCBDRUxMX1NJWkUpOg0KICAgICAgICAgICAgc2VsZi5zbmFrZV9kaXIgPSAoMCwgLUNFTExfU0laRSkNCiAgICAgICAgZWxpZiBrZXkgPT0gIkRvd24iIGFuZCBzZWxmLnNuYWtlX2RpciAhPSAoMCwgLUNFTExfU0laRSk6DQogICAgICAgICAgICBzZWxmLnNuYWtlX2RpciA9ICgwLCBDRUxMX1NJWkUpDQogICAgICAgIGVsaWYga2V5ID09ICJMZWZ0IiBhbmQgc2VsZi5zbmFrZV9kaXIgIT0gKENFTExfU0laRSwgMCk6DQogICAgICAgICAgICBzZWxmLnNuYWtlX2RpciA9ICgtQ0VMTF9TSVpFLCAwKQ0KICAgICAgICBlbGlmIGtleSA9PSAiUmlnaHQiIGFuZCBzZWxmLnNuYWtlX2RpciAhPSAoLUNFTExfU0laRSwgMCk6DQogICAgICAgICAgICBzZWxmLnNuYWtlX2RpciA9IChDRUxMX1NJWkUsIDApDQoNCiAgICBkZWYgdXBkYXRlX2dhbWUoc2VsZik6DQogICAgICAgIGlmIG5vdCBzZWxmLnJ1bm5pbmc6DQogICAgICAgICAgICByZXR1cm4NCg0KICAgICAgICBuZXdfaGVhZCA9IChzZWxmLnNuYWtlWzBdWzBdICsgc2VsZi5zbmFrZV9kaXJbMF0sDQogICAgICAgICAgICAgICAgICAgIHNlbGYuc25ha2VbMF1bMV0gKyBzZWxmLnNuYWtlX2RpclsxXSkNCg0KICAgICAgICBpZiAobmV3X2hlYWRbMF0gPCAwIG9yIG5ld19oZWFkWzBdID49IFdJRFRIIG9yDQogICAgICAgICAgICBuZXdfaGVhZFsxXSA8IDAgb3IgbmV3X2hlYWRbMV0gPj0gSEVJR0hUIG9yDQogICAgICAgICAgICBuZXdfaGVhZCBpbiBzZWxmLnNuYWtlKToNCiAgICAgICAgICAgIHNlbGYucnVubmluZyA9IEZhbHNlDQogICAgICAgICAgICBzZWxmLmNhbnZhcy5jcmVhdGVfdGV4dChXSURUSC8vMiwgSEVJR0hULy8yLCB0ZXh0PSJHQU1FIE9WRVIiLA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZmlsbD0icmVkIiwgZm9udD0oIkFyaWFsIiwgMjQpKQ0KICAgICAgICAgICAgcmV0dXJuDQoNCiAgICAgICAgc2VsZi5zbmFrZS5pbnNlcnQoMCwgbmV3X2hlYWQpDQoNCiAgICAgICAgaWYgbmV3X2hlYWQgPT0gc2VsZi5mb29kOg0KICAgICAgICAgICAgc2VsZi5zY29yZSArPSAxDQogICAgICAgICAgICBzZWxmLmZvb2QgPSBzZWxmLnBsYWNlX2Zvb2QoKQ0KICAgICAgICBlbHNlOg0KICAgICAgICAgICAgc2VsZi5zbmFrZS5wb3AoKQ0KDQogICAgICAgIHNlbGYuZHJhdygpDQogICAgICAgIHNlbGYucm9vdC5hZnRlcigxMjAsIHNlbGYudXBkYXRlX2dhbWUpDQoNCiAgICBkZWYgZHJhdyhzZWxmKToNCiAgICAgICAgc2VsZi5jYW52YXMuZGVsZXRlKCJhbGwiKQ0KDQogICAgICAgIHgsIHkgPSBzZWxmLmZvb2QNCiAgICAgICAgc2VsZi5jYW52YXMuY3JlYXRlX3JlY3RhbmdsZSh4LCB5LCB4K0NFTExfU0laRSwgeStDRUxMX1NJWkUsDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBmaWxsPSJyZWQiKQ0KDQogICAgICAgIGZvciBpLCAoeCwgeSkgaW4gZW51bWVyYXRlKHNlbGYuc25ha2UpOg0KICAgICAgICAgICAgY29sb3IgPSAiZ3JlZW4iIGlmIGkgPiAwIGVsc2UgImxpbWUiDQogICAgICAgICAgICBzZWxmLmNhbnZhcy5jcmVhdGVfcmVjdGFuZ2xlKHgsIHksIHgrQ0VMTF9TSVpFLCB5K0NFTExfU0laRSwNCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBmaWxsPWNvbG9yKQ0KDQogICAgICAgIHNlbGYuY2FudmFzLmNyZWF0ZV90ZXh0KDQwLCAxMCwgdGV4dD1mIlNjb3JlOiB7c2VsZi5zY29yZX0iLA0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBmaWxsPSJ3aGl0ZSIsIGZvbnQ9KCJBcmlhbCIsIDEyKSkNCg0Kcm9vdCA9IHRrLlRrKCkNCmdhbWUgPSBTbmFrZUdhbWUocm9vdCkNCnJvb3QubWFpbmxvb3AoKQ=="

# exec(base64.b64decode(cmd))