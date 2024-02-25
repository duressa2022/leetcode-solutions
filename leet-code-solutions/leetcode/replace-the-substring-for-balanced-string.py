class Solution:
    def balancedString(self, s: str) -> int:
        counter=Counter(s)
        length=len(s)
        n=length//4
        balanced=self.checkBalanced(counter,n)
        if balanced:
            return 0
        result,left=len(s),0
        for right in range(length):
            counter[s[right]]-=1
            while left<=right and self.checkBalanced(counter,n):
                result=min(result,right-left+1)
                counter[s[left]]+=1
                left=left+1
        return result


    def checkBalanced(self,counter,n):
        for key in counter:
            if counter[key]>n:
                return False
        return True
        