import random

def userInput():
    firstNumber = random.randrange(0, 100)
    secondNumber = random.randrange(0, 100)
    answer = int(input(f'{firstNumber} + {secondNumber} = '))
    return firstNumber, secondNumber, answer

print('Test your knowledge with Addition Trainer!')
print('Please enter your answer on the following quesions:')

numberOfProblems = 10
count = 0

for i in range(numberOfProblems):
    firstN, secondN, userAnswer = userInput()
    solution = firstN + secondN
    if userAnswer == solution:
        count = count + 1
        print('Correct! Nice Job!')
    else:
        print('Wrong Answer. Try Again.')

print(f'Your total score is {count}/10.')