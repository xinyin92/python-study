import random
print('I am thinking of a number between 1 and 20')
count = 0
ran = random.randint(1, 21)
while True:
    count = count + 1
    print('take a guess')
    guess = int(input())
    if guess > ran:
        print('your guess is too large')
    elif guess < ran:
        print('your guess is too low')
    else:
        print('good job, your guessed my number in ' + str(count) + ' guesses')
        break
    
