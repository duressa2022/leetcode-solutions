class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        set_word=set(words)
        counter=0
        for word in  words:
            set_word.remove(word)
            if word[::-1] in set_word:
                counter+=1

        return counter
        