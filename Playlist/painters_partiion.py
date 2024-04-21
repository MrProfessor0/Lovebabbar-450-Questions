def is_possible(boards,mid,k):
    painter_count = 1
    painter_units = 0

    for i in boards:
        if (painter_units + i) <= mid:
            painter_units += i
        else:
            painter_count += 1
            # print("mid:"+ str(mid)+ " painter_units:"+ str(painter_units) +" painter_count:" + str(painter_count), end="\n\n")
            if (painter_count > k) or (i>mid):
                return False 
            painter_units = i

    return True


def findLargestMinDistance(boards:list, k:int):
    # Write your code here
    # Return an integer
    sum = 0
    for i in boards:
        sum += i

    start = 0
    end = sum
    ans = 0

    while(start<=end):
        mid  = int(start + (end-start)/2)

        flag = is_possible(boards,mid,k)
        print(start,end,mid,flag)

        if flag:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1

    return ans



if __name__ == "__main__":
    arr = [8, 6, 10, 3, 2, 7, 10]
    k = 7
    
    print(findLargestMinDistance(arr,k))