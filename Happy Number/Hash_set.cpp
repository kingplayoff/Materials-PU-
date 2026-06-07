#include <iostream>
#include <unordered_set>

class Solution {
private:
    // Helper function to extract digits and calculate the sum of their squares
    int getNextNumber(int n) {
        int totalSum = 0;
        while (n > 0) {
            int digit = n % 10;  // Extract the last digit
            totalSum += digit * digit;
            n /= 10;             // Move to the next digit placeholder
        }
        return totalSum;
    }

public:
    bool isHappy(int n) {
        // Hash set to store previously encountered numbers
        std::unordered_set<int> visitedNumbers;

        // Loop runs until n becomes 1 (Happy) or falls into a cycle
        while (n != 1) {
            // Order of Operations Check: Test for presence BEFORE inserting new state
            if (visitedNumbers.count(n)) {
                return false; // Cycle detected, it's an unhappy number
            }
            
            visitedNumbers.insert(n);
            n = getNextNumber(n); // Advance to the next calculated value
        }

        return true; // Successfully converged to 1
    }
};

int main() {
    Solution solution;
    int testNum = 19; // Example 1: 19 is a Happy Number
    
    if (solution.isHappy(testNum)) {
        std::cout << testNum << " is a Happy Number!\n";
    } else {
        std::cout << testNum << " is not a Happy Number.\n";
    }
    return 0;
}