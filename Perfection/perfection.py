import sys
import math

class PerfectionSolver:
    def classify_number(self, n: int) -> str:
        """
        Calculates the sum of proper divisors of N in O(sqrt(N)) time 
        and classifies it into PERFECT, DEFICIENT, or ABUNDANT.
        """
        # Edge Case handling: 1 has no proper divisors less than itself
        if n <= 1:
            return "DEFICIENT"

        # 1 is always a proper divisor for any N > 1
        divisor_sum = 1 
        sqrt_n = int(math.isqrt(n))

        # Loop from 2 up to sqrt(N)
        for i in range(2, sqrt_n + 1):
            if n % i == 0:
                divisor_sum += i # Add lower divisor
                
                # Add symmetric upper divisor only if it's unique
                symmetric_divisor = n // i
                if symmetric_divisor != i:
                    divisor_sum += symmetric_divisor #

        # State Classification Logic
        if divisor_sum == n:
            return "PERFECT" #
        elif divisor_sum < n:
            return "DEFICIENT" #
        else:
            return "ABUNDANT" #

def main():
    solver = PerfectionSolver()
    
    # Quick Diagnostic Verification Run
    sample_tests = [1, 6, 9, 12, 28]
    
    print("PERFECTION OUTPUT") # Header marker
    for n in sample_tests:
        category = solver.classify_number(n)
        # f"{n:>5}" enforces a right-aligned width of 5 characters
        print(f"{n:>5}  {category}") #
    print("END OF OUTPUT")     # Footer marker

    # Standard template configured to parse massive Online Judge batch text inputs
    # Handles arbitary whitespace and multiple integers per line cleanly.
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    print("PERFECTION OUTPUT") #
    for token in input_data:
        n = int(token)
        
        # Termination Sentinel Gate
        if n == 0:
            break
            
        category = solver.classify_number(n)
        print(f"{n:>5}  {category}") #
    print("END OF OUTPUT") #
    """

if __name__ == "__main__":
    main()