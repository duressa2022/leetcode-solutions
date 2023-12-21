class Solution:
    def largestGoodInteger(self, num: str) -> str:
        data=["999","888","777","666","555","444","333","222","111","000"]
        for val in data:
            if val in num:
                return val
        return ""

        