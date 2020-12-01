# variables_demo.py | imlq

i1 = 33
i2 = 48
i3 = 65
i4 = i3 + 25
i5 = 97

print('Integers')
print(i1,i2,i3,i4,i5)
print()

c1 = chr(i1)
c2 = chr(i2)
c3 = chr(i3)
c4 = chr(i4)
c5 = chr(i5)

print('Characters')
print(c1,c2,c3,c4,c5)
print()

sum = i1 + i2 + i3 + i4 + i5
print('Sum: ', sum)
print(type(sum))
print()

concat = c1 + c2 + c3 + c4 + c5
print('This is now a string: ', concat)
print(type(concat))