A = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list=[]
number=int(input("Enter the number: "))
for i in A:
    if(i < number):
        new_list.append(i)
print(new_list)

input("Press ENTER to close the window")

