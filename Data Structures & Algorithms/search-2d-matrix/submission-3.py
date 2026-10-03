class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = [element for row in matrix for element in row]

        l = 0
        r = len(arr) - 1

        while (l <= r):
            m =  (l + r)//2
            if arr[m] < target:
                l = m + 1
            elif arr[m] > target:
                r = m - 1
            else:
                return True
        return False
            