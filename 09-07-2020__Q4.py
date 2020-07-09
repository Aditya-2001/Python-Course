def funct(x):
    lower=0
    upper=0
    for i in x:
        if ord(i)<=122 and ord(i)>=97 :
            lower+=1
        else:
            upper+=1
    print("Total upper case letters are: ",upper)
    print("Total lower case letters are: ",lower)

listt=input("Enter string of a-z and A-Z characters only: ")
funct(listt)