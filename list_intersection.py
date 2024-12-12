#function to find intersection
def intersection(list1, list2):
    set0 = set(list1).intersection(set(list2))
    list0 = list(set0)
    return list0

#Given list
list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 3, 4, 2]

#calling function
intersection = intersection(list1, list2)

#Output
print("First list =",list1)
print("Second list =",list2)
print("The intersection of the lists =",intersection)
