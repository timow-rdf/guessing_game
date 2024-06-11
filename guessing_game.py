# guessing game v1.0
# guessing game v2.0

import random

number = random.randint(1, 100)
print(f'DEBUG: The number is {number}')

guess_correct = False

count_attempts = 0

while not guess_correct:
    try:
        guess = int(input('Guess a number between 1 and 100: '))

        if guess < 1 or guess > 100:
            raise ValueError

        count_attempts += 1

        if number == guess:
            print(f'Congratulation, your guess {guess} is correct. Score: {count_attempts}')
            guess_correct = True
        elif number < guess:
            print(f'The number you are looking for is smaller than your guess {guess}!')
        elif number > guess:
            print(f'The number you are looking for is greater than your guess {guess}!')

    except ValueError:
        print('Wrong Input!')
