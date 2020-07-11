#- WAP to Square and cube every number in a given list of integers using Lambda
# Sample List : [1,2,3,4,5,6]

listt=input("Enter list: ").split(" ")
final_list_square=list(map(lambda x: int(x)**2,listt))
print("Square are: ",final_list_square)
final_list_cube=list(map(lambda x: int(x)**3,listt))
print("Cube are: ",final_list_cube)