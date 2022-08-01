# Q3. The denominations in Indian currency are:
# |1, |2, |5, |10, |,20, |50, |100, |200, |500, |2000.
# Given an amount N, print how many coins/notes make up N
# Sample input:
# Enter the amount: 2640
# Output:
# 2000 1
# 500 1
# 100 1
# 10 4
# Also test your program with N=3781, 4928, and 5134


# function to return the number of notes of the given denomination
def countofNote(note, amount):
    return(amount//note)


def splitDenominations():
    amount = int(input("Enter the amount: "))
    denominations = [2000,500,200,100,50,20,10,5,2,1]
    for i in denominations:
        num = countofNote(i, amount)
        if num != 0:
            print(f"{i} {num}")
            amount = amount - (i * num)
            if amount == 0:
                break
        else:
            continue

splitDenominations()


#output:

# Enter the amount: 2640
# 500 1
# 100 1
# 20 2

# Enter the amount: 3781
# 2000 1
# 500 3
# 200 1
# 20 1
# 10 1
# 1 1

# Enter the amount: 4928
# 2000 2
# 500 1
# 20 1
# 5 1
# 2 1
# 1 1

# Enter the amount: 5134
# 2000 2
# 500 2
# 100 1
# 20 1
# 10 1
# 2 2