# guessing game v4.0

import random

def play():
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
    return count_attempts

def save_score(count_attempts):
    file = "Scores.txt"
    nickname = input("\nEnter nickname: ")
    with open(file, 'a') as w:
        w.write(f"\n{nickname}: {count_attempts} Attempts")
    pass

while True:
    highscore = play()

    save_score(highscore)

    correctUserInput = False

    while not correctUserInput:
        prompt = input('Do you want to play again? [Yes/No] ')

        if prompt == 'Yes':
            correctUserInput = True
        elif prompt == 'No':
            exit()
        else:
            print('Wrong Input! Only \'Yes\' or \'No\'')
