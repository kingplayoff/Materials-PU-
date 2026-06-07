#include <iostream>
#include <vector>
#include <unordered_set>

class B2SequenceSolver {
public:
    // Solver function executing validation logic on a given sequence
    bool isB2Sequence(const std::vector<int>& A) {
        int n = A.size();
        
        // 1. Sequence Integrity Gate: Validate positive and monotonic increasing constraints
        if (n > 0 && A[0] < 1) return false; // Elements must be greater than or equal to 1
        
        for (int i = 0; i < n - 1; ++i) {
            if (A[i] >= A[i + 1]) { 
                return false; // Fixes Monotonic Failure bug (must be strictly increasing)
            }
        }

        // Hash set container to cache and track pairwise sums
        std::unordered_set<int> seenSums;

        // 2. Pairwise Sum Generation & Collision Detection
        for (int i = 0; i < n; ++i) {
            // Fix for Boundary Fault: j starts from i because i <= j is allowed (a_i + a_i)
            for (int j = i; j < n; ++j) {
                int currentSum = A[i] + A[j];

                // Early-Exit Failure Trigger: Duplicate sum found -> Not a B2-Sequence
                if (seenSums.count(currentSum)) {
                    return false; 
                }
                
                // Commit unique calculated sum state to memory
                seenSums.insert(currentSum);
            }
        }

        return true; // Passed all constraints successfully
    }
};

int main() {
    // Optimize standard I/O buffer flow speed
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    B2SequenceSolver solver;
    int n;
    int caseNumber = 1;

    // Loop continuously tracks inputs until End-Of-File (EOF) to manage batch test cases
    while (std::cin >> n) {
        std::vector<int> A(n);
        for (int i = 0; i < n; ++i) {
            std::cin >> A[i];
        }

        // Execute verification logic
        bool result = solver.isB2Sequence(A);

        // Exact formatting matching Online Judge output specifications
        std::cout << "Case #" << caseNumber << ": ";
        if (result) {
            std::cout << "It is a B2-sequence.\n";
        } else {
            std::cout << "It is not a B2-sequence.\n";
        }
        
        // Formatter requirement: Output a trailing blank line after each case statement
        std::cout << "\n";
        
        caseNumber++;
    }

    return 0;
}