import csv
with open("file.scv","w") as csv_file:
    field_names=['name','age','roll_number']
    writer=csv.DictWriter(csv_file,fieldnames=field_names)
    writer.writeheader()
    x=int(input("Enter number of users: "))
    for i in range(0,x):
        name=input("Enter name: ")
        age=int(input("Enter age: "))
        roll_number=int(input("Enter roll number: "))
        writer.writerow({'name':name, 'age':age, 'roll_number':roll_number })

import csv
with open("file.scv","r") as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',')
    count=0
    for row in csv_reader:
        if count==0:
            print(f'Column names are {", ".join(row)}')
        elif count%2==0:
            print(f'Name is {row[0]}, Age is {row[1]}, Roll Number is {row[2]}')
        count+=1