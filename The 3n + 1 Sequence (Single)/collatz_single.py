import sys

class CollatzSingleSolver:
    def generate_sequence(self, n: int) -> str:
        """
        Generates the 3n + 1 sequence for a single integer n until it reaches 1.
        Time Complexity: O(Steps) dependent on Collatz path length.
        Space Complexity: O(Steps) to store the sequence elements.
        """
        # Data Container initialization as described in Section 4 [cite: 76]
        sequence_log = []
        val = n # Primary variable data container [cite: 73]
        
        # Step-by-step Conditional Loop Processing [cite: 108]
        while val != 1:
            # Cast integer into string state before entering the collection [cite: 84]
            sequence_log.append(str(val))
            
            # Parity determination logic [cite: 130]
            if val % 2 == 0:
                val = val // 2 # Rule 1: Even operation [cite: 112, 119]
            else:
                val = 3 * val + 1 # Rule 2: Odd operation [cite: 113, 121]
                
        # Final Entry: insert the mandatory termination constant 1 [cite: 94, 103]
        sequence_log.append("1")
        
        # Flattening dynamic data container into a single blank-spaced row string [cite: 65, 95]
        return " ".join(sequence_log)

def main():
    solver = CollatzSingleSolver()
    
    # Quick Diagnostic Verification Run 
    sample_input = 6
    print("--- Diagnostic Run ---")
    print(f"Input: {sample_input}")
    print(f"Output Sequence: {solver.generate_sequence(sample_input)}") # Expected: 6 3 10 5 16 8 4 2 1 

    # Standard template configured to parse text inputs from Online Judge streaming batches
    # Reads a single number line-by-line or from a continuous stream until EOF
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    for token in input_data:
        start_number = int(token)
        # Call the calculation engine and output the exact required string layout [cite: 65]
        result_line = solver.generate_sequence(start_number)
        print(result_line)
    """

if __name__ == "__main__":
    main()