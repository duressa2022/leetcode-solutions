class Solution:
    def frequencySort(self, s: str) -> str:
        counter=Counter(s)
        charHolder=[]
        for char,freq in counter.items():
            charHolder.append((freq,char))
        length=len(charHolder)
        charHolder=self.bucketSort(charHolder,length)
        result=[] 
        for freq,char in reversed(charHolder):
            result.append(char*freq)
        return "".join(result)
        
    def insertionSort(self,bucket):
        length=len(bucket)
        for i in range(length):
            for j in range(i,0,-1):
                (freq1,char1)=bucket[i-1]
                (freq2,char2)=bucket[i]
                if freq1>freq2:
                    (bucket[i],bucket[i-1])=(bucket[i-1],bucket[i])
        return bucket
                    
    def bucketSort(self,array,length):
        buckets=[[] for i in range(length)]
        maxValue=-float("inf")
        minValue=float("inf")
        result=[]
        for freq,char in array:
            maxValue=max(maxValue,freq)
            minValue=min(minValue,freq)
        ranValue=maxValue-minValue
        if ranValue==0:
            return array
        for freq,char in array:
            index=(freq-minValue)/ranValue/(length-1)
            index=int(index)
            buckets[index].append((freq,char))
        for i in range(length):
            buckets[index]=self.insertionSort(buckets[index])
        for bucket in buckets:
            result.extend(bucket)
        return result
        


        