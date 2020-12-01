#asc2.py imlq
# Change the range from (0,35) to (32,???)
for i in range (32, 128):
    c = chr(i)
    print("[",i,"=",c,"]",end="")
    if (i % 10 == 0):
        print("\n")