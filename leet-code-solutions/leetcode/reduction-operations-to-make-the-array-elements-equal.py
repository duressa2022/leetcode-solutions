class Solution:
  def reductionOperations(self, nums: List[int]) -> int:
    #create result var
    result = 0
    #sort the list
    nums.sort()
    #move throgh out the list
    for i in range(len(nums) - 1, 0, -1):
        #make comparison
      if nums[i] != nums[i - 1]:
        #update the result
        result += len(nums) - i
    #return the result
    return result
        

        