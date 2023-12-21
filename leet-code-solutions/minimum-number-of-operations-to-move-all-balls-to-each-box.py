class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result=[]
        for i in range(len(boxes)):
            counter=0
            for j in range(len(boxes)):
                if i!=j and boxes[j]!="0":
                    counter+=abs(j-i)
            result.append(counter)
        return result
    
        