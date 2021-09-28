num = int(input("enter the number"))
p = 1
for i in range(1, num+1):
    for j in  range(1, num+1):
        print(p, end=" ")
        p += 1
    print('\n')
