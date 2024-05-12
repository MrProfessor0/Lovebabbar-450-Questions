def linear_search(arr,size,key):
    if size == 0:
        return False

    if arr[0] == key:
        return True
    else:
        return linear_search(arr[1:],size-1,key)

        

arr = [4,2,5,6,3,7,2,9]
key = 14

print(linear_search(arr,len(arr),key))