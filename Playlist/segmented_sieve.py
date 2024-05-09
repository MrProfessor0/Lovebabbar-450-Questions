import math
def count_primes(n: int):
    prime_nums = []
    if n<2:
        return prime_nums

    count = 1
    prime = [True] * (n+1)
    prime[0] = prime[1] = False

    for i in range(2,n+1):
        if prime[i]:
            count += 1
            prime_nums.append(i)
            for j in range(i*2,n,i):
                prime[j] = False

    return prime_nums

def segmented_sieve(l:int,r:int)->int:
    sqrt = int(math.sqrt(r))

    prime = count_primes(sqrt)

    dummy = [True] * (r-l+1)

    for prime in prime:

        for j in range(max(l,prime*prime),r+1,prime):
            dummy[j-l] = False

    for i in range(len(dummy)):
        if dummy[i]:
            if l+i<2:
                continue
            print(l+i,end=" ")
    print()

segmented_sieve(l=0,r=1000)

# 3 4 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 