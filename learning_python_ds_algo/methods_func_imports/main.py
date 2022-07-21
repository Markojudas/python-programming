# Built-in functions
# len(), type(), id() (functions)
# upper(), lower(),  strip(), find() (methods)

# import string  # imports ALL of string module
# importing only the constant ascii_lowercase from string
from string import ascii_lowercase

greeting = "Hello"
user = "Jose"
message = "Welcome to the algorithms course"

print(greeting, user, message)  # Hello Jose Welcome to the algorithms course

print(len(greeting))  # 5
print(len(user))  # 4
print(len(message))  # 32 including white spaces

print(type(message))  # <class 'str'>
print(type(greeting))  # <class 'str'>

# everything in python is an object

print(id(user))  # the id of the object = CPython returns the object's mem address

print(greeting.upper(), user.lower())

message2 = "      welcome       to the course"
print(message.strip())  # strips unnecessary white space

print(message.split())  # returns a list of string, default delim is white space

message3 = "welcome-to-the-course"

print(message3.split("-"))  # delim = "-"

my_languages = ['Python', 'Go', 'Java']

print("".join(my_languages))  # PythonGoJava
print(" ".join(my_languages))  # Python Go Java

print(ascii_lowercase)  # no need to specify the module
