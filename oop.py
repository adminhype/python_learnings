# CLASSES AND OBJECTS

# class Human:
#     def __init__(self, color, country, name):
#         self.color = color
#         self.country = country
#         self.name = name      
#         # __init__ is the constructor → runs automatically when object is created

#     def introduction(self):
#         print(f"i am {self.name}")  # prints name of the person

#     def eat(self):
#         pass  # placeholder method
#     def walk(self):
#         pass
#     def cry(self):
#         pass

# human1 = Human("White", "German", "Adolf")  # creates object human1
# human2 = Human("Black", "Ghana", "Abowey")  # creates object human2

# human2.introduction()  # i am Abowey





# class Company:
#     def __init__(self, color, country, name):
#         self.color = color
#         self.country = country
#         self.name = name    
#         # constructor sets up object attributes

#     def introduction(self):
#         print(f"i am {self.name}")  # shared method for all subclasses

#     def walk(self):
#         pass


# class Human(Company):
#     def eat(self):
#         pass

#     def cry(self):
#         pass
#     # inherits all attributes & methods from Company


# class Worker(Company):
#     def work(self):
#         print("do stuff!")  # adds custom method
#     # also inherits everything from Company


# human1 = Human("White", "German", "Adolf")
# human2 = Human("Black", "Ghana", "Abowey")

# worker1 = Worker("Yellow", "Tokyo", "Akasa")

# worker1.introduction()  # i am Akasa
# human2.introduction()   # i am Abowey




# CLASS EXAMPLE — Pokemon with attributes and private variable

# public attributes example
# class Pokemon:
#     def __init__(self, n, l):
#         self.n = n  # public attribute (name)
#         self.l = l  # public attribute (level)

#     def into(self):
#         print(f"{self.n}, {self.l}")  # prints name and level

# if __name__ == "__main__":
#     glurak = Pokemon("Glurakus", 0)
#     glurak.into()  # Glurakus, 0


## class Pokemon:
#     def __init__(self, n, l):
#         self.n = n
#         self.__l = l  # private variable (not directly accessible)

#     def into(self):
#         print(f"{self.n}, {self.n}")  # print name twice (small mistake)
    
#     def get_l(self):
#         return self.__l  # getter for private attribute

# if __name__ == "__main__":
#     glurak = Pokemon("Glurakus", 0)
#     schiggy = Pokemon("Schigga", 10)

#     glurak.into()   # Glurakus, Glurakus
#     schiggy.into()  # Schigga, Schigga

#     print(glurak.get_l())  # 0
#     print(schiggy.get_l()) # 10


# class Pokemon:
#     def __init__(self, n, l):
#         self.n = n
#         self.__l = l
#         self.into()  # automatically calls intro on creation

#     def into(self):
#         print(f"{self.n}, {self.n}")  # prints name twice (typo again)
    
#     def get_l(self):
#         return self.__l

# if __name__ == "__main__":
#     glurak = Pokemon("Glurakus", 0)
#     schiggy = Pokemon("Schigga", 10)
# # prints both intros immediately after creation






# CLASS: Pokemon (Encapsulation and Object Interaction)

# basic version — simple attributes
# class Pokemon:
#     def __init__(self, name, level):
#         self.__n = name
#         self.__health = 100
#         self.__level = 1  # starts at level 1 (fixed)

#     def intro(self):
#         print(f"{self.__n}, {self.__n}")  # prints name twice
    
#     def show_health(self):
#         return self.__health  # returns health value

#     def show_level(self):
#         return self.__level  # returns level value
    
# if __name__ == "__main__":
#     pass  # nothing happens here yet


# add gain() method to increase level
# class Pokemon:
#     def __init__(self, name):
#         self.__n = name
#         self.__health = 100
#         self.__level = 1

#     def intro(self):
#         print(f"{self.__n}, {self.__n}")
    
#     def show_health(self):
#         return self.__health
    
