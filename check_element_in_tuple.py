#Given tuple
my_tuple = (1,2,3,4,5,6,7,8,9,10)

#Element to check
print("Tuple =",my_tuple)
element = int(input("Enter element to search : "))

#Check if element exists in the tuple
if element in my_tuple:
    print(element,"exists in the tuple")
else:
    print(element,"does not exist in the tuple")
