arr = []
listHere = (input('enter the number in the list'))
special_symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
while(listHere):
    if(listHere == 'q'):
        break
    if(listHere.isalpha() or (listHere in special_symbol)):
        print('enter valid number')
    else:
        for i in range(1, int(listHere)+1):
            if(int(listHere) >= 0):
                num = (input())
                arr.append(num)
                print('here entered list is: \n', arr)
    b = input('do you want to continue?(y/n)')
    if(b == 'n'):
        break
    listHere = (input('enter the number in the list'))
