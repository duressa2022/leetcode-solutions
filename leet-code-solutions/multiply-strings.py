class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        map={str(i):i for i in range(10)}
        number1=0
        for i in num1:
            if i in map:
                number1*=10
                number1+=map[i]
        number2=0
        for i in num2:
            if i in map:
                number2*=10
                number2+=map[i]
        return str(number1*number2)
        