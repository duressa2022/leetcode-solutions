class Solution:
    def reverseWords(self, s: str) -> str:
        list_word=s.split()
        result=[]
        for word in list_word:
            result.append(self.revString(word))
        return " ".join(result)

    def revString(self,string):
        ls_Character=list(string)
        left=0
        right=len(string)-1
        while left<right:
            (ls_Character[left],ls_Character[right])=(ls_Character[right],ls_Character[left])
            left=left+1
            right=right-1
        return "".join(ls_Character)


        