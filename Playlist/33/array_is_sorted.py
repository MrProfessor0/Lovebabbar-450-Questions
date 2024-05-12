def is_sorted(arr,size):
    if size == 0 or size == 1:
        return True

    if arr[0] > arr [1]:
        return False
    else:
        ans = is_sorted(arr[1:],size-1)
        return ans




arr = [2,4,6,9,11,13,1]

print(is_sorted(arr,len(arr)))