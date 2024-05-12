def arr_sum(arr,size):
    if size == 0:
        return 0

    if size == 1:
        return arr[0]
    
    sum = arr[0] + arr_sum(arr[1:],size-1)

    return sum



arr = [1,2,3,4,5]
# arr = [1]
print(arr_sum(arr,len(arr)))