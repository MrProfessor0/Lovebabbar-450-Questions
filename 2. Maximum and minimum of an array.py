from array import array

# finding min_max thorugh linear search
def min_max(arr:array)->int:
    min = 0
    max = 0

    for i in arr:
        if min > i:
            min = i
        if max < i:
            max = i
    
    return min,max

# other ways through like sorting

if __name__ == '__main__':
    arr = array("i",[1,2,3,4,5])
    min,max = min_max(arr)
    print(f"min: {min}, max= {max}")