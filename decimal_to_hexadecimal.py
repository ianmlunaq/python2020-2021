# decimal_to_hexadecimal.py | Ian Luna

def decToHex(dec):
    hex_str_0 = str(hex(dec))
    hex_str_1 = hex_str_0.replace('0x', '').upper()
    return(hex_str_1)

def main():
    print('DECIMAL TO HEXADECIMAL CONVERSION')
    hexadecimal = decToHex(10)
    print(10, hexadecimal)
    hexadecimal = decToHex(256)
    print(256, hexadecimal)


main()
