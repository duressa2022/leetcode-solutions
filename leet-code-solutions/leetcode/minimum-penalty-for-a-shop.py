class Solution:
    def bestClosingTime(self, customers: str) -> int:
        length=len(customers)
        customers=customers[::-1]
        customerArrival=[0]*(length+1)
        customerNonArrival=[0]*(length+1)
        for i in range(1,length+1):
            if customers[i-1]=="Y":
                customerArrival[i]=customerArrival[i-1]+1
            else:
                customerArrival[i]=customerArrival[i-1]
        customerArrival.reverse()
        customers=customers[::-1]
        for i in range(1,length+1):
            if customers[i-1]=="N":
                customerNonArrival[i]=customerNonArrival[i-1]+1
            else:
                customerNonArrival[i]=customerNonArrival[i-1]
        minHour=length+1
        penality=float("inf")
        for i in range(length+1):
            current=customerArrival[i]+customerNonArrival[i]
            if current<penality:
                minHour=i
                penality=current
        return minHour

        