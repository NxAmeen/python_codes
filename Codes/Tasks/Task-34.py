class MathUtils:
    @staticmethod
    def calculatesum(numbers):
        return sum(numbers)
    

numbers=[1,2,3,4,5]
result=MathUtils.calculatesum(numbers)
print(f'Sum of the numbers: {result}')