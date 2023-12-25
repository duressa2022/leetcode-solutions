class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        ranges=sorted(ranges)
        for u,v in ranges:
            if u<=left and left<=v:
                left=v+1
        return left>right

        