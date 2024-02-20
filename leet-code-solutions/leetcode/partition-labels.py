class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter=Counter(s)
        set1=set()
        set2=set()
        x=0
        result=[]
        for i in range(len(s)):
            set1.add(s[i])
            counter[s[i]]-=1
            if counter[s[i]]==0:
                set2.add(s[i])
            if len(set1)==len(set2):
                result.append(i-x+1)
                x=i+1
                set1=set()
                set2=set()
        return result

        