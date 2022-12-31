def encrypt(str):
    for i in range(len(str)):
        if (str[i] == 'z'):
            str[i] = 'a'
        elif (str[i] == 'ç'):
            str[i] = 'd'
        elif (str[i] == 'ə'):
            str[i] = 'f'
        elif (str[i] == 'ğ'):
            str[i] = 'h'
        elif (str[i] == 'ö'):
            str[i] = 'p'
        elif (str[i] == 'ş'):
            str[i] = 't'
        elif (str[i] == 'ü'):
            str[i] = 'v'
        else:
            str[i] = chr(ord(str[i]) + 1)

    return ''.join(str)

str = "Fərid Pashayev"
print(encrypt(list(str)))
