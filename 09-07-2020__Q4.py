#- Calculate the number of upper / lower case letters in a string
# sample_string = "Hey I AM doing Good IN PROGRamming"


# def funct(x):
#     lower=0
#     upper=0
#     for i in x:
#         if ord(i)<=122 and ord(i)>=97 :
#             lower+=1
#         else:
#             upper+=1
#     print("Total upper case letters are: ",upper)
#     print("Total lower case letters are: ",lower)

# listt=input("Enter string of a-z and A-Z characters only: ")
# funct(listt)

def string_test(s):
    d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    for c in s:
        if c.isupper():
            d["UPPER_CASE"] += 1
        elif c.islower():
            d["LOWER_CASE"] += 1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["UPPER_CASE"])
    print("No. of Lower case Characters : ", d["LOWER_CASE"])


string_test('The quick Brown Fox')
