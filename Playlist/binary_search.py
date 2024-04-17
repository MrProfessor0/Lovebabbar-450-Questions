from array import array

def binary_search(arr:array,size:int,key:int) -> int:
    start = int(0)
    end = int(size-1)

    mid = int((start+end)/2)

    while(start <= end):
        # print(mid)
        # print(start,end)
        if arr[mid] == key:
            return mid
        if arr[mid] < key:
            start = mid + 1
        if arr[mid] > key:
            end = mid - 1
        mid = int((start+end)/2)
    return -1

if __name__ == '__main__':
    even = array("i",[2,4,6,8,12,18])
    key = 18
    index = binary_search(even,len(even),key)
    print(f"index of {key} is " + str(index))

    odd = array("i",[3,8,11,14,16])
    key = 20
    index = binary_search(odd,len(odd),key)
    print(f"index of {key} is " + str(index))
