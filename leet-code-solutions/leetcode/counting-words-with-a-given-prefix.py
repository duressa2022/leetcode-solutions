class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        counter=0
        for word in words:
            if len(pref)<=len(word) and pref==word[:len(pref)]:
                counter+=1
        return counter
        