class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers.sort()
        result=0
        length=len(answers)
        current=0
        prev=0
        while current<length:
            prev=current
            result+=answers[current]+1
            minLength=answers[current]+1
            current=current+1
            index=1
            while prev<length and current<length and index<minLength and answers[prev]==answers[current]:
                current=current+1
                index=index+1      
        return result
        
        