def collatz(number):
    is_even = number % 2
    if is_even == 0:
        res = number // 2
    else:
        res = number * 3 + 1
    print(res)
    return res       

print('please input a number')

try:
    number = int(input())
    while number != 1:
        number = collatz(number)
        print('collatz: ' + str(number))
except ValueError:
    print('please input a integer')


