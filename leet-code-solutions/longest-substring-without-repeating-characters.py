class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map={}
        left,right=0,0
        longest=0
        if len(s)==1:return 1
        while right<len(s):
            if s[right] not in hash_map:
                hash_map[s[right]]=right
            else:
                left=max(left,hash_map[s[right]]+1)
                hash_map[s[right]]=right
            longest=max(longest,right-left+1)
            right=right+1
        return longest


        