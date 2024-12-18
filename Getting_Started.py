from math import *

print("Hello world")
name = "kiran"
print(name + str(5))
a = 56
print(pow(a, 10))
gmail = "@gmail.com"
fullname = input("Enter your fullname ")
print(fullname + name + str(a) + gmail)

from fileinput import close

# lists in python
lucky = [2, 5, 6, 7, 9]
friends = ["kiran", "raghu", "rakesh", "sudheer", "arun"]
friends2 = friends.copy()
friends.extend(lucky)
print(friends[1:4])
friends.append("rajesh")
friends.insert(1, "harry")
friends.remove("kiran")
friends.clear()
friends.pop()
print(friends.index("kiran"))
print(friends2)
print(friends)

# tuples are immutable
unchange = (5, 6, 7, 8)
print(unchange)

def sayhi():
    print("hello world")   # functions

sayhi()

def cube(a):
    return a * a * a    # return values

print(cube(5))

if 1 and not 0:
    print('kiran')
elif 1 or 0:
    print('babu')    # if statements
else:
    print('kiran')

def greater3(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print(greater3(33, 2, 3))

month_dict = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",           # Dictionary
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
print(month_dict["Aug"])
# print(month_dict["Bug"])  # This would throw an error since "Bug" is not a key
print(month_dict.get("bug"))
print(month_dict.get("bug", "not available"))

i = 1
while i <= 10:
    print(i)
    i += 1

for letter in "kiranbabukiran":
    print(letter)

for friend in friends:
    print(friend)

for i in range(3, 10):
    print(i)

for i in range(len(friends)):
    print(friends[i])

def power(base, power):
    result = 1
    for i in range(power):
        result = result * base      # Exponent Function
    return result

print(power(3, 3))

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],           # 2D Lists
    [0]
]

print(grid[0][2])

for row in grid:
    for col in row:
        print(col)

try:
    age = int(input("enter your age: "))        # exception
except ValueError:
    print("Invalid input")

class Student:
    def __init__(self, name, major, gpa, is_present):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_present = is_present

    def on_honor_roll(self):
        if self.gpa >= 8.0:
            return True
        else:
            return False

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
