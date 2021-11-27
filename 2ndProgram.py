import random

def userInput():
    firstNumber = random.randrange(0, 100)
    secondNumber = random.randrange(0, 100)
    answer = int(input(f'{firstNumber} + {secondNumber} = '))
    return firstNumber, secondNumber, answer

def checkAnswer(answer, solution):
    count = 0
    if answer == solution:
        count = count + 1
        print('Correct! Nice Job!')
        return count
    else:
        print('Wrong Answer. Try Again.')
        return count

print('Test your knowledge with Addition Trainer!')
print('Please enter your answer on the following quesions:')

numberOfProblems = 10
for i in range(numberOfProblems):
    firstN, secondN, userAnswer = userInput()
    solution = firstN + secondN
    count = 0
    score = checkAnswer(userAnswer, solution)

print(f'Your total score is {score}/10.')