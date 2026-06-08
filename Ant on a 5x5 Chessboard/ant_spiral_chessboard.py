import sys
import math

class AntSpiralChessboardSolver:
    def get_coordinates(self, n: int) -> str:
        """
        Calculates the (X, Y) coordinates of an ant moving on a snake-like spiral grid at second n.
        Time Complexity: O(1) - Pure mathematical mapping logic.
        Space Complexity: O(1) - Auxiliary constant variables.
        """
        # Section 2 & 5: Determine the concentric shell ring
        shell = math.ceil(math.sqrt(n))
        
        # Calculate maximum token capacity index wrapped inside the previous layer inner boundary
        prev_max = (shell - 1) ** 2
        
        # Section 4: Determine path progression step distance offset parameter
        offset = n - prev_max
        
        x, y = 1, 1
        
        # Branch Evaluation Rules based on Parity Matrix Switches
        if shell % 2 != 0:
            # Case 1: Odd Shell Layer processing layout
            if offset <= shell:
                x = shell
                y = offset
            else:
                x = 2 * shell - offset
                y = shell
        else:
            # Case 2: Even Shell Layer processing layout
            if offset <= shell:
                x = offset
                y = shell
            else:
                x = shell
                y = 2 * shell - offset
                
        # Section 3: Format presentation syntax precisely
        return f"({x},{y})"

def main():
    solver = AntSpiralChessboardSolver()
    
    # Quick Diagnostic Verification Run Tracing Padlet Examples
    print("--- Diagnostic Verification Run ---")
    test_cases = [1, 3, 6, 7, 23]
    for case in test_cases:
        print(f"Time (n) = {case:2d} -> Coordinate position: {solver.get_coordinates(case)}")

    # Continuous Stream Processing Pipeline adjusted for Online Judge submission layers
    """
    input_tokens = sys.stdin.read().split()
    if not input_tokens:
        return
        
    for token in input_tokens:
        n_seconds = int(token)
        # Bounded processing condition check for standard 5x5 board simulation runtime limits
        if 1 <= n_seconds <= 25:
            result_tuple_string = solver.get_coordinates(n_seconds)
            print(result_tuple_string)
    """

if __name__ == "__main__":
    main()