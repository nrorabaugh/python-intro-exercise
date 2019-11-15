from capitals import states
import random

for s in states:
    s['answered'] = 0
    s['correct'] = 0

score = {
    'correct': 0,
    'incorrect': 0
}

i = 0
while i < 1:
    score['correct'] = 0
    score['incorrect'] = 0
    print('Welcome to the state capital game! When prompted, type the capital of the designated state. \nLet\'s see how well you know your capitals!\n')
    random.shuffle(states)
    for s in states:
        answer=input(f'What is the capital of {s["name"]}?\n')
        if answer == s["capital"]:
            score['correct']  += 1
            s['correct'] += 1
            s['answered'] += 1
            print(f'Congratulations! That is correct. You have {score["correct"]} correct answers and {score["incorrect"]} incorrect answers.\nYou have answered this state correctly {s["correct"]} out of {s["answered"]} tries.\n')
        elif answer != s["capital"]:
            score['incorrect'] += 1
            s['answered'] += 1
            print(f'No, the answer is {s["capital"]}. You have {score["correct"]} correct answers and {score["incorrect"]} incorrect answers.\nYou have answered this state correctly {s["correct"]} out of {s["answered"]} tries.\n')
    print(f'Congratulations on finishing the state capitals game! Your score is {score["correct"]} out of 50.\nWould you like to play again? (Y/N)')
    play_again = input()
    if play_again == 'n' or play_again == 'N':
        i=1
        print('Thanks for playing!')