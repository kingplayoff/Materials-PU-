import sys

class FindingHaplotypesSolver:
    def count_possible_haplotypes(self, genotype_str: str) -> int:
        """
        Calculates the total number of distinct haplotypes from a genotype sequence.
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(1) auxiliary space.
        """
        # Clean string to eliminate whitespace pollution
        genotype_str = genotype_str.strip()
        
        # Count the number of heterozygous sites 'H'
        heterozygous_count = genotype_str.count('H')
        
        # Fast Bitwise Shift Operator to calculate 2^H instantly
        # Equivalent to math.pow(2, heterozygous_count) but executes at the CPU bit-level
        return 1 << heterozygous_count

def main():
    solver = FindingHaplotypesSolver()
    
    # Quick Diagnostic Verification Run
    sample_tests = [
        "***",       # All homozygous -> Expected: 2^0 = 1
        "H**",       # 1 Heterozygous -> Expected: 2^1 = 2
        "H*H",       # 2 Heterozygous -> Expected: 2^2 = 4
        "HHHHHHHH",  # 8 Heterozygous -> Expected: 2^8 = 256
    ]
    
    print("--- Diagnostic Run ---")
    for genotype in sample_tests:
        result = solver.count_possible_haplotypes(genotype)
        print(f"Genotype Sequence: {genotype:10} -> Possible Haplotypes: {result}")

    # Standard template configured to parse text inputs from Online Judge streaming batches
    # Triggers continuous loop and breaks on empty or end-of-stream signals
    """
    input_data = sys.stdin.read().splitlines()
    for line in input_data:
        if not line:
            continue
            
        # Adjust termination condition based on the platform requirement (e.g., a specific character or string)
        if line.strip() == "END":
            break
            
        result = solver.count_possible_haplotypes(line)
        print(result)
    """

if __name__ == "__main__":
    main()