class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights) - 1

        width = r - l 
        height = min(heights[l], heights[r])

        max_area = 0

        while l < r:
            width = r - l 
            height = min(heights[l], heights[r])
            curr_area = width * height
            max_area = max(max_area, curr_area)

            if heights[l] <= heights[r]:
                l += 1
            elif heights[r] <= heights[l]:
                r -= 1
            
        return max_area
            

        
        