class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter1=defaultdict(int)
        counter2=Counter(t)
        left,length=0,len(s)+1
        result=""
        for right in range(len(s)):
            counter1[s[right]]+=1
            while self.checkCounters(counter1,counter2):
                if length>right-left+1:
                    length=right-left+1
                    result=s[left:right+1]
                counter1[s[left]]-=1
                if counter1[s[left]]==0:
                    del counter1[s[left]]
                left=left+1
        return result

    def checkCounters(self,counter1,counter2):
        for key,value in counter2.items():
            if counter1[key]<value:
                return False
        return True

