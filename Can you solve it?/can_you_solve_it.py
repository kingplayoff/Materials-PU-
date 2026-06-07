import sys

class CanYouSolveItSolver:
    def get_absolute_steps(self, x: int, y: int) -> int:
        """
        Converts a 2D coordinate (x, y) into a 1D linear sequence index 
        using an arithmetic progression formula in O(1) time.
        """
        # Diagonal line identifier layer
        layer = x + y
        
        # Calculate base steps using integer floor division to prevent precision loss
        base_steps = (layer * (layer + 1)) // 2 #
        
        # Absolute sequence ID is base steps plus the current x-axis offset
        return base_steps + x

    def calculate_distance(self, x1: int, y1: int, x2: int, y2: int) -> int:
        """
        Calculates the distance between two grid coordinates.
        """
        id1 = self.get_absolute_steps(x1, y1)
        id2 = self.get_absolute_steps(x2, y2)
        
        # Return the absolute step difference
        return abs(id2 - id1)

def main():
    solver = CanYouSolveItSolver()
    
    # Quick Diagnostic Verification Run
    # Sample Test: (0, 0) to (0, 1) -> Expected Steps: |1 - 0| = 1
    # Sample Test: (0, 0) to (1, 0) -> Expected Steps: |2 - 0| = 2
    sample_tests = [
        (0, 0, 0, 1),
        (0, 0, 1, 0),
        (0, 1, 1, 0),
    ]
    
    print("--- Diagnostic Run ---")
    for case_idx, (x1, y1, x2, y2) in enumerate(sample_tests, 1):
        dist = solver.calculate_distance(x1, y1, x2, y2)
        print(f"Sample Case {case_idx}: ({x1},{y1}) -> ({x2},{y2}) = {dist} steps")

    # Standard template configured to parse Online Judge batch text inputs
    # Format expects a total count integer N followed by N query coordinate lines.
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    num_test_cases = int(input_data[0])
    idx = 1
    
    for case_num in range(1, num_test_cases + 1):
        x1 = int(input_data[idx])
        y1 = int(input_data[idx+1])
        x2 = int(input_data[idx+2])
        y2 = int(input_data[idx+3])
        idx += 4
        
        result = solver.calculate_distance(x1, y1, x2, y2)
        print(f"Case {case_num}: {result}")
    """

if __name__ == "__main__":
    main()