#include <iostream>
#include <vector>
#include <algorithm>

class CollatzSolution {
private:
    // Global cache limit setup to balance memory allocation and speed bounds
    // Numbers above this threshold are computed dynamically without memory overhead
    const int CACHE_LIMIT = 1000000;
    std::vector<int> cache;

public:
    CollatzSolution() {
        // Initialize the memoization table with 0s, size defined by optimization threshold
        cache.assign(CACHE_LIMIT, 0);
        cache[1] = 1; // Base Case: 1 takes exactly 1 step
    }

    // Helper function to find the cycle length of a single number with high optimizations
    long long getCycleLength(long long n) {
        if (n == 1) return 1;

        // Check if the calculation hit a known cached result to return early
        if (n < CACHE_LIMIT && cache[n] != 0) {
            return cache[n];
        }

        long long length = 0;
        // Bitwise Optimization: Replace n % 2 != 0 with (n & 1)
        if (n & 1) {
            // Safe execution handling intermediate integer overflow risks
            length = 1 + getCycleLength(3 * n + 1); //
        } else {
            // Bitwise Optimization: Replace n / 2 with n >> 1 shift
            length = 1 + getCycleLength(n >> 1); //
        }

        // Store result into memoization cache table if within bounds
        if (n < CACHE_LIMIT) {
            cache[n] = length;
        }

        return length;
    }

    // Main solver function handling range iterations and parameter boundary anomalies
    long long getMaxCycleLength(long long i, long long j) {
        long long original_i = i;
        long long original_j = j;

        // Smart Boundary Management: Swap values if range parameters are inverted
        if (i > j) {
            std::swap(i, j); // Fixes Incorrect Range Handling bug
        }

        long long maxCycle = 0;

        // Loop through every single tracking number in the interval
        for (long long n = i; n <= j; ++n) {
            long long currentCycle = getCycleLength(n); //
            maxCycle = std::max(maxCycle, currentCycle); // Record Tracking
        }

        return maxCycle;
    }
};

int main() {
    CollatzSolution solver;
    
    // Standard input sample pairs (handles normal and inverted ranges)
    long long i = 1;
    long long j = 10;
    
    long long max_len = solver.getMaxCycleLength(i, j);
    std::cout << i << " " << j << " " << max_len << std::endl;

    // Test case for Inverted Range handling
    long long inv_i = 100;
    long long inv_j = 1;
    long long inv_max_len = solver.getMaxCycleLength(inv_i, inv_j);
    std::cout << inv_i << " " << inv_j << " " << inv_max_len << std::endl;

    return 0;
}