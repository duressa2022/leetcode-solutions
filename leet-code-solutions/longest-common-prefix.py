class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLength=float("inf")
        for string in strs:
            minLength=min(minLength,len(string))
        testString=strs[0]
        result=""
        for i in range(minLength):
            for j in range(1,len(strs)):
                if testString[i]!=strs[j][i]:
                    return result
            result+=testString[i]
        return result
        