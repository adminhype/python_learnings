# Arithmetic Operators (Grundrechenarten)


# print(30 / 15) #2.0, normal division (returns float)

# print(30 // 15) #2, floor division (no decimals)
# print(7 // 2) #3, floor division rounds down
# print(5 // 8) #0, result below 1 becomes 0

# print(42 % 12) #6, remainder of division
# print(5 % 4) #1, remainder
# print(10 % 3) #1, remainder
# print(10 % 2) #0, no remainder

# print(2**1) #2, power of 1
# print(2**2) #4, power of 2
# print(2**3) #8, power of 3
# print(2**4) #16, power of 4
# print(2**5) #32, power of 5
# print(2**6) #64, power of 6
# print(2**7) #128, power of 7
# print(2**8) #256, power of 8
# print(2**9) #512, power of 9
# print(2**10) #1024, power of 10

# print(2 + 5 * 3) #17, multiplication before addition

# print(10 / 2 + 5) #10.0, division first then addition
# print(5 + 10 / 2) #10.0, same result (order by precedence)


# Combined Arithmetic Examples
# 5**3 + 2 #127
# 4 + 3 -5 #2
# 6 + 8 / 2 #10.0
# 10 * 2 ** 3 #80
# 5 * 9 * 2 / 10 #9.0
# 5 % 3 * 7 #14
# 6 % 5 + 3 #4
# 10 % 2**2 #2

# Mixed Operations & Precedence
# 12 * 12 = 144
# 2.5 + 3.5 = 6.0
# 20 / 5 = 4.0
# 15 - 3 * 5 = 0
# 8 + 10//4 = 10
# 8 + 10/4 = 10.5
# 20 / (5 - 4 ) = 20.0
# 4 * 2.5 / 4 = 2.5
# 1//2 - 3//4 = 0
# (12 % 5) * (5 % 12) = 10
# 2**3 = 8
# 4**(8 - 5) = 64
# 2**(8 // 2) = 16
# 5**2 * 3 = 75
# (8 - 5)**(27//9) = 27
# "apfel" + "baum" = apfelbaum
# 5 * ("a"+ "b") = ababababab
# "x" * 2**3 = xxxxxxxx
# 12 % 5 = 2
# 42 % 43 = 42
# 2**10 % 2 = 0
# 5 * 4 * 3 * 2 * 1.0 = 120.0
# 0 * "Adem" = ""
# "xyz" * (12 % 5 ) = xyzxyz


# Increment/Decrement examples
# i = 0
# # i++  # invalid in Python, use i += 1 instead
# # i++  # invalid, same reason
# # i--  # invalid, use i -= 1


# # Assignment operators
# # += adds and assigns
# # -= subtracts and assigns

# i = 0
# i += 1  # 1, increases by 1
# i += 2  # 3, adds 2 (1 + 2)
# i += 5  # 8, adds 5 (3 + 5)

# i -= 1  # 7, subtracts 1 (8 - 1)
# i -= 2  # 5, subtracts 2 (7 - 2)
# i -= 5  # 0, subtracts 5 (5 - 5)

# i = 5
# i /= 2  # 2.5, divides and assigns (float result)
# i //= 2  # 1.0, floor divides and assigns (integer-like result)

# a = 5
# a **= 2  # 25

# b = 10
# b %= 3  # 1, takes remainder and assigns (10 mod 3)

# Comparison Operators
# print(2 < 3) #True, 2 is smaller than 3
# print(2 > 3) #False, 2 is not greater than 3

# a = 2
# b = 3
# print(a < b) #True, 2 is smaller than 3
# print(a <= b) #True, 2 is smaller or equal to 3
# print(a >= b) #False, 2 is not greater or equal to 3

# a = "adem"
# b = "Hamburg"
# print(a == b) #False, strings are not equal
# print(a < b) #False, lowercase 'a' > uppercase 'H' in ASCII order
# print(a != b) #True, strings are different


# Bitwise / XOR Encryption Example
# 10101   <- cleartext
# 11011   <- key

# XOR encryption
# 01110   <- ciphertext
# 11011   <- same key again

# XOR decryption
# 10101   <- cleartext


# Logical Operators (and, or, not, xor)
# print(2 < 3 and 3 < 5) #True, both conditions are True
# print(2 < 3 and 3 == 5) #False, second condition is False

# print(2 < 3 or 3 == 5) #True, at least one condition is True
# print(2 < 3 or 3 != 5) #True, first and second are True

# print((2 < 3) ^ (3 != 5)) #False, both True -> XOR gives False
# print((2 < 3) ^ (3 == 5)) #True, one True one False -> XOR gives True

# print(True or 2 < 3 and False) #True, and runs first -> True or False = True
# print(True and 2 < 3 and False) #False, all must be True but last is False
# print((True or 2 < 3) and False) #False, parentheses first -> True and False = False

# print(not(True or 2 < 3 and False)) #False, not reverses True -> False
# print(not False) #True, not flips False to True
# print(True and not False) #True, True and True


# True and False and True or False        #False
# not False or not True                   #True
# True and (False or not False)           #True
# not(not False ^ True or not False)      #False
# True and False ^ True and False         #False


# Logical Expressions with Explanations
# print(2 < 3 and not 2 > 5) 
# # True:
# # 2 < 3 → True  
# # 2 > 5 → False  
# # not False → True  
# # True and True → True

# print(not True ^ False or 3 == 2 + 1)
# # True:
# # not True → False  
# # False ^ False → False (both same)  
# # 3 == 2 + 1 → True  
# # False or True → True

# print(not not not 2 % 5 == 7 % 5)
# # False:
# # 2 % 5 = 2
# # 7 % 5 = 2 → so (2 % 5 == 7 % 5) → True  
# # not True → False  
# # not False → True  
# # not True → False → False

# print(True and False ^ True and False)
# # False:
# # ^ has higher precedence than AND  
# # False ^ True → True  
# # So: True and True and False  
# # → (True and True) → True  
# # True and False → False

# print(True ^ False ^ 0 ^ 1 ^ (2 > 3))
# # 0 means False, 1 means True  
# # step by step:
# # 1 ^ 0 = 1
# # 1 ^ 0 = 1
# # 1 ^ 1 = 0
# # 0 ^ 0 = 0
# # Result: 0


# a = 2.5
# b = -5
# c = 20
# d = "Hello"
# e = "Python"

# d + " " + e                     # Hello Python
# c % 7                           # 6
# 16**(a - 2)                     # 4.0
# d**c                            # TypeError
# (b + c) / b                     # -3.0
# 20**2(2 * a + b)                # 1.0
# 2 * a * d                       # TypeError
# (c - b) // 7                    # 3
# e // "Python"                   # TypeError
# b**2 - 25                       # 0
# True or False ^ True            # True
# 0 > 1 and True ^ True           #False