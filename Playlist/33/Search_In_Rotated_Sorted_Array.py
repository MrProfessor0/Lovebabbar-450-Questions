def peak_index(arr,start,end):
    if start>=end:
        return start

    mid = start+int((end-start)/2)
    
    if arr[mid] >= arr[0]:
        return peak_index(arr,mid+1,end)
    else:
        return peak_index(arr,start,mid)

def binary_search(arr,start,end,k):
    if start>end:
        return -1
    
    mid = start + int((end-start)/2)
    print(start,mid,end)

    if arr[mid] == k:
        return mid
    if arr[mid] < k:
        return binary_search(arr,mid+1,end,k)
    if arr[mid] > k:
        return binary_search(arr,start,mid-1,k)

def firstAndLastPosition(arr, n, k):
    # Write your code here

    index = peak_index(arr,0,n-1)
    # print("index: ",end="  ")
    print(index)
    if arr[index]<=k and k <= arr[n-1]:
        print(True)
        return binary_search(arr,index,n-1,k)
        # return binary_search(arr,0,index,k)
    else:
        return binary_search(arr,0,index-1,k)


# arr = [2, 3, 5, 8]
# n = 4
# k = 3

# arr = [5, 6, 7, 8, 9, 10, 0, 2, 3]
# n = 9
# k = 7

arr = [11, 13, 5, 8, 9, 10] 
n = 6
k = 5
print(firstAndLastPosition(arr,n,k))