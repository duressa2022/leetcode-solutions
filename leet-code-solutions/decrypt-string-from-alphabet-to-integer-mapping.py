class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        string="abcdefghijklmnopqrstuvwxyz"
        hash_map={str(i+1):char for i,char in enumerate(list(string))}
        i=len(s)-1
        result=""
        while i>=0:
            if s[i]=="#":
                result=hash_map[s[i-2:i]]+result
                i=i-3
            else:
                result=hash_map[s[i]]+result
                i=i-1
        return result



       

        