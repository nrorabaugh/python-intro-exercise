from capitals import states
import random



i = 0
while i < 2:
    random.shuffle(states)
    for s in states:
        answer=input(f'What is the capital of {s["name"]}?\n')
        if answer == s["capital"]:
            print('Congratulations! That is correct.')
        else:
            print(f'No, the answer is {s["capital"]}.')
    i+=1