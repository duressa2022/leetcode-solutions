class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left,right=0,len(s1)
        baseCounter=Counter(s1)
        while right<len(s2)+1:
            subString=s2[left:right]
            counter=Counter(subString)
            if self.isEqualCounter(counter,baseCounter):
                return True
            left=left+1
            right=right+1
        return False
    def isEqualCounter(self,counter1,counter2):
        for key in counter1:
            if counter1[key]!=counter2[key]:
                return False
        return True






        