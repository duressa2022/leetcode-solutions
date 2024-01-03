class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString=""
        for char in s:
            if char.isalnum():
                newString+=char.lower()
        left=0
        right=len(newString)-1
        while left<=right:
            if newString[left]!=newString[right]:
                return False
            left=left+1
            right=right-1
        return True
        