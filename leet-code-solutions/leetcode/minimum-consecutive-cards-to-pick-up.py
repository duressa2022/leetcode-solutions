class Solution:
    def minimumCardPickup(self,cards):
        last_index = {}
        min_distance = float('inf')
        for i, card in enumerate(cards):
            if card in last_index:
                min_distance = min(min_distance, i - last_index[card])
            last_index[card] = i

        return min_distance+1 if min_distance != float('inf') else -1

        