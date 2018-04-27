import random
def getAnswer(num):
    if num == 1:
        return 'certain'
    elif num == 2:
        return 'decidedly'
    elif num == 3:
        return 'yes'
    elif num == 4:
        return 'hazy try again'
    elif num == 5:
        return 'ask again later'
    elif num == 6:
        return 'concentrate and ask again'
    elif num == 7:
        return 'no'
    elif num == 8:
        return 'not good'
    elif num == 9:
        return 'doubtful'

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)
