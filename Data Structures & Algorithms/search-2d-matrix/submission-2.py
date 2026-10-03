class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0

        while(i < len(matrix)):
            l = 0
            r = len(matrix[0]) - 1
            while (l <= r):
                m = (l + r)//2
                if matrix[i][m] < target:
                    l = m + 1
                elif matrix[i][m] > target:
                    r = m - 1
                else:
                    return True
            i += 1
        return False
            