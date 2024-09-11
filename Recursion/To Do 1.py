# Recursive Sigma
def recersion_sum(n):
    if n<=1:
        return n 
    else:
        return n+recersion_sum(n-1)
    
num = 5

if num < 0:
    print('enter a positive value :')
else:
    print('the sum is : ',recersion_sum(num))


# Recursive Factorial

def recersion_fact(n):
    if n<=1:
        return n 
    else:
        return n*recersion_sum(n-1)
    
num = 3

if num < 0:
    print('enter a positive value :')
else:
    print('the factorial is : ',recersion_sum(num))