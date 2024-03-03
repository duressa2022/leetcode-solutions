class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        length=len(seats)
        result=0
        for i in range(length):
            result+=abs(seats[i]-students[i])
        return result        