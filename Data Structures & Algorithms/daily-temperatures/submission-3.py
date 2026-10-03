class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackI = stack.pop()
                result[stackI] = (i-stackI)
            stack.append([t, i])

        # for i in range(len(temperatures)):
        #     t = temperatures[i]
        #     while stack and t > temperatures[stack[-1]]:
        #         index = stack.pop()
        #         result[index] = result[i - index]
        #     stack.append(i)

        return result


        
            