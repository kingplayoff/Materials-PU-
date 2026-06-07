import sys

class PrimaryArithmeticSolver:
    def count_carries(self, a: int, b: int) -> int:
        """
        Calculates the total number of carry operations when adding a and b.
        Time Complexity: O(log(max(a, b)))
        Space Complexity: O(1)
        """
        carry_count = 0
        carry = 0

        # Fix for Chain-Carry Blindspot: loop must continue if a carry remains
        while a > 0 or b > 0 or carry > 0:
            # Extract the trailing digits
            digit_a = a % 10
            digit_b = b % 10

            # Calculate column sum including the previous carry state
            column_sum = digit_a + digit_b + carry

            # Evaluate carry trigger conditions
            if column_sum >= 10:
                carry_count += 1
                carry = 1 # Set carry for next column
            else:
                carry = 0 # Fix for Carry Reset bug

            # Reduce the numbers for the next iteration
            a //= 10
            b //= 10

        return carry_count

    def format_output(self, carry_count: int) -> str:
        """
        Formats the output string according to the strict grammar rules.
        """
        if carry_count == 0:
            return "No carry operation."
        elif carry_count == 1:
            return "1 carry operation."
        else:
            return f"{carry_count} carry operations."

def main():
    solver = PrimaryArithmeticSolver()
    
    # Quick Diagnostic Verification Run
    sample_tests = [
        (123, 456), # Expected: No carry operation.
        (555, 555), # Expected: 3 carry operations.
        (123, 594), # Expected: 1 carry operation.
        (999, 1),   # Expected: 3 carry operations. (Tests Chain-Carry)
    ]
    
    print("--- Diagnostic Run ---")
    for a, b in sample_tests:
        count = solver.count_carries(a, b)
        print(f"{a} + {b} -> {solver.format_output(count)}")

    # Standard template configured to parse massive Online Judge batch streams
    # Uncomment the block below for formal platform submission:
    """
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
            
        parts = line.split()
        a = int(parts[0])
        b = int(parts[1])
        
        # Termination Sentinel Gate
        if a == 0 and b == 0:
            break
            
        carries = solver.count_carries(a, b)
        print(solver.format_output(carries))
    """

if __name__ == "__main__":
    main()