def is_possible(arr,mid,k):
    cow_count = 1
    last_cow = arr[0]

    for i in arr:
        if (i-last_cow) >= mid:
            cow_count += 1
            if cow_count == k:
                return True
            last_cow = i
    
    return False



def aggressive_cows(arr,k):
    max = -1
    arr.sort()
    
    for i in arr:
        if max < i:
            max = i
    
    start = 0
    end = max
    ans = -1

    while(start<=end):
        mid =  int(start + (end-start)/2)
        
        flag = is_possible(arr,mid,k)
        print(start,end,mid,flag)
        
        if flag:
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
    
    return ans

if __name__ == "__main__":
    # arr = [0, 3, 4, 7, 10, 9]
    # k = 4
    
    arr = [4, 2, 1, 3, 6]
    k = 2

    print(aggressive_cows(arr,k))