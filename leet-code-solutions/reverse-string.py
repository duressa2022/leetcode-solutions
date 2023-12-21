class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        low=0
        high=len(s)-1
        while low<high:
            (s[low],s[high])=(s[high],s[low])
            low=low+1
            high=high-1
        