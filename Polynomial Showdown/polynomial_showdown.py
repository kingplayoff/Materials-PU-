import sys

class PolynomialShowdownSolver:
    def format_polynomial(self, coefficients: list) -> str:
        """
        Formats a list of 9 coefficients into a valid algebraic polynomial string.
        Time Complexity: O(1) due to the fixed input size of 9 elements.
        Space Complexity: O(1) auxiliary buffer.
        """
        # Guard Clause: Check if the entire polynomial consists of zeroes
        if all(c == 0 for c in coefficients):
            return "0" #

        output_tokens = []
        is_first = True # Flag tracking whether we are printing the head of the polynomial

        # Process each coefficient from highest power (x^8) down to constant (x^0)
        for idx, coef in enumerate(coefficients):
            if coef == 0:
                continue # Zero coefficients are suppressed completely

            power = 8 - idx # Power degree map

            # 1. Handle intermediate sign spacing for the body terms
            if not is_first:
                if coef > 0:
                    output_tokens.append(" + ") #
                else:
                    output_tokens.append(" - ") #
            else:
                # For the head term, a leading negative sign is attached directly without spaces
                if coef < 0:
                    output_tokens.append("-") #

            # Get the absolute value to format the magnitude cleanly
            abs_coef = abs(coef)

            # 2. Format the coefficient magnitude
            # Omit the coefficient '1' if there is a variable part (power > 0)
            if abs_coef != 1 or power == 0:
                output_tokens.append(str(abs_coef)) #

            # 3. Format the variable and exponent parts
            if power > 1:
                output_tokens.append(f"x^{power}") #
            elif power == 1:
                output_tokens.append("x") #

            # Once the first active term is printed, clear the flag
            is_first = False

        return "".join(output_tokens)

def main():
    solver = PolynomialShowdownSolver()
    
    # Quick Diagnostic Verification Run
    sample_tests = [
        [0, 0, 0, 1, 1, -7, 0, 3, -1], # Expected: x^5 + x^4 - 7x^3 + 3x - 1
        [0, 0, 0, 0, 0, 0, 0, 0, 0],   # Expected: 0
        [-1, 0, 0, 0, 0, 0, 0, 0, 1],  # Expected: -x^8 + 1
    ]
    
    print("--- Diagnostic Run ---")
    for coefs in sample_tests:
        print(f"Coefficients: {coefs} \n-> Polynomial: {solver.format_polynomial(coefs)}")

    # Standard template configured to parse text inputs from Online Judge streaming batches
    # Each line contains exactly 9 space-separated integers.
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    idx = 0
    while idx < len(input_data):
        # Extract 9 tokens at a time to form a case row
        row_coefficients = [int(x) for x in input_data[idx : idx + 9]]
        idx += 9
        
        if len(row_coefficients) < 9:
            break
            
        result = solver.format_polynomial(row_coefficients)
        print(result)
    """

if __name__ == "__main__":
    main()