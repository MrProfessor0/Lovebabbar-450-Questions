def reverseString(string):
    if not string:
        return ""
    
    return string[-1] + reverseString(string[:-1])

print(reverseString("abcde"))