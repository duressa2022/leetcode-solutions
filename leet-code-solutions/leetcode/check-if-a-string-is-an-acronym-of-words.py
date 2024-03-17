class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        temp=[]
        for word in words:
            temp.append(word[0])
        return s=="".join(temp)
        