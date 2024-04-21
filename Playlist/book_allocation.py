
def is_possible(arr:list[int], mid:int, m:int):
    student_count = 1
    page_count = 0

    for i in arr:
        if (page_count+i) <= mid:
            page_count += i
        else:
            student_count += 1
            if (student_count > m) or (i>mid):
                return False
            page_count = i

    return True


def allocate_books(arr:list[int], m:int):
    sum = 0
    for i in arr:
        sum += i

    start = 0
    end = sum
    ans = -1

    while(start<=end):
        mid = int(start + (end-start)/2)

        flag = is_possible(arr, mid, m)
        print(start,end,mid,flag)

        if flag:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1

    return ans


if __name__ == '__main__':
    arr = [2, 8, 8, 4, 5]
    m = 6
    print("ans:  " + str(allocate_books(arr,m)))

