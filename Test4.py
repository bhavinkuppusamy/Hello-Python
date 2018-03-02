num=int(input("Enter the Number to check: "))
list=range(2,num)
divisorlist=[1,num]
flag=0
for element in list: 
    divisor = num%element
    if divisor == 0:
        flag=1
        divisorlist.append(element) 
print (divisorlist)
A=len(divisorlist)
print("The Number of Divisors are :", A)
if flag == 0:
    print(num,"is a prime number")
