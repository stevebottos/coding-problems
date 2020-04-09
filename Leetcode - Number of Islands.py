class Solution:

    """
    Recursive solution using dfs helper function
    """
    def dfs(r,c, rows, cols, grid, pts_on_this_island):
        # A check to ensure that we don't leave the bounds of the grid...
        if (r < 0) or (r > rows-1) or (c < 0) or (c > cols-1) or (grid[r][c] == '0'):
            return 0
        grid[r][c] = '0'
        pts_on_this_island += 1
        # Think about this... It'll keep going in all directions until it has traversed the whole "island"
        Solution.dfs(r+1, c, rows, cols, grid, pts_on_this_island)
        Solution.dfs(r-1, c, rows, cols, grid, pts_on_this_island)
        Solution.dfs(r, c-1, rows, cols, grid, pts_on_this_island)
        Solution.dfs(r, c+1, rows, cols, grid, pts_on_this_island)
        
        # Just extra, the area of the island
        # TO FUTURE ME: Review why recursive functions return backwards
        # print(pts_on_this_island)
        return 1
    
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        
        num_of_islands = 0
        rows = len(grid)
        cols = len(grid[0])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    pts_on_this_island = 0
                    num_of_islands += Solution.dfs(r,c, rows, cols, grid, pts_on_this_island)
        
        return num_of_islands