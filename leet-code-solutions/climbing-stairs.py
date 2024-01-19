class Solution:
    def climbStairs(self, n,memo={}) -> int:
        if n in memo:
            return memo[n]
        if n==0 or n==1:
            return 1
        memo[n]=self.climbStairs(n-1)+self.climbStairs(n-2)
        return memo[n]
        