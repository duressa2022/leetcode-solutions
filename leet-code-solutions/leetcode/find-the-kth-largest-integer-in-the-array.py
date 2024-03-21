class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        length=len(nums)-1
        result=[]
        for num in nums:
            result.append(int(num))
        def solver(array,left,right,k):
            if left==right:
                return array[left]
            index=self.helperFunction(array,left,right)
            if k-1==index:
                return array[index]
            else:
                if k-1>index:
                    return solver(array,index+1,right,k)
                else:
                    return solver(array,left,index-1,k)
        return str(solver(result,0,length,k))

    def helperFunction(self,array,left,right):
        index=random.randint(left,right)
        (array[index],array[right])=(array[right],array[index])
        pivot=array[right]
        holder=left-1
        for seeker in range(left,right):
            if array[seeker]>pivot:
                holder+=1
                (array[seeker],array[holder])=(array[holder],array[seeker])
        (array[holder+1],array[right])=(array[right],array[holder+1])
        return holder+1
        