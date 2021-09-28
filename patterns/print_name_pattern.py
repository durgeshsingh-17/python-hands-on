arr = 'Durgesh'
l = list(arr)
l.reverse()
for i in range(len(l)):
    for j in range(i+1):
        print(l[j], end=' ')
    print('\n')


arr = 'Durgesh'
for i in range(len(arr)):
    for j in range(i+1):
        print(arr[j], end=' ')
    print('\n')
