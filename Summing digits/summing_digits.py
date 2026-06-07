import sys

class SummingDigitsSolver:
    def get_digital_root_math(self, n: int) -> int:
        """
        Method 1: Highly optimized O(1) mathematical closed-form approach.
        Fixes the Modulo-9 edge defect using: 1 + (n - 1) % 9.
        """
        if n == 0:
            return 0
        return 1 + (n - 1) % 9 #

    def get_digital_root_loop(self, n: int) -> int:
        """
        Method 2: Clean O(log N) integer arithmetic simulation loop.
        Completely bypasses string allocation overhead.
        """
        # Loop continues until the number collapses to a single digit
        while n >= 10:
            digit_sum = 0 # Reset sum for the current reduction phase
            
            # Digit Stripping execution
            while n > 0:
                digit_sum += n % 10 # Extract lowest digit
                n //= 10            # Truncate lowest digit
                
            n = digit_sum # Transition current state to the calculated sum
            
        return n

def main():
    solver = SummingDigitsSolver()
    
    # Quick Diagnostic Verification Run
    sample_tests = [
        2,      # Single digit -> Expected: 2
        11,     # 1 + 1 -> Expected: 2
        47,     # 4 + 7 = 11 -> 1 + 1 -> Expected: 2
        12345,  # 1+2+3+4+5 = 15 -> 1 + 5 -> Expected: 6
        9,      # Modulo-9 Anchor test -> Expected: 9
        18,     # Modulo-9 Anchor test -> Expected: 9
    ]
    
    print("--- Diagnostic Run (Using Math O(1)) ---")
    for n in sample_tests:
        print(f"Number: {n:5} -> Digital Root: {solver.get_digital_root_math(n)}")

    # Standard template configured to parse massive Online Judge batch text inputs
    # Uncomment the block below for formal platform submission:
    """
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
            
        n = int(line)
        
        # Termination Sentinel Gate
        if n == 0:
            break
            
        # Using the ultra-fast O(1) mathematical shortcut
        result = solver.get_digital_root_math(n)
        print(result)
    """

if __name__ == "__main__":
    main()