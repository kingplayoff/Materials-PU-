import sys

class SimpleCipherSolver:
    def verify_cipher_equivalence(self, s1: str, s2: str) -> str:
        """
        Determines if s1 can be transformed into s2 via rearrangement and 1-to-1 mapping.
        Time Complexity: O(N) where N is the length of the string (Sorting 26 elements takes O(1) constant time).
        Space Complexity: O(1) auxiliary constant frequency storage footprint.
        """
        # Section 1 Safeguard: Strings must have identical length characteristics
        if len(s1) != len(s2):
            return "NO"

        # Section 4: Allocate fixed-size frequency vectors
        count1 = [0] * 26
        count2 = [0] * 26

        # Section 5: Populate character frequency maps
        for char in s1:
            idx = ord(char) - ord('A')
            if 0 <= idx < 26:
                count1[idx] += 1

        for char in s2:
            idx = ord(char) - ord('A')
            if 0 <= idx < 26:
                count2[idx] += 1

        # Sort vector footprints to cross-examine core fingerprints
        count1.sort()
        count2.sort()

        # Section 3 & 5: Identity pattern verification evaluation
        if count1 == count2:
            return "YES"
        else:
            return "NO"

def main():
    solver = SimpleCipherSolver()
    
    # Quick Diagnostic Verification Run matching Padlet analytical test cases
    print("--- Diagnostic Verification Run ---")
    test_cases = [
        ("AAAA", "BBBB"),
        ("AABBCC", "XXYYZZ"),
        ("JWPUDJSTVP", "VICTORIOUS"),
        ("APPLE", "WORLD")
    ]
    for s1, s2 in test_cases:
        print(f"S1: {s1:<12} | S2: {s2:<12} -> Valid Mapping: {solver.verify_cipher_equivalence(s1, s2)}")

    # High-performance streaming interface pipeline optimized for Online Judge batches
    """
    input_data = sys.stdin.read().split()
    if not input_data or len(input_data) % 2 != 0:
        return
        
    for i in range(0, len(input_data), 2):
        string_one = input_data[i].strip()
        string_two = input_data[i+1].strip()
        
        result_flag = solver.verify_cipher_equivalence(string_one, string_two)
        print(result_flag)
    """

if __name__ == "__main__":
    main()