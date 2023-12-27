class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        can_capacity=capacity
        steps=0
        i=-1
        while i<len(plants)-1:
            i+=1
            if capacity>=plants[i]:
                capacity=capacity-plants[i]
                steps+=1
            else:
                steps+=(i+1)+i
                capacity=can_capacity
                capacity=capacity-plants[i]
        return steps
        