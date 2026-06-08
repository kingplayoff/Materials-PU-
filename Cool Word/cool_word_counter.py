import sys

class CoolWordCounter:
    def is_cool_word(self, word: str) -> bool:
        """
        Validates if a word matches the 'Cool Word' criteria.
        Time Complexity: O(L) where L is the length of the string word.
        Space Complexity: O(1) auxiliary fixed alphabet storage array footprint.
        """
        if len(word) < 2:
            return False
            
        # Section 4: Allocate fixed letter map slots
        char_counts = [0] * 26
        for char in word:
            idx = ord(char) - ord('a')
            if 0 <= idx < 26:
                char_counts[idx] += 1
                
        # Section 5: Extract non-zero occurrence numbers
        frequencies = [count for count in char_counts if count > 0]
        
        # Condition Check 1: Must contain at least 2 distinct characters
        if len(frequencies) < 2:
            return False
            
        # Condition Check 2: All frequency values must be unique
        return len(frequencies) == len(set(frequencies))

def main():
    counter = CoolWordCounter()
    
    # Quick Diagnostic Verification Run matching Section 2 trace profiles
    print("--- Diagnostic Verification Run ---")
    test_words = ["banana", "apple", "aaaa", "cool"]
    for word in test_words:
        print(f"Word: {word:<10} -> Is Cool Word: {counter.is_cool_word(word)}")

    # Production stream-reading engine designed for Online Judge verification passes
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    token_ptr = 0
    case_num = 1
    
    while token_ptr < len(input_data):
        # Step 2: Read block limit integer N
        N = int(input_data[token_ptr])
        token_ptr += 1
        
        cool_word_count = 0
        
        # Step 4: Iterate precisely over N input strings
        for _ in range(N):
            if token_ptr < len(input_data):
                current_word = input_data[token_ptr]
                if counter.is_cool_word(current_word):
                    cool_word_count += 1
                token_ptr += 1
                
        # Step 5: Output structured layout format to stdout
        print(f"Case {case_num}: {cool_word_count}")
        case_num += 1
    """

if __name__ == "__main__":
    main()