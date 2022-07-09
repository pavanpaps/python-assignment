n = int(input('Enter number of rows:'))
for i in range(n):
    print(' '*(n-i),end='')
    print(' '.join(str(11**i)))