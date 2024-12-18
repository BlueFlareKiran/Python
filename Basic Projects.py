color=input("Enter a color: ")
noun=input("Enter a noun: ")
name=input("Enter a name: ")
                              #Basic Mad_LIbs
print("Roses are "+color)
print(noun+" are blue")
print("I love "+name)
# from Getting_Started import Question

print("This is a Basic Calculater")
a=float(input("Enter a number: "))
op=input("Enter a operator: ")
b=float(input("Enter a number: "))

if op=="+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op=="*":               #Basic Calculater
    print(a*b)
elif op=="/":
    print(a/b)
else:
    print("Invalid Operator")

secret_word = "giraffe"
guess = ""
guess_count = 0
max_guesses = 3                         #Basic Word Guess Game

while guess != secret_word and guess_count < max_guesses:
    guess = input("This is an animal with the largest neck. Try to guess: ")
    guess_count += 1
    if guess == secret_word:
        print("You guessed it right, You Win!")
        break
    elif guess_count == max_guesses:
        print("You failed. The correct answer was 'giraffe'. Try again next time!")
        break
    else:
        print("Wrong guess. Try again.")


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            translation += "k"               #translate vowels into k
        else:
            translation += letter
    print(translation)

phrase = input("Enter a phrase: ")
translate(phrase)

emp=open("Employees.txt","a")
print(emp.readable())
print(emp.read())
emp.write("Toby - Data Scientist")      #Basic File Operations
print(emp.readiness())
emp.close()

from Getting_Started import Student

student1=Student("kiran","Software",6.32, False)
print(student1.gpa)
student2=Student("kiran","Software",8.32, False)
print(student1.on_honor_roll())
print(student2.gpa)
print(student2.on_honor_roll())

from Getting_Started import Question

question_prompts = [
    "What is the capital of France?\n (a) Berlin\n (b) Madrid\n (c) Paris\n (d) Rome",
    "Which programming language is known as the backbone of web development?\n (a) Python\n (b) JavaScript\n (c) C++\n (d) Ruby",
    "Who painted the Mona Lisa?\n (a) Vincent van Gogh\n (b) Leonardo da Vinci\n (c) Pablo Picasso\n (d) Michelangelo",
    "What is the largest planet in our solar system?\n (a) Earth\n (b) Mars\n (c) Jupiter\n (d) Saturn",
    "Which element has the chemical symbol 'O'?\n (a) Oxygen\n (b) Osmium\n (c) Gold\n (d) Hydrogen"
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "c"),
    Question(question_prompts[4], "a")
]


def run_test(questions):
    score=0
    for question in questions:
        answer=input(question.prompt+"\n")
        if answer==question.answer:
            score+=1
    print("You got "+str(score)+"/"+str(len(questions))+" Correct")

run_test(questions)

