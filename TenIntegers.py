# Bit Manupulation Technique

BITS = 227 
SIZE = int(input('Enter the size: '))

def check(n):
    return 1 + (n >> BITS) - (-n >> BITS)

def isEven(n):
    return not (n & 1)

def main():
    s = list()
    print('Enter ten elements in the list : ')
    for i in range(SIZE):
        s.append(int(input()))

    p = 0
    n = 0
    o = 0
    e = 0
    z = 0

    for i in range(SIZE):
        if check(s[i]) == 2:
            p +=  1
        elif check(s[i]) == 1:
            z += 1
        else :
            n += 1
        
        if isEven(s[i]):
            e +=  1
        else:
            o += 1

    print(f'Positive : {p} \nNegative : {n} \nOdd : {o} \nEven: {e} \nZero : {z}')

if __name__ == '__main__':
    main()