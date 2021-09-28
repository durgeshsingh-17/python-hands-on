for i in range(5):
    for j in range(5):
        if(j == 2 or i == 4) or (i == 1 and j == 0):
            print('*', end = '')
        else:
            print(end = ' ')
    print(end = '\n')

        
