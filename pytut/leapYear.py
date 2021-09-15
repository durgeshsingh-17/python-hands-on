year = input('Enter the year')
special_symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
while(year):
    if(year == 'a'):
        break
    if(year.isalpha() or (year in special_symbol)):
        print('enter valid input')
    else:
        if(((int(year) % 4 == 0) and not(int(year) % 100 == 0)) or (int(year) % 400 == 0)):
            print('Leap Year')
        else:
            print('Not leap year')
    b=input("do you want to continue?(y/n)")
    if(b=="n"):
        break
    year = input('Enter the year')
    
    
    
