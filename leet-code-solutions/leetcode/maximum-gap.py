class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:return 0
        length=len(nums)
        nums=self.bucketSort(nums,length)
        result=0
        left,right=0,1
        while right<length:
            result=max(result,nums[right]-nums[left])
            left=left+1
            right=right+1
        return result
    def insertionSort(self,array):
        if len(array)<1:
            return []
        if max(array)-min(array)==0:
            return array
        length=len(array)
        for i in range(length):
            for j in range(i,0,-1):
                if array[j-1]>array[j]:
                    (array[j-1],array[j])=(array[j],array[j-1])
        return array
    def bucketSort(self,array,length):
        buckets=[[]for i in range(length)]
        maxValue=max(array)
        minValue=min(array)
        ranValue=maxValue-minValue
        result=[]
        if ranValue==0:
            return array
        for num in array:
            index=(num-minValue)/(ranValue/(length-1))
            index=int(index)
            buckets[index].append(num)
        for i in range(length):
            buckets[i]=self.insertionSort(buckets[i])
        for i in range(length):
            result.extend(buckets[i])
        return result

        