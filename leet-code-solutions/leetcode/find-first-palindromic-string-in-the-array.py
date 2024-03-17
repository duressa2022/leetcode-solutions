class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.iscorrect(word):
                return word
        return ""
    def iscorrect(self,string):
        left,right=0,len(string)-1
        while left<=right:
            if string[left]!=string[right]:
                return False
            left=left+1
            right=right-1
        return True

        