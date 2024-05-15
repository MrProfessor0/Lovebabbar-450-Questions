def reverseString(string):
    if not string:
        return
    
    return string[-1] + reverseString()

print(reverseString("abcde"))