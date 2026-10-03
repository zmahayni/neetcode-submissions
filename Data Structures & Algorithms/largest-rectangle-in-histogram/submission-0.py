class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        # for i, h in enumerate(heights):
        #     if not stack:
        #         stack.append([i,h])
        #     else:
        #         while h <= stack[-1][1]:
        #             width = i - stack[-1][0]
        #             area = h * width
        #             max_area = max(max_area, area)
        #             stack.append([stack.pop()[0], h])
        #         else:
        #             stack.append(i, h)
        # for i, h in stack:
        #     max_area = max(max_area, h * (len(heights) - i))
        # return max_area

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append([start, h])
        
        for i, h in (stack):
            max_area = max(max_area, h * (len(heights) - i))
        return max_area


