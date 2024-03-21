class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter=Counter(nums)
        freqHolder=[]
        for value,freq in counter.items():
            freqHolder.append((freq,value))
        length=len(freqHolder)
        freqHolder=self.bucketSort(freqHolder,length)
        result=[]
        for i in range(length-1,length-k-1,-1):
            result.append(freqHolder[i][1])
        return result

    def insertionSort(self,bucket):
        length=len(bucket)
        for i in range(length):
            for j in range(i,0,-1):
                if bucket[i-1][0]>bucket[i][0]:
                    (bucket[i],bucket[i-1])=(bucket[i-1],bucket[i])
        return bucket
    def bucketSort(self,array,length):
        buckets=[[] for i in range(length)]
        maxValue=-float("inf")
        minValue=float("inf")
        result=[]
        for freq,value in array:
            maxValue=max(maxValue,freq)
            minValue=min(minValue,freq)
        ranValue=maxValue-minValue
        if ranValue==0:
            return array
        for freq,value in array:
            index=(freq-minValue)/(ranValue/(length-1))
            index=int(index)
            buckets[index].append((freq,value))
        for i in range(length):
            buckets[i]=self.insertionSort(buckets[i])
        for bucket in buckets:
            result.extend(bucket)
        return result
        
        
       