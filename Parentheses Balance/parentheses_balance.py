import sys

class ParenthesesBalancer:
    def check_balance(self, expression: str) -> str:
        """
        Validates the balancing configurations of string segments using a LIFO list stack.
        Time Complexity: O(L) where L is the length of the individual expression string.
        Space Complexity: O(L) auxiliary memory allocation matching total open items stack-depth.
        """
        # Section 1 & 5: Empty lines are explicitly categorized as balanced configurations
        if not expression or expression == "\n":
            return "Yes"

        stack = []
        
        # Section 2 & 5: Line vector step scanning loop
        for char in expression:
            if char in ('(', '['):
                stack.append(char)
            elif char == ')':
                if not stack or stack.pop() != '(':
                    return "No"
            elif char == ']':
                if not stack or stack.pop() != '[':
                    return "No"
                    
        # Section 5 Final Step: Stack must be completely empty to be verified as balanced
        return "Yes" if len(stack) == 0 else "No"

def main():
    balancer = ParenthesesBalancer()
    
    # Quick Diagnostic Verification Test Case Run
    print("--- Diagnostic Verification Run ---")
    diagnostic_inputs = ["()", "([])", "([)]", "", "((([][])))]"]
    for test in diagnostic_inputs:
        print(f"Expression: {test:<15} -> Balanced Status: {balancer.check_balance(test)}")

    # High-performance streaming interface pipeline optimized for automated Online Judge suites
    """
    input_lines = sys.stdin.read().splitlines()
    if not input_lines:
        return
        
    try:
        # Step 1: Parse total expected processing iterations count
        num_cases = int(input_lines[0].strip())
        
        # Step 2: Loop exactly over the provided case lines count parameters
        for idx in range(1, num_cases + 1):
            if idx < len(input_lines):
                target_str = input_lines[idx]
                print(balancer.check_balance(target_str))
            else:
                # Fallback for an empty or trailing blank string line
                print("Yes")
    except ValueError:
        return
    """

if __name__ == "__main__":
    main()