class Solution:
    def predictTheWinner(self, nums,score1=0,score2=0) -> bool:
        def helperFunction(left,right,score1,score2,isPlayer1):
            if left>right:
                if score1>=score2:
                    return True
                else:
                    return False
            else:
                if isPlayer1==True:
                    leftResult=helperFunction(left+1,right,score1+nums[left],score2,False)
                    rightResult=helperFunction(left,right-1,score1+nums[right],score2,False)
                    return leftResult or rightResult
                else:
                    leftResult=helperFunction(left+1,right,score1,score2+nums[left],True)
                    rightResult=helperFunction(left,right-1,score1,score2+nums[right],True)
                    return leftResult and rightResult
        return helperFunction(0,len(nums)-1,0,0,True)
                    
        

        