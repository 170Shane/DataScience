import configparser, argparse

def collatz(num):

    if num % 2 == 0:
        return num // 2
    else:
        return (3 * num) + 1

try:
    result = collatz(int(input('Enter a number : ')))
    print(result)
    while result != 1:
        result = collatz(result)
        print(result)
except ValueError as e:
    print('Only numeric values are allowed')


results = 5
print('1', results)
del results
# print('2', results)



list = [1,2,3,4,5,6,7,8,9,10]
print(list.index('3'))