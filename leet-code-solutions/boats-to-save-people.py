class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left,right=0,len(people)-1
        counter=0
        while left<=right:
            if left!=right:
                current=people[left]+people[right]
            else:
                current=people[right]
                counter+=1
                break
            if current<=limit:
                counter+=1
                left=left+1
                right=right-1
            elif current>limit:
                counter+=1
                right=right-1
        return counter


        