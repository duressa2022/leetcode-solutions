class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        left,right,length=0,0,len(word)
        ls_string=list(word)
        if ch not in word:
            return word
        while right<length:
            if ls_string[right]==ch:
                break
            right=right+1
        while left<=right:
            (ls_string[left],ls_string[right])=(ls_string[right],ls_string[left])
            left=left+1
            right=right-1
        return "".join(ls_string)
        