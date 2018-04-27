# spam = ['apples', 'bananas', 'tofu', 'cats']
# def foo(list):
#     loop = len(list)
#     res = ''
#     for i in range(loop):
#         if i < loop - 1:
#             res += list[i] + ', '
#         else:
#             res += 'and ' + list[i]
#     return res

# print(foo(spam))

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']];
res = ''
x = len(grid)
y = len(grid[0])
for i in range(y):
    for j in range(x):
        res += grid[j][i]
    res += '\n'
print(res)