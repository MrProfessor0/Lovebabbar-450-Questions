def power(a,b):
    print(a,b)
    if b == 0:
        return 1

    if b == 1:
        return a
    
    # Recursive call
    ans = power(a,int(b/2))

    if b&1:
        return a * ans * ans
    else:
        return ans * ans



print(power(2,10))