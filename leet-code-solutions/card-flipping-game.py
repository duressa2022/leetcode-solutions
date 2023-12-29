class Solution:
    def flipgame(self,fronts, backs):
        result=None
        hash_set=set()
        for front,back in zip(fronts,backs):
            if front==back:
                hash_set.add(front)
        cards=fronts+backs
        for number in cards:
            if number not in hash_set:
                if result is None or result>number:
                    result=number
        return result if result is  not None else 0

            
