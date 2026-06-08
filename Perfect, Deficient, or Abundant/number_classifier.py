import sys

class NumberPropertyClassifier:
    def classify_number(self, n: int) -> str:
        """
        Classifies whether a positive integer n is perfect, abundant, or deficient.
        Time Complexity: O(n) linear evaluation scanning limits.
        Space Complexity: O(1) constant architectural storage markers.
        """
        # Section 4: Initialize the aggregation accumulator container
        div_sum = 0
        
        # Section 2 & 5: Loop through all proper candidate values from 1 to n-1
        for i in range(1, n):
            if n % i == 0:
                div_sum += i # Append proper divisor to running total accumulation
                
        # Section 3: Branch classification validation criteria tests
        if div_sum == n:
            return "perfect"
        elif div_sum > n:
            return "abundant"
        else:
            return "deficient"

def main():
    classifier = NumberPropertyClassifier()
    
    # Quick Diagnostic Verification Run tracking Padlet test parameters
    print("--- Diagnostic Verification Run ---")
    sample_cases = [6, 12, 9]
    for case in sample_cases:
        print(f"Input Integer: {case:2d} -> Classification Result: {classifier.classify_number(case)}")

    # Standard Streaming Bridge for automated Online Judge submission engines
    """
    input_tokens = sys.stdin.read().split()
    if not input_tokens:
        return
        
    for token in input_tokens:
        target_number = int(token)
        if target_number > 0:
            output_string = classifier.classify_number(target_number)
            print(output_string)
    """

if __name__ == "__main__":
    main()