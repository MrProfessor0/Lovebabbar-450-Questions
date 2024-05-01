class Solution:
    
    #Function to find the maximum occurring character in a string.
    def getMaxOccurringChar(self,s):
        #code here
        count = [0] * 26
        max = -1
        char = 'z'
        
        for i in s:
            count[ord(i.lower())-ord('a')] = count[ord(i.lower())-ord('a')] + 1

        print(count)
        max = -1
        ans = -1
        for i in range(0,26):
            if count[i] > max:
                ans = i
                max = count[i]

        print(chr(ord('a')+ans))

        
                



str = "testsample"

s = Solution()
s.getMaxOccurringChar(str)