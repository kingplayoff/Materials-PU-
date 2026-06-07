import sys
import math

class SquareNumbersSolver:
    def count_square_numbers(self, a: int, b: int) -> int:
        """
        Calculates the count of perfect squares within [A, B] in O(1) time complexity.
        Uses integer-safe root matching to eliminate floating-point drift.
        """
        # Guard clause for invalid ranges
        if a > b or b < 0:
            return 0
        
        # Ensure 'a' is non-negative for mathematical root execution
        a = max(0, a)

        # 1. Calculate the Upper Bound Floor Root
        # math.isqrt(b) natively rounds down to the nearest integer floor
        upper_root = math.isqrt(b)

        # 2. Calculate the Lower Bound Ceiling Root
        # To get the ceiling of sqrt(a) using integer math:
        # If 'a' is a perfect square, its integer root is exact.
        # Otherwise, adding 1 to the floor root shifts it correctly to the ceiling.
        floor_root_a = math.isqrt(a)
        if floor_root_a * floor_root_a == a:
            lower_root = floor_root_a
        else:
            lower_root = floor_root_a + 1

        # 3. Interval Counting Evaluation
        if lower_root > upper_root:
            return 0
            
        return upper_root - lower_root + 1

def main():
    solver = SquareNumbersSolver()
    
    # Quick Diagnostic Verification Run
    sample_tests = [
        (3, 9),   # Perfect squares are 4, 9 -> Expected Output: 2
        (1, 4),   # Perfect squares are 1, 4 -> Expected Output: 2
        (10, 20), # Perfect squares is 16     -> Expected Output: 1
    ]
    
    print("--- Diagnostic Run ---")
    for a, b in sample_tests:
        print(f"Interval [{a}, {b}] -> Count of Perfect Squares: {solver.count_square_numbers(a, b)}")

    # Standard template configured to parse massive Online Judge batch streams
    # Uncomment the block below for formal platform submission:
    """
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        # Ingest line integers
        parts = line.split()
        a = int(parts[0])
        b = int(parts[1])
        
        # Termination Sentinel Gate: exit instantly upon '0 0'
        if a == 0 and b == 0:
            break
            
        result = solver.count_square_numbers(a, b)
        print(result)
    """

if __name__ == "__main__":
    main()