from typing import List

class ATM:

    def __init__(self):
        self.array_notes=[20,50,100,200,500]
        self.list_deposits=[0 for i in range(len(self.array_notes))]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(self.array_notes)):
            self.list_deposits[i]+=banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        result=[0 for i in range(len(self.array_notes))]
        for i in range(len(self.array_notes)-1,-1,-1):
            counter=min(self.list_deposits[i],amount//self.array_notes[i])
            result[i]=counter
            amount=amount-self.array_notes[i]*counter
        if amount!=0:
            return [-1]
        for i in range(len(self.array_notes)):
            self.list_deposits[i]-=result[i]
        return result









        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)