class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter=Counter(arr)
        values=sorted([counter[key] for key in counter])
        left,right=0,1
        while right<len(values):
            if values[left]==values[right]:
                return False
            left=left+1
            right=right+1
        return True
        