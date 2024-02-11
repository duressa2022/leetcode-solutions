class Solution:
    def maxScore(self,cardPoints, k):
        total_points = sum(cardPoints)
        n = len(cardPoints)
        window_size = n - k
        
        min_window_sum = float('inf')
        current_window_sum = 0
        
        for i in range(window_size):
            current_window_sum += cardPoints[i]
        
        min_window_sum = min(min_window_sum, current_window_sum)
        for i in range(window_size, n):
            current_window_sum += cardPoints[i] - cardPoints[i - window_size]
            min_window_sum = min(min_window_sum, current_window_sum)
        return total_points - min_window_sum

        