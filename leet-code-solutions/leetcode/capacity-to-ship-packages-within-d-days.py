class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left,right,best=max(weights),sum(weights),1
        while left<=right:
            mid=left+(right-left)//2
            counter=0
            current_day=1
            for i in range(len(weights)):
                counter+=weights[i]
                if counter>mid:
                    current_day+=1
                    counter=weights[i]
            if current_day>days:
                left=mid+1
            else:
                right=mid-1
                best=mid
        return best


        