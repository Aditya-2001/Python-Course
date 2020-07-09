def funct(x):
    sum=0
    for i in x:
        sum+=int(i)
    print(sum)

listt=input("Enter elements: ").split(" ")
funct(listt)