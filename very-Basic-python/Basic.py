# Python memory unlocking, Very Basic python

# Hello world
print("Hello world")

# Variables and data types
var1 = 1  # Int
var2 = 1.3  # float
var3 = "PythonE"  # string

# List, Tuple, Dictionary, Sets

list1 = [1, 2, 3, 4, 5]
list2 = ["John Smith", "Mundane mann", "Cid", "Shadow"]
tuple1 = (6, 7, 8, 9, 10)
tuple2 = ("Ben Affleck", "Christian Bale", "Robert Pattinson", "Micheal Keaton")
dict1 = {
    12: "twelve",
    13: "thirteen",
    14: "fourteen"
}
set1 = {"Eminem", 11, 5.4, 80085}

# If, else, elif
if 1 in list1:
    print(list1)
elif 6 in list1:
    print(list1)
else:
    print("There is no 1 in list1")
# Loops
for actor in tuple2:
    print(f'{actor} is Batman')
lim = 0
list3 = []
while lim < 10:
    lim = lim + 1
    list3.append(lim)
print(list3)
# Calculator, user input
# print("two-dimensional basic calculator")
# a = int(input("value of a:"))
# b = int(input("value of b:"))
# operation = str(input("Choose operation: + , - , * , / :"))
#
# if operation == "+":
#     ans = a + b
#     print(f'{a} + {b} = {ans} ')
# elif operation == "-":
#     ans = a - b
#     print(f'{a} - {b} = {ans} ')
# elif operation == "*":
#     ans = a * b
#     print(f'{a} * {b} = {ans} ')
# elif operation == "/":
#     ans = a / b
#     print(f'{a} / {b} = {ans} ')
# else:
#     print("something is wrong, I can feel it")

# Guess the number, combining skills, lol

number = 7
guess = 0
attempts = 0

while attempts < 3:
    guess = int(input("Guess the number:"))
    if number == guess:
        print("Congrats, you win!")
        break
    elif number < guess:
        print("Too much, bruh")
        attempts += 1
        if attempts == 3:
            again = (input("You lost."
                           "if yes, type 'yes'"
                           "if no, type 'no'"
                           "Try again? :"))
            if again == "yes":
                attempts = 0
            elif again == "no":
                break
            else:
                print("something is wrong, I can feel it")
    elif number > guess:
        print("Too less, bruh")
        attempts += 1
        if attempts == 3:
            again = (input("You lost."
                           "if yes, type 'yes'"
                           "if no, type 'no'"
                           "Try again? :"))
            if again == "yes":
                attempts = 0
            elif again == "no":
                break
            else:
                print("something is wrong, I can feel it")
