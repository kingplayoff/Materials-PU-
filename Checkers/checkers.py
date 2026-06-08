import sys

class CheckersSolver:
    def calculate_max_pieces(self, rows: int, cols: int) -> int:
        """
        Calculates the maximum number of checkers pieces or primary tiles 
        on an R x C board in O(1) time complexity.
        """
        total_cells = rows * cols
        
        # Mathematical ceiling division using pure integer arithmetic
        # Equivalent to ceil(total_cells / 2), maximizing odd grid properties
        return (total_cells // 2) + (total_cells % 2)

def main():
    solver = CheckersSolver()
    
    # Quick Diagnostic Verification Run
    sample_tests = [
        (1, 1),  # 1*1 = 1 -> Expected: 1
        (2, 2),  # 2*2 = 4 -> Expected: 2
        (3, 3),  # 3*3 = 9 -> Expected: 5 (Odd grid ceiling)
        (4, 3),  # 4*3 = 12 -> Expected: 6
    ]
    
    print("--- Diagnostic Run ---")
    for r, c in sample_tests:
        print(f"Board {r}x{c} -> Maximum Pieces: {solver.calculate_max_pieces(r, c)}")

    # Standard template configured to parse text inputs from Online Judge streaming batches
    # Reads all space-separated tokens to handle multiple inputs cleanly
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    idx = 0
    while idx < len(input_data):
        r = int(input_data[idx])
        if idx + 1 >= len(input_data):
            break
        c = int(input_data[idx+1])
        idx += 2
        
        # Termination Sentinel Gate (Adjust to match the platform's specific rule, e.g., 0 0)
        if r == 0 and c == 0:
            break
            
        result = solver.calculate_max_pieces(r, c)
        print(result)
    """

if __name__ == "__main__":
    main()