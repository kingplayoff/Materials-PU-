import sys
import math

class AntChessboardSolver:
    def get_coordinates(self, n: int):
        """
        Calculates the exact (x, y) coordinates for a given second n in O(1) time.
        Handles large integer values safely without floating-point precision loss.
        """
        if n == 0:
            return 0, 0
            
        # 1. Locate the L-shaped layer boundary using integer-safe square roots
        # math.isqrt(n) computes the exact integer part of the square root
        root = math.isqrt(n)
        if root * root == n:
            s = root
        else:
            s = root + 1 # Ceiling root assignment
            
        # 2. Derive key mathematical structural thresholds for layer S
        s_squared = s * s
        previous_s_squared = (s - 1) * (s - 1)
        midpoint = s_squared - s + 1
        
        # 3. Apply Parity Direction Shift and Midpoint Evaluation Logic
        if s % 2 == 0:
            # Even Layer Logic: Growth starts vertically up, then goes right
            if n < midpoint:
                x = n - previous_s_squared
                y = s
            else:
                x = s
                y = s_squared - n + 1
        else:
            # Odd Layer Logic: Growth starts horizontally right, then goes up
            if n < midpoint:
                x = s
                y = n - previous_s_squared
            else:
                x = s_squared - n + 1
                y = s
                
        return x, y

def main():
    solver = AntChessboardSolver()
    
    # Example test cases processing from standard input simulation
    # Sample input test data array
    sample_inputs = [8, 20, 25, 3]
    
    print("--- Diagnostic Run ---")
    for n in sample_inputs:
        x, y = solver.get_coordinates(n)
        print(f"Second: {n} -> Coordinates: {x} {y}")

    # Standard template used to handle high-volume Online Judge text streaming
    # Uncomment the lines below when pasting into the formal system submission box:
    """
    for line in sys.stdin:
        n = int(line.strip())
        if n == 0:
            break
        x, y = solver.get_coordinates(n)
        print(f"{x} {y}")
    """

if __name__ == "__main__":
    main()