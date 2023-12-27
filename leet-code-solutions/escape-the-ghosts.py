class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        distance=abs(target[0])+abs(target[1])
        for i in ghosts:
            _computed=abs(i[0]-target[0])+abs(i[1]-target[1])
            if _computed<=distance:
                return False
        return True
        