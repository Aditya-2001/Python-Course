#-Write a Python program to count the number of lines in a text file.

#since it is not important that all those access this code must have same named text file so we will create it and then operate
file=open("A","a")
while True:
    string=input("Enter the text: ")
    file.write(string)
    file.write("\n")
    print("If want another line then press y else any key")
    text=input()
    if text!='y':
        break
file.close()
file=open("sample_file","r")
ans=0
for each in file:
    ans+=1
print("total lines are ",ans)
file.close()