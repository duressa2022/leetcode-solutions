class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        list=[0 for i in s]
        for i,val in enumerate(indices):
            list[val]=s[i]
        return "".join(list)
