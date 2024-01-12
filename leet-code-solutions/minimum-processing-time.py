class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse=True)
        tasks.sort()
        partition=len(tasks)//len(processorTime)
        index=0
        result=[]
        right=partition
        while index<len(processorTime):
            result.append(processorTime[index]+tasks[right-1])
            right+=partition
            index=index+1
        return max(result)


        