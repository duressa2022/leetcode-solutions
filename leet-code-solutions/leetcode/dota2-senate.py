class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant=deque()
        dire=deque()
        length=len(senate)
        for index,value in enumerate(senate):
            if value=="R":
                radiant.append(index)
            else:
                dire.append(index)
        while radiant and dire:
            if radiant[0]<dire[0]:
                radiant.append(radiant[0]+length)
            else:
                dire.append(dire[0]+length)
            radiant.popleft()
            dire.popleft()
        return "Radiant" if radiant else "Dire"
        