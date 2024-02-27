class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter=Counter(s)
        set1=set()
        set2=set()
        left=0
        result=[]
        for right in range(len(s)):
            set1.add(s[right])
            counter[s[right]]-=1
            if counter[s[right]]==0:
                set2.add(s[right])
            if len(set1)==len(set2):
                result.append(right-left+1)
                left=right+1
        return result
                

        