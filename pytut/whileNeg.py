n = 1
x = 0
while(n > 0):
    num1 = int(input("enter the number:"))
    x = x + num1
    num2 = input("do you want to continue?(y/n)")
    if(num2 == "n"):
        n = 0
print("the sum is :", x)
