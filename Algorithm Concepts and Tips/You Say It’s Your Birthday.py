def check_birthday(n1 , n2):
    month = 2
    day = 5
    if(n1 == month and n2 == day ) or (n1 == day and n2 == month):
        print('How did you know?')
    else:
        print('Just another day....')

check_birthday(5,2)
check_birthday(4,1)