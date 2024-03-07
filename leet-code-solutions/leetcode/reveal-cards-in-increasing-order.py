class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        queue=deque()
        for val in deck:
            if queue:
                queue.appendleft(queue.pop())
            queue.appendleft(val)
        return list(queue)
        