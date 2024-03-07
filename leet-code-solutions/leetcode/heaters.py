class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        #optimal solution
        heaters.sort()
        distance=0
        for house in houses:
            left,right=0,len(heaters)-1
            minDistance=float("inf")
            while left<=right:
                mid=(left+right)//2
                minDistance=min(minDistance,abs(house-heaters[mid]))
                if heaters[mid]>house:
                    right=mid-1
                else:
                    left=mid+1
            distance=max(distance,minDistance)
        return distance
                
        #Brute force solutions
        distance=-float('inf')
        for house in houses:
            minDistance=float("inf")
            for heater in heaters:
                minDistance=min(minDistance,abs(house-heater))
            distance=max(distance,minDistance)
        return distance
        distance=[]
        for house in houses:
            minDistance=float("inf")
            for heater in heaters:
                minDistance=min(minDistance,abs(house-heater))
            distance.append(minDistance)

        return max(distance)
        