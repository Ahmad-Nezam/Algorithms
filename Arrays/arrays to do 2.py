# reverse
def reverse(arr):
    left = 0 
    right = len(arr) - 1
    while left < right:
        arr[left] , arr[right] = arr[right] , arr[left] 
        left+=1     
        right-=1
    return arr

print(reverse([1,2,3,4,5]))

# rotate

def reverse_segment(arr, start, end):
   
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotateArr(arr, shiftBy):
    n = len(arr)
    
    if n == 0:
        return arr
    
    shiftBy = shiftBy % n
    
    if shiftBy < 0:
        shiftBy += n
  
    reverse_segment(arr, 0, n - 1)
    
    reverse_segment(arr, 0, shiftBy - 1)
    
    reverse_segment(arr, shiftBy, n - 1)
    
    return arr

print(rotateArr([1, 2, 3], 1))   
print(rotateArr([1, 2, 3, 4, 5], 2))  

# filter

def filter(arr, min_val, max_val):
    valid_index = 0 
    
    for i in range(len(arr)):
    
        if min_val <= arr[i] <= max_val:
            arr[valid_index] = arr[i]
            valid_index += 1
    
    while len(arr) > valid_index:
        arr.pop()  
    return arr

print(filter([1, 3, 5, 7, 9], 3, 7))  
print(filter([10, 20, 30, 40, 50], 15, 35))  

# concat
def concat(arr1 , arr2):
    new_array = []
    
    for i in arr1:
        new_array.append(i)
    for i in arr2:
        new_array.append(i)
    return new_array

print(concat(['ahmad','nezam'] , [1,2,3])) 
print(concat(['salah','aamer'] , [100,200,300]))  