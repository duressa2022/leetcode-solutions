class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minQueue=deque()
        maxQueue=deque()
        start=maxResult=0
        for end in range(len(nums)):
            #create min queue and max Queue
            while minQueue and minQueue[-1]>nums[end]:
                minQueue.pop()
            minQueue.append(nums[end])
            while maxQueue and maxQueue[-1]<nums[end]:
                maxQueue.pop()
            maxQueue.append(nums[end])
            #check the validity and update in accordance
            while maxQueue[0]-minQueue[0]>limit:
                num=nums[start]
                if num==minQueue[0]:
                    minQueue.popleft()
                if num==maxQueue[0]:
                    maxQueue.popleft()
                start=start+1
            #update the max result of the subarray
            maxResult=max(maxResult,end-start+1)
        return maxResult

            

        