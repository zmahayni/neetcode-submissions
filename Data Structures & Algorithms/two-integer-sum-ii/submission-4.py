class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                print(i)
                print(j)
                if i == j:
                    continue
                if numbers[i] + numbers[j] > target:
                    numbers.pop()
                    continue
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
