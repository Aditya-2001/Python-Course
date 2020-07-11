#Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.

#65,91 for A-Z
for x in range(65,92):
    c=chr(x)
    file=open(c,"w")
    file.close()