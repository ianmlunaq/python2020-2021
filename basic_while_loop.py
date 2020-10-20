# basic_while_loop.py | Ian Luna

count = 0
divisor = 11
while(count < 1001):
    if(count % divisor == 0):
        print(count)
    else:
        print(count, end=' ')
    count = count + 1
