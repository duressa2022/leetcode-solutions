class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        counter=0
        for word in words:
            if self.isAllowed(allowed,word):
                counter+=1
        return counter
    def isAllowed(self,word1,word2):
        set1=set(list(word1))
        for char in word2:
            if char not in set1:
                return False
        return True
        