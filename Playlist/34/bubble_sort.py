def bubble_sort(arr):
    length = len(arr)-1
    # print(length)

    for i in range(0,length):
        for j in range(0,length-i):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
        # print(arr)

    # print("\n\n\n")
    return arr

def recursive_bubble_sort(arr,n):
    # print(arr,n)
    if n < 1:
        return arr

    for i in range(n):
        if arr[i] > arr[i+1]:
            temp = arr[i+1]
            arr[i+1] = arr[i]
            arr[i] = temp

    return recursive_bubble_sort(arr,n-1)


# arr = [9,8,7,6,5,4,3,2,1,0]
arr = [2,1]
print(arr,end="\n\n")
print(bubble_sort(arr))
print(recursive_bubble_sort(arr,len(arr)-1))