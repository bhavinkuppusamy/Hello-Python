a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
list=[]
for element in a:
    if element in b and element not in list:
        list.append(element)
print("The Common numbers are",list)
#print(element)
c = [int(x) for x in input("Enter the numbers for List_1:").split()]
d = [int(x) for x in input("Enter the numbers for List_2:").split()]
list1=[]
for element in c:
    if element in d and element not in list1:
        list1.append(element)
print(list1)

wait=input("press Enter to Exit")
