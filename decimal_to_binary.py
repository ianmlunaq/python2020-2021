# decimal_to_binary.py | imlq

def decimal_to_binary(dec):
    binS = str(bin(dec))
    b = binS.replace('0b', '')
    #print(dec, binValue, b)
    return b

def main():
    print('* Decimal to Binary * * * * * *')
    binString = decimal_to_binary(23)
    print(23, binString)
    binString = decimal_to_binary(245)
    print(245, binString)

main()