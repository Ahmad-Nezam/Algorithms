def flex(num1 , num2 ,num3,num4):
    current = num2

    while current <= num3:
        if current % num1 == 0 and current != num4:
            print(current)
        current += 1

flex(2 , 4 , 6 , 8) 