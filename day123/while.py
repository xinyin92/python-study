#name = ''
#while name != 'your name':
#    print('Please type your name')
#    name = input()
#print('Thank you!')

#while True:
#    print('Please type your name')
#    name = input()
#    if name == 'your name':
#        break
#print('Thank you')

while True:
    print('who are you')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe.  What is your password?')
    password = input()
    if password == 'swordfish':
        break
print('Acess granted')
