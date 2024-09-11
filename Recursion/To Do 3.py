def Rbinary_search(arr , value , left = 0 , right = None):
    if right is None:
        right = len(arr) - 1

    if left > right:
        return False
    mid = (left + right) // 2

    if arr[mid] == value:
        return True
    elif value < arr[mid]:
        return Rbinary_search(arr , value , left , mid -1 )
    else:
        return Rbinary_search(arr , value , mid + 1 ,right)
    
result = Rbinary_search([1,2,3,5],3)
print(result)  

# Greatest Common Factor

def rGCF(a, b):
   
    if b == 0:
        return a
  
    return rGCF(b, a % b)


print(rGCF(123456, 987654)) 
