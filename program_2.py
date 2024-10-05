# Title: Math Quiz
# Author: Andrew Bittner
# Date: 10/4/2024
from random import random, randint


# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247

# + 129

# ------

# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.


# Initialize variables
# QUESTIONS_COUNT = 5
num1 = 25
num2 = 7

# Define math problem generator function
# def math_quiz():
#     global num1
#     global num2
#     global operation
#     num1 = random.randint(1, 5)
#     num2 = 2
#     operation = random.randint(1, 4)
#     if operation == 1:
#         result = num1 + num2
#     elif operation == 2:
#         result = num1 - num2
#     elif operation == 3:
#         result = num1 * num2
#     else:
#         result = num1 / num2
#     return result

# Define type conversion function
def convert_typ(inp, outp_typ):
    inp = float(inp)
    while not type(inp) == outp_typ:
        if type(outp_typ) == int:
            inp = int(inp)
        elif type(outp_typ) == float:
            inp = float(inp)
        else:
            inp = str(inp)
    return inp

# Define input validation function
def validate_inp(inp, inp_typ, outp_typ, err_msg = 'Invalid input entered.', inp_msg = 'Please re-enter your answer: '):
    while not type(inp) == outp_typ:
        try:
            inp = float(inp)
            inp = convert_typ(inp, float)
        except:
            print(err_msg)
            inp = (input(inp_msg))
    return inp

# for q in range(QUESTIONS_COUNT):
#     answer = math_quiz()
#     question = input(f'What is {num1} {operation} {num2}? ')
answer = input(f"What is {num1} * {num2}? ")
if answer == num1 * num2:
    print(f'That\'s correct!')
else: print(f'Sorry, that\'s not correct.')