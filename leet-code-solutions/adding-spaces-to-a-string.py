class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        map={spaces[i]:i for i in range(len(spaces))}
        result=""
        for i in range(len(s)):
            if i in map:
                result=result+" "
            result+=s[i]
        return result

        