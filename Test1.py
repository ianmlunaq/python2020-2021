import random

def buildArray(arr, a):
    for i in range(a):
        rand = random.randint(10, 99)
        arr.append(rand)

def sumArray(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum

def main():
    appendingArr = []
    print('How many values to add to the array:')
    appending = int(input())
    buildArray(appendingArr, appending)
    print(appendingArr)
    sum = sumArray(appendingArr)
    print('Total ', sum)

main()