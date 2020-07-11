#-Find the sum of all the numbers in a list using functions.

def funct(x):
    sum=0
    for i in x:
        sum+=int(i)
    print(sum)

listt=input("Enter elements: ").split(" ")
funct(listt)