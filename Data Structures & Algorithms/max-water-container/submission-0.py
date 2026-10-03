class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        l = 0
        r = len(heights) - 1
        width = r
        while l < r:
            curr = 0
            if heights[l] < heights[r]:
                curr = heights[l] * width
                l+=1
                width-=1
            else:
                curr = heights[r] * width
                r-=1
                width-=1
            if curr > max:
                max = curr
        return max
            

            