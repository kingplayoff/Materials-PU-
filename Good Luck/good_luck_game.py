import sys

class GoodLuckSolver:
    def __init__(self, max_limit=100005):
        self.max_limit = max_limit
        # True represents prime, False represents composite
        self.is_prime = [True] * (self.max_limit + 1)
        # 1: Losing state, 2: Winning state
        self.dp = [0] * (self.max_limit + 1)
        
        self._precompute_all()

    def _precompute_all(self):
        """
        Precomputes prime numbers using the Sieve of Eratosthenes 
        and calculates game states using Bottom-Up Dynamic Programming.
        """
        # 1. Sieve of Eratosthenes Execution
        self.is_prime[0] = self.is_prime[1] = False
        for p in range(2, int(self.max_limit**0.5) + 1):
            if self.is_prime[p]:
                for i in range(p * p, self.max_limit + 1, p):
                    self.is_prime[i] = False
                    
        # Extract primes list to optimize transition inner loops
        primes = [i for i, prime in enumerate(self.is_prime) if prime]

        # 2. Dynamic Programming Game State Solver
        # Base Cases: 0 and 1 are default Losing States (Value 1)
        self.dp[0] = 1
        self.dp[1] = 1

        for i in range(2, self.max_limit + 1):
            can_win = False
            for p in primes:
                if p > i:
                    break
                # If there exists a move leading to a Losing State, current state wins
                if self.dp[i - p] == 1:
                    can_win = True
                    break
            
            self.dp[i] = 2 if can_win else 1

    def solve(self, n: int) -> str:
        """
        Returns the winning status statement for the player.
        """
        # If dp[n] == 2, it is a winning state for the first player
        if self.dp[n] == 2:
            return "Good Luck"
        else:
            return "Bad Luck"

def main():
    # Instantiate the precomputation engine
    solver = GoodLuckSolver()
    
    # Example diagnostic run
    test_cases = [2, 3, 4, 5, 9]
    print("--- Diagnostic Run ---")
    for n in test_cases:
        print(f"Number N = {n} -> Result: {solver.solve(n)}")

    # Standard template used to handle high-volume Online Judge text streaming
    # Uncomment the lines below when pasting into the formal system submission box:
    """
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        n = int(line)
        print(solver.solve(n))
    """

if __name__ == "__main__":
    main()