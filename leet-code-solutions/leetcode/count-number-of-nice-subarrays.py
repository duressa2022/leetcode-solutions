class Solution:
    def numberOfSubarrays(self,nums, k):
        count = 0
        odd_count = 0
        prefix_counts = {0: 1}

        for num in nums:
            if num % 2 == 1:
                odd_count += 1
            if odd_count - k in prefix_counts:
                count += prefix_counts[odd_count - k]
            prefix_counts[odd_count] = prefix_counts.get(odd_count, 0) + 1
        return count



        

