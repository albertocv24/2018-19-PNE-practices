#Create a function called sum(n), which calculates the sum of the n first integers and returns the result.

def sum(n):
    total = 0
    for i in range(n):
        total = total + i + 1

    return total

num = int(input("Please introduce n: "))
print("The total number sum is :", sum(num))