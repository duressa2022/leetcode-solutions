class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        length=len(palindrome)
        palindrome=list(palindrome)
        if length==1:
            return ""
        for start in range(length):
            end=length-1-start
            if start==end:
                continue
            if palindrome[start]!="a":
                palindrome[start]="a"
                return "".join(palindrome)
        palindrome[length-1]="b"
        return "".join(palindrome)

        