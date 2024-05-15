def sqrt(n,start,end,ans):
    if start>end:
        return ans
    mid = start + int((end-start)/2)
    square = mid*mid
    if square == n:
        return mid
    if square > n:
        return sqrt(n,start,mid-1,ans)
    else:
        return sqrt(n,mid+1,end,mid)

    

def floorSqrt(n):
    return sqrt(n,0,n,0)

n = 6
print(floorSqrt(n))



# def floorSqrt(n):
#     # write your code logic here .
#     start = 0
#     end = n
#     ans = 0
#     while(start<=end):
#         mid = start + int((end-start)/2)
#         # print(start,mid,end)
#         if (mid*mid) == n:
#             return mid
#         if (mid*mid) >  n:
#             end = mid-1
#         else:
#            ans = mid
#            start = mid+1
        
#     return ans