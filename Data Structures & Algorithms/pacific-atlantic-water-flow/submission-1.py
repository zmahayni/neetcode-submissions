class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        if not heights or not heights[0]:
            return []

        R, C = len(heights), len(heights[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        def canReach(r: int, c: int, ocean: str) -> bool:
            seen = set()
            q = deque([(r,c)])
            seen.add((r,c))

            while q:
                x, y = q.popleft()
                # check if this touches the ocean edge
                if ocean == "pacific" and (x == 0 or y == 0):
                    return True
                if ocean == "atlantic" and (x == R-1 or y == C-1):
                    return True

                for dx, dy in dirs:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < R and 0 <= ny < C and (nx,ny) not in seen:
                        if heights[nx][ny] <= heights[x][y]:
                            seen.add((nx,ny))
                            q.append((nx,ny))
            return False

        ans = []
        for r in range(R):
            for c in range(C):
                if canReach(r, c, "pacific") and canReach(r, c, "atlantic"):
                    ans.append([r, c])
        return ans


        
            