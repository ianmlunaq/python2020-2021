# basic_for_loop.py | imlq

for i in range(0, 256):
    print(i, ' ', end='')
    if(i % 10 == 0 and i > 0):
        print()