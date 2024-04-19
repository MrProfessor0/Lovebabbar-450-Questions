def pivot_element(arr:list) -> int:
    s = 0
    e = len(arr) - 1

    while(s<e):
        mid = (s+e)//2
        if arr[mid] >= arr[0]:
            s = mid + 1
        else:
            e = mid
    
    return s

if __name__ == "__main__":
    arr = [3,8,10,17,1]
    print(pivot_element(arr))
