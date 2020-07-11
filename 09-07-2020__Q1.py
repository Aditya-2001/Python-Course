#-Write a Python function that takes a list and returns a new list with unique elements of the first list.
#Sample List : [1,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]

def funct(x):
    print(list(sorted(set(listt))))


listt = input("Enter elements: ").split(" ")
funct(listt)

# i added this comment
