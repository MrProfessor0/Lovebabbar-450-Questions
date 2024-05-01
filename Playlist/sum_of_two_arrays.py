def findArraySum(a, n, b, m):
    # Write your code here.
    ans = []
    i = n-1
    j = m-1
    carry = 0

    while(i>=0 and j>=0):
        sum = 0
        val1 = a[i]
        val2 = b[j]
        sum = val1+val2+carry
        carry = sum//10
        sum = sum%10
        ans.append(sum)
        i -= 1
        j -= 1

    while(i>=0):
        sum = 0
        val1 = a[i]
        sum = val1+carry
        carry = 0
        carry=sum//10
        sum=sum%10
        ans.append(sum)
        i -= 1

    while(j>=0):
        sum = 0
        val1 = b[j]
        sum = val1+carry
        carry=sum//10
        sum=sum%10
        ans.append(sum)
        j -= 1    

    if carry != 0:
        ans.append(carry)

    return ans[::-1]

# 1240

a = [1,2,3,4]
n = 4
b = [6]
m = 1

a = [9,9,9]
n = 3
b = [9,9,9]
m = 3

print(findArraySum(a,n,b,m))