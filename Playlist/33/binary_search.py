def binary_search(arr,start,end,key):
    # print(start,end)
    if start > end:
        return False

    mid = start + (end-start)//2

    if arr[mid] == key:
        return True

    if key < arr[mid]:
        return binary_search(arr,start,mid-1,key)
    else:
        return binary_search(arr,mid+1,end,key)


# arr = [1,2,3,4,5,6,7,8,9,10]
arr = [6,12,13,14,16,18,20,28,35,42,44,47]
key = 40

print(binary_search(arr=arr,start=0,end=len(arr)-1,key=key))