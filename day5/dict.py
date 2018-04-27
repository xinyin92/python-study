# myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
# print(myCat)
# myCat2 = {'color': 'gray', 'disposition': 'loud', 'size': 'fat'}
# print(myCat == myCat2)
# print(myCat.keys())
# print(myCat.values())
# print(myCat.items())
# import pprint
# message = 'it was a bright cold day in april, and the clocks were striking thirteen'
# count = {}
# for char in message:
#     count.setdefault(char, 0)
#     count[char] = count[char] + 1

# print(count) 
# pprint.pprint(count)
# format = pprint.pformat(count)
# print(format)

the_board = {
    'top_l': ' ', 'top_m': ' ', 'top_r': ' ',
    'mid_l': ' ', 'mid_m': ' ', 'mid_r': ' ',
    'low_l': ' ', 'low_m': ' ', 'low_r': ' '
}

def printBoard(board):
    print(board['top_l'] + '|' + board['top_m'] + '|' + board['top_r'])
    print('-+-+-')
    print(board['mid_l'] + '|' + board['mid_m'] + '|' + board['mid_r'])
    print('-+-+-')
    print(board['low_l'] + '|' + board['low_m'] + '|' + board['low_r'])
turn = 'X'
for i in range(9):
    printBoard(the_board)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    the_board[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    
    