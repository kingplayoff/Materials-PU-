import sys

class ZappingSolver:
    def get_min_clicks(self, a: int, b: int) -> int:
        """
        Calculates the minimum button presses to switch from channel A to B 
        on a circular 100-channel dial (0-99).
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        # Calculate direct linear absolute distance
        direct_dist = abs(a - b)
        
        # Calculate circular wrap-around distance (total 100 channels)
        wrap_dist = 100 - direct_dist
        
        # Return the shortest route
        return min(direct_dist, wrap_dist)

def main():
    solver = ZappingSolver()
    
    # Quick Diagnostic Verification Run
    sample_tests = [
        (3, 9),   # Direct: 6, Wrap: 94 -> Expected: 6
        (0, 99),  # Direct: 99, Wrap: 1 -> Expected: 1 (Wrap around)
        (12, 88), # Direct: 76, Wrap: 24 -> Expected: 24
    ]
    
    print("--- Diagnostic Run ---")
    for a, b in sample_tests:
        print(f"From {a} to {b} -> Minimum Clicks: {solver.get_min_clicks(a, b)}")

    # Standard template configured to parse text inputs from Online Judge streaming batches
    # Continuously parses coordinate pairs and terminates cleanly on '-1 -1'
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    idx = 0
    while idx < len(input_data):
        a = int(input_data[idx])
        if idx + 1 >= len(input_data):
            break
        b = int(input_data[idx+1])
        idx += 2
        
        # Termination Sentinel Gate
        if a == -1 and b == -1:
            break
            
        result = solver.get_min_clicks(a, b)
        print(result)
    """

if __name__ == "__main__":
    main()