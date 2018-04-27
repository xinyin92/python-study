#print('hello', end=' ')
#print('world')
def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)
