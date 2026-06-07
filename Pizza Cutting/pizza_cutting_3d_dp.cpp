#include <iostream>
#include <vector>
#include <string>

class PizzaCuttingSolution {
private:
    int rows, cols;
    const int MOD = 1e9 + 7; // Modulo to prevent integer overflow
    std::vector<std::vector<int>> preSum; // 2D Prefix Sum table
    // 3D DP Table: dp[k][r][c]
    std::vector<std::vector<std::vector<int>>> dp; 

    // Helper function to query apple count in a sub-grid using O(1) PreSum
    int getAppleCount(int r1, int c1, int r2, int c2) {
        return preSum[r1][c1] - preSum[r2 + 1][c1] - preSum[r1][c2 + 1] + preSum[r2 + 1][c2 + 1];
    }

    // Top-Down DFS with Memoization
    int dfs(int k, int r, int c) {
        // Base Case 1: If the remaining piece contains 0 apples, this cut path is invalid
        if (getAppleCount(r, c, rows - 1, cols - 1) == 0) {
            return 0; //
        }
        // Base Case 2: If all required cuts have been successfully made
        if (k == 0) {
            return 1; // Valid way found
        }
        // Overlapping Subproblems: Return cached result if already calculated
        if (dp[k][r][c] != -1) {
            return dp[k][r][c];
        }

        long long totalWays = 0;

        // 1. Explore Horizontal Cuts (Iterate through rows nr > r)
        // Fix for Off-by-One error: boundary checked up to rows - 1
        for (int nr = r + 1; nr < rows; ++nr) {
            // Invalid Cuts Check: Upper piece must have at least one apple
            if (getAppleCount(r, c, nr - 1, cols - 1) > 0) {
                totalWays = (totalWays + dfs(k - 1, nr, c)) % MOD; // Apply Modulo
            }
        }

        // 2. Explore Vertical Cuts (Iterate through columns nc > c)
        // Fix for Off-by-One error: boundary checked up to cols - 1
        for (int nc = c + 1; nc < cols; ++nc) {
            // Invalid Cuts Check: Left piece must have at least one apple
            if (getAppleCount(r, c, rows - 1, nc - 1) > 0) {
                totalWays = (totalWays + dfs(k - 1, r, nc)) % MOD; // Apply Modulo
            }
        }

        // Store result in the memoization table before returning
        return dp[k][r][c] = totalWays;
    }

public:
    int ways(std::vector<std::string>& pizza, int k) {
        rows = pizza.size();
        cols = pizza[0].size();
        
        // Initialize 2D Prefix Sum matrix with size (rows+1) x (cols+1) to prevent out-of-bound errors
        preSum.assign(rows + 1, std::vector<int>(cols + 1, 0));
        
        // Preprocessing: Build the preSum matrix using bottom-up accumulation
        for (int r = rows - 1; r >= 0; --r) {
            for (int c = cols - 1; c >= 0; --c) {
                int isApple = (pizza[r][c] == 'A') ? 1 : 0;
                preSum[r][c] = isApple + preSum[r + 1][c] + preSum[r][c + 1] - preSum[r + 1][c + 1];
            }
        }

        // Initialize 3D DP table with size [k][rows][cols] filled with -1
        dp.assign(k, std::vector<std::vector<int>>(rows, std::vector<int>(cols, -1)));

        // Trigger DFS from top-left (0,0) requiring k-1 cuts
        return dfs(k - 1, 0, 0);
    }
};

int main() {
    PizzaCuttingSolution solution;
    
    // Grid representation: 'A' represents an apple, '.' is empty space
    std::vector<std::string> pizza = {
        "A..",
        "AAA",
        "..."
    };
    int k = 3; // Target slices count

    int result = solution.ways(pizza, k);
    std::cout << "Total valid ways to cut the pizza: " << result << std::endl;

    return 0;
}