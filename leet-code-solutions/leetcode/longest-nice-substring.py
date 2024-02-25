class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        result=""
        longest=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                tempString=s[i:j+1]
                if self.isNiceString(tempString):
                    if longest<j-i+1:
                        result=tempString
                        longest=j-i+1
        return result
        
    def isNiceString(self,string):
        for char in string:
            if char.islower():
                if char.upper() not in string:
                    return False
            if char.isupper():
                if char.lower() not in string:
                    return False
        return True
                    

        