from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target=Counter(p)
        left,right=0,len(p)-1
        result=[]
        while right<len(s):
            if self.checkAnagram(p,s[left:right+1]):
                result.append(left)
            left=left+1
            right=right+1
        return result
    def checkAnagram(self,string1,string2):
        counterString1=Counter(string1)
        counterString2=Counter(string2)
        for key in counterString1:
            if counterString1[key]!=counterString2[key]:
                return False
        return True

            


        