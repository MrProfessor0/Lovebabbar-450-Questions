from array import array

# Array Reverse Using an Extra Array
def reverse_using_extra_array(arr:array,size:int)->array:
    # Using array lib
    reverse_array = array("i",[0]*size)
    for i in range(0,size):
        reverse_array[size-1-i] = arr[i]
    return reverse_array

    # using list
    # reverse_list = array[::-1]


# Array Reverse Using a Loop (In-place)
def reverse_using_a_loop(arr:array,size:int)->array:
    start = 0
    end = size-1
    while(start<end):
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1
    return arr


# Array Reverse Recursion
def reverse_using_recursion(arr:array,start:int,end:int)->array:
    if start > end:
        return arr
    arr[start],arr[end] = arr[end],arr[start]
    
    return reverse_using_recursion(arr,start+1,end-1)
    

if __name__ == '__main__':
    arr = array("i",[1, 2, 3, 4, 5, 6])
    # arr = reverse_using_extra_array(arr,len(arr))
    # arr = reverse_using_a_loop(arr,len(arr))
    arr = reverse_using_recursion(arr,0,end=len(arr)-1)

    print(f"Reveresed array: {arr}")