#     def show_level(self):
#         return self.__level
    
#     def gain(self):
#         self.__level += 1  # increases level by +1
    
# if __name__ == "__main__":
#     p1 = Pokemon("Pikachu")
#     p2 = Pokemon("Schiggy")

#     p1.gain()
#     p1.gain()
#     print(p1.show_level())  # 3


# show_level() now prints the info instead of returning
# class Pokemon:
#     def __init__(self, name):
#         self.__n = name
#         self.__health = 100
#         self.__level = 1

#     def intro(self):
#         print(f"{self.__n}, {self.__n}")
    
#     def show_health(self):
#         return self.__health
    
#     def show_level(self):
#         print(f"{self.__n} :: {self.__level}")  # print formatted level info
    
#     def gain(self):
#         self.__level += 1
    
# if __name__ == "__main__":
#     p1 = Pokemon("Pikachu")
#     p2 = Pokemon("Schiggy")

#     p1.gain()
#     p1.gain()
#     p1.show_level()  # Pikachu :: 3
#     p2.show_level()  # Schiggy :: 1


# add attack() method — Pokémon can fight!
# class Pokemon:
#     def __init__(self, name):
#         self.__n = name
#         self.__health = 100
#         self.__level = 1

#     def intro(self):
#         print(f"{self.__n}, {self.__n}")
    
#     def show_health(self):
#         return self.__health
    
#     def show_level(self):
#         print(f"{self.__n} :: {self.__level}")
    
#     def gain(self):
#         self.__level += 1

#     def attack(self, other, damage):
#         other.__health -= damage  # reduces health of the target Pokémon
    
# if __name__ == "__main__":
#     p1 = Pokemon("Pikachu")
#     p2 = Pokemon("Schiggy")
    
#     p1.attack(p2, 10)  # Pikachu attacks Schiggy with 10 damage
#     print(p2.show_health())  # 90




# MAGIC METHODS — internal Python methods that customize behavior of objects

# __str__  → called when printing an object
# __gt__   → called when comparing with '>'
# other examples: __lt__, __eq__, __add__, __len__, etc.


# class Pokemon:
#     def __init__(self, name):
#         self.__n = name
#         self.__health = 100
#         self.__level = 1

#     def __str__(self):
#         return f"Name: {self.__n}\nHealth: {self.__health}\nLevel:{self.__level}"

#     def intro(self):
#         print(f"{self.__n}, {self.__n}")
    
#     def show_health(self):
#         return self.__health
    
#     def show_level(self):
#         print(f"{self.__n} :: {self.__level}")
    
#     def gain(self):
#         self.__level += 1

#     def attack(self, other, damage):
#         other.__health -= damage
    
# if __name__ == "__main__":
#     p1 = Pokemon("Pikatchu")
#     p2 = Pokemon("Schiggy")

#     p1.gain()
#     p2.attack(p1, 28)
#     print(p1)

# Example
# Name: Pikachu
# Health: 72
# Level: 2



# add __gt__ → greater than comparison
# allows: p1 > p2 to compare levels

# class Pokemon:
#     def __init__(self, name):
#         self.__n = name
#         self.__health = 100
#         self.__level = 1

#     def __str__(self):
#         return f"Name: {self.__n}\nHealth: {self.__health}\nLevel: {self.__level}"
    
#     def __gt__(self, other):
#         return self.__level > other.__level  # compare by level

#     def intro(self):
#         print(f"{self.__n}, {self.__n}")
    
#     def show_health(self):
#         return self.__health
    
#     def show_level(self):
#         print(f"{self.__n} :: {self.__level}")
    
#     def gain(self):
#         self.__level += 1

#     def attack(self, other, damage):
#         other.__health -= damage

# if __name__ == "__main__":
#     p1 = Pokemon("Pikachu")
#     p2 = Pokemon("Schiggy")

#     p1.gain()  # Pikachu level 2
#     print(p1 > p2)  # True

