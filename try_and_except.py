# ERROR HANDLING (try / except)

# list = [1, 2, 3, "Adem", "Ado", "Adolf"]

# try:
#     index = int(input("please enter index..:" ))
#     print([list[index]])
# except IndexError as ex:
#     print(f"failed..\n{ex}")


# multiple exceptions
# list = [1, 2, 3, "Adem", "Ado", "Adolf"]

# try:
#     index = int(input("please enter index..:" ))
#     print([list[index]])
# except IndexError as ex:
#     print(f"failed..\n{ex}")
# except ValueError:
#     print("please enter a number!")


# general error handling (any type)
# list = [1, 2, 3, "Adem", "Ado", "Adolf"]

# try:
#     index = int(input("please enter index:" ))
#     print([list[index]])
# except Exception:
#     print("something is wrong..")


# general error handling (with error message)
# list = [1, 2, 3, "Adem", "Ado", "Adolf"]

# try:
#     index = int(input("please enter index:" ))
#     print([list[index]])
# except Exception as ex:
#     print(f"something is wrong..\n{ex}")





# FINALLY BLOCK — runs no matter what (error or not)

# list = [1, 2, 3, "Adem", "Ado", "Adolf"]

# try:
#     index = int(input("please enter index:" ))
#     print([list[index]])
# except Exception as ex:
#     print("something is wrong..")   # catches any kind of error
# finally:
#     print("im done!")               # always runs (even after error)


# FILE HANDLING with finally (ensures file is closed)

# try:
#     f = open("test.txt", "w")   # open file for writing
#     f.write("hey!")             # write text to file
# except Exception:
#     pass                        # ignore any error
# finally:
#     f.close()                   # close file even if an error occurs