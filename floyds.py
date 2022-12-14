# Q4. The following is called Floyd’s triangle:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11
# · · ·
# 12 13 14 15
# Given a positive integer N, write a program that prints N rows of Floyd’s
# triangle, with the rows properly aligned

def floyds():
    n=int(input("Enter the nmber of rows: "))
    num=1
    for i in range(n):
        print('row', i+1, end=':  ')
        for j in range(i+1):        
            print(num, end = '\t')
            num = num + 1
        print()
floyds()

# output
# Enter the nmber of rows: 8
# row 1:  1
# row 2:  2       3
# row 3:  4       5       6
# row 4:  7       8       9       10
# row 5:  11      12      13      14      15
# row 6:  16      17      18      19      20      21
# row 7:  22      23      24      25      26      27      28
# row 8:  29      30      31      32      33      34      35      36