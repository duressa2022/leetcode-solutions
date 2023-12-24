class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_map={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        result=0
        prev=0
        for i in range(len(s)):
            if hash_map[s[i]]<=prev:
                result+=hash_map[s[i]]
            else:
                result+=hash_map[s[i]]-2*prev
            prev=hash_map[s[i]]
        return result


        