# fonction de base 10 en base 16
n=int(input('Quelle nombre en décimal voulez vous son équivalent en hexadécimal'))

def hexaDigits (n: int)->str:

    if n<10 :
        return str(n)
    elif n== 10 :
        return 'A'
    elif n== 11 :
        return 'B'
    elif n== 12 :
        return 'C'
    elif n== 13 :
        return 'D'
    elif n== 14 :
        return 'E'
    elif n== 15 :
        return 'F'
    else:
        print('?')
print(hexaDigits(n))

#

def fillBits (n: int)->int:
    n = str(n)
    L = len(n)
    while L%4 != 0:
        n = '0' + n
        L = len(n)
    return n
print (fillBits(n))

#Fonction décimal a binaire

n = int(input('Entrez un nombre entier en décimal'))
def dec2Bin (n:int)->int:
    R = ''
    while n != 0:
        R = R + str(n%2)
        n = n//2
    return R
print(dec2Bin(n))

#


