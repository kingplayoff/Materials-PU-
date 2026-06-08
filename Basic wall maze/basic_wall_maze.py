import sys
from collections import deque

class BasicWallMazeSolver:
    def solve_maze(self, grid: list, start_x: int, start_y: int, end_x: int, end_y: int) -> int:
        """
        Finds the shortest path distance in a 2D grid maze using BFS traversal.
        Time Complexity: O(R * C)
        Space Complexity: O(R * C) for the queue container tracking.
        """
        rows = len(grid)
        cols = len(grid[0])
        
        # Guard clause: check if start or end positions are blocked
        if grid[start_x][start_y] == '#' or grid[end_x][end_y] == '#':
            return -1

        # Queue storing tuples of (current_x, current_y, current_distance)
        queue = deque([(start_x, start_y, 0)])
        
        # In-Place Visited Optimization: mark the starting cell as a wall to prevent re-entry
        grid[start_x][start_y] = '#'

        # Directional Vectors for orthogonal steps (Up, Down, Left, Right)
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        while queue:
            curr_x, curr_y, dist = queue.popleft()

            # Target Destination Check: if reached, return the path distance
            if curr_x == end_x and curr_y == end_y:
                return dist

            # Explore 4 orthogonal directions
            for i in range(4):
                nx, ny = curr_x + dx[i], curr_y + dy[i]

                # Boundary Verification Gate: Check bounds and if the path is open
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != '#':
                    # In-Place Visited Optimization: Mark visited immediately to avoid queue explosion
                    grid[nx][ny] = '#'
                    queue.append((nx, ny, dist + 1))

        return -1 # Return -1 if destination is completely unreachable

def main():
    # Simulation sample grid
    # '.' represents open paths, '#' represents walls
    sample_grid = [
        ['.', '.', '.', '#', '.'],
        ['#', '#', '.', '#', '.'],
        ['.', '.', '.', '.', '.'],
        ['.', '#', '#', '#', '#'],
        ['.', '.', '.', '.', '.']
    ]
    
    solver = BasicWallMazeSolver()
    # Path from top-left (0,0) to bottom-right (4,4)
    result = solver.solve_maze(sample_grid, 0, 0, 4, 4)
    
    print("--- Diagnostic Run ---")
    print(f"Shortest path distance: {result} steps")

    # Standard template configured to parse Online Judge batch text inputs
    # Uncomment the block below for formal platform submission:
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    # Example parser depending on problem format:
    # rows = int(input_data[0])
    # cols = int(input_data[1])
    # ... parse grid map matrix and run solver ...
    """

if __name__ == "__main__":
    main()