number=int(input("Enter the Number: "))

divided=number%2

if divided==0:
    if number%4==0:
        print(str(number) + " is multiple of 4")
    else:
        print(str(number) + " is Even")
elif divided==1:
    print(str(number)+ " is Odd")
else:
    print(str(number), "is not known")

num=int(input("Enter the Number: "))
check=int(input("Enter the Divide: "))
if num%check==0:
    print(str(num) + " is divisibe by "+ str(check))
else:
    print(str(num) + " is not divisibe by "+ str(check))
input("Press ENTER to close the window")
