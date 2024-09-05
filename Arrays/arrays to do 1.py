# push in front
def push(arr , val):
    arr.insert(0,val)
    return arr

print(push([5,7,2,3],8)) 
print(push([550],7))

# pop from front 
def pop(arr):
    if len(arr) == 0:
        return None
    first_value = arr[0]
    for i in range(1,len(arr)):
        arr[i-1] = arr[i]
    arr.pop()
    print(arr)
    return first_value

print(pop([1,2,3])) 

# insert 
def insert_at(arr , index , val):
    arr.append(val)
    for i in range(len(arr)-1 , index , -1):
        arr[i] = arr[i-1]
    arr[index] = val 
    return arr
    
print(insert_at([100,200,300],1,311)) 