def selection_sort(arr):
    n = len(arr)
    # print(n)

    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if arr[min] > arr[j]:
                min = j
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp

    print("\n\n")
    return arr
        

def recursive_selection_sort(arr,i,n):
    print(i,n,arr)
    if i >= n-1:
        return arr
    min = i
    for j in range(i+1,n):
        if arr[min] > arr[j]:
            min = j
    temp = arr[i]
    # print(temp,min)
    arr[i] = arr[min]
    arr[min] = temp

    return recursive_selection_sort(arr,i+1,n)

    


arr = [9,8,7,6,5,4,3,2,1,0]
# print(arr,end="\n\n")
# print(selection_sort(arr))
print(recursive_selection_sort(arr,0,len(arr)))