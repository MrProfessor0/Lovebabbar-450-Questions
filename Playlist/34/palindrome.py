def isPalindrome(string,i,j):
    if i > j:
        return True

    if string[i] != string[j]:
        return False
    else:
        i+=1
        j-=1
        return isPalindrome(string,i,j)
    

s = "A man, a plan, a canal: Panama"
s = "".join(i.lower() for i in s if i.isalnum())

print(isPalindrome(s,0,len(s)-1))
