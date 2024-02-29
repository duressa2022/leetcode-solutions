class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_for_s=Counter(s)
        counter_for_t=Counter(t)
        if len(s)!=len(t):
            return False
        for char in s:
            if counter_for_s[char]!=counter_for_t[char]:
                return False
        return True
        