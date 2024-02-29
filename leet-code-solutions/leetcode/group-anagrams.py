class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram={}
        for word in strs:
            temp="".join(sorted(word))
            if temp not in anagram:
                anagram[temp]=[word]
            else:
                anagram[temp].append(word)
        return [anagram[key] for key in anagram]


    def isAnagram(word1,word2):
        counter1=Counter(word1)
        counter2=Counter(word2)
        if len(word1)!=len(word2):
            return False
        for char in word1:
            if counter1[char]!=counter[char]:
                return False
        return True
        