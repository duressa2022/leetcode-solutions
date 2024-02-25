class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter=defaultdict(int)
        left=result=0
        for right in range(len(s)):
            counter[s[right]]+=1
            while right-left+1-max(counter.values())>k:
                counter[s[left]]-=1
                left=left+1
            result=max(result,right-left+1)
        return result
            

        