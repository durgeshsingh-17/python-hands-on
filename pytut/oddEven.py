a = input('Enter the number: ')
special_symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
while(a):
    if(a == 'q'):
        break
    if(a.isalpha() or (a in special_symbol)):
        print('enter valid input')
    else:
        if(int(a) % 2 == 0):
            print('Even Number')
        else:
            print('Odd Number')
    b=input("do you want to continue?(y/n)")
    if(b=="n"):
        break
    a = input('Enter the number: ')
        
