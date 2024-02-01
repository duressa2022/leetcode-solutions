class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        left,right=0,0
        result=[]
        while left<len(firstList) and right<len(secondList):
            left1,right1=firstList[left]
            left2,right2=secondList[right]
            if max(left1,left2)<=min(right1,right2):
                result.append([max(left1,left2),min(right1,right2)])
            if right1<right2:
                left=left+1
            else:
                right=right+1
        return result

        