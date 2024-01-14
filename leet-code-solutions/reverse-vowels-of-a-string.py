class Solution:
    def reverseVowels(self, s: str) -> str:
        ls_string=list(s)
        hash_set={"a","A","e","E","i","I","o","O","u","U"}
        left=0
        right=len(s)-1
        while left<right:
            if ls_string[left] in hash_set and ls_string[right] in hash_set:
                (ls_string[left],ls_string[right])=(ls_string[right],ls_string[left])
                left=left+1
                right=right-1
            elif ls_string[left] in hash_set and ls_string[right] not in hash_set:
                right=right-1
            elif ls_string[left] not in hash_set and ls_string[right] in hash_set:
                left=left+1
            else:
                right=right-1
                left=left+1
        return "".join(ls_string)
        