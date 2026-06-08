import sys

class HaikuValidator:
    def __init__(self):
        # Section 1: Define the target 6 vowels specified by the problem definition
        self.vowels = set("aeiouy")
        # Section 2 & 3: The standard Haiku layout metrics array
        self.expected_pattern = [5, 7, 5]

    def count_syllables(self, line: str) -> int:
        """
        Counts the total syllables in a line where consecutive vowels are grouped as one.
        Time Complexity: O(L) where L is the length of the line string.
        Space Complexity: O(1) auxiliary tracking space.
        """
        count = 0
        inside_vowel_group = False

        # Section 5: Step-by-step state matching character loop iterator
        for ch in line:
            if ch in self.vowels:
                if not inside_vowel_group:
                    count += 1
                    inside_vowel_group = True
            else:
                inside_vowel_group = False
                
        return count

    def verify_haiku(self, lines: list) -> str:
        """
        Validates if the 3 input lines match the 5-7-5 syllable layout criteria.
        Returns 'Y' if valid, or the 1-based index of the first invalid line.
        """
        # Section 5: Run the tracking loops across the 3 rows
        for i in range(3):
            line_syllables = self.count_syllables(lines[i])
            if line_syllables != self.expected_pattern[i]:
                return str(i + 1) # Return the 1-based line number immediately on failure
                
        return "Y"

def main():
    validator = HaikuValidator()
    
    # Quick Diagnostic Verification Test Case Run using Padlet parameters
    print("--- Diagnostic Verification Run ---")
    sample_haiku = [
        "do re mi fa so",
        "la ti do re mi fa so",
        "do re mi fa so"
    ]
    print(f"Sample Input Haiku:\n1: {sample_haiku[0]}\n2: {sample_haiku[1]}\n3: {sample_haiku[2]}")
    print(f"Validation Result: {validator.verify_haiku(sample_haiku)}")

    # Standard High-Performance streaming bridge pipeline for Online Judge automation
    """
    try:
        # Read exactly 3 lines of strings from standard input
        input_lines = []
        for _ in range(3):
            line = sys.stdin.readline()
            if not line:
                return
            input_lines.append(line.strip())
            
        result = validator.verify_haiku(input_lines)
        print(result)
    except Exception as e:
        return
    """

if __name__ == "__main__":
    main()