import sys

class HaikuReviewSolver:
    def count_syllables(self, phrase: str) -> int:
        """
        Counts the syllables in a phrase based on groups of consecutive vowels.
        Vowels include: a, e, i, o, u, y.
        Time Complexity: O(L) where L is the length of the phrase string.
        """
        vowels = {'a', 'e', 'i', 'o', 'u', 'y'} # 'y' is a vowel here
        syllable_count = 0
        in_vowel_group = False # Flag tracking consecutive vowel streams

        for char in phrase.lower():
            if char in vowels:
                if not in_vowel_group:
                    syllable_count += 1
                    in_vowel_group = True # Lock flag for consecutive vowels
            else:
                in_vowel_group = False # Reset flag when hitting a consonant or symbol

        return syllable_count

    def validate_haiku(self, line: str) -> str:
        """
        Validates if a line follows the 5-7-5 syllable rule of Haiku.
        Returns 'Y' if valid, or the 1-based index of the first broken phrase.
        """
        # Split the input line into exactly three phrases
        phrases = line.strip().split('/')
        if len(phrases) != 3:
            return "1" # Fallback safeguard if line formatting is totally broken

        # Strict target syllable rules for Haiku
        target_syllables = [5, 7, 5]

        for idx, phrase in enumerate(phrases):
            actual_count = self.count_syllables(phrase)
            # Early break strategy: check for a syllable count mismatch
            if actual_count != target_syllables[idx]:
                return str(idx + 1) # Return 1-based index of the broken phrase

        return "Y" # Return 'Y' if all phrases match the 5-7-5 structure

def main():
    solver = HaikuReviewSolver()
    
    # Quick Diagnostic Verification Run
    sample_tests = [
        "happy purple frog/eating bugs in the sunshine/it is a good day", # Expected: Y (5-7-5)
        "computer/is running too slow/need help",                     # Expected: 1 (Phrase 1 broken)
    ]
    
    print("--- Diagnostic Run ---")
    for test in sample_tests:
        print(f"Haiku Input: {test} \n-> Validation Result: {solver.validate_haiku(test)}")

    # Standard template configured to parse text inputs from Online Judge streaming batches
    # Continuously processes lines until hitting the sentinel string 'e/o/f'
    """
    input_lines = sys.stdin.read().splitlines()
    for line in input_lines:
        if not line:
            continue
            
        # Termination Sentinel Gate
        if line.strip() == "e/o/f":
            break
            
        result = solver.validate_haiku(line)
        print(result)
    """

if __name__ == "__main__":
    main()