class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        left,right=0,0
        result=""
        while left<len(word1) and right<len(word2):
            if word1[left]>word2[right]:
                result+=word1[left]
                left=left+1
            else:
                if word1[left]==word2[right]:
                    if word1[left:]>word2[right:]:
                        result+=word1[left]
                        left=left+1
                    else:
                        result+=word2[right]
                        right=right+1
                else:
                    result+=word2[right]
                    right=right+1
        if left<len(word1):
            result+=word1[left:]
        if right<len(word2):
            result+=word2[right:]
        return result
