#include <iostream>
#include <string>
#include <unordered_map>
#include <algorithm>

class LanguageDetector {
private:
    // Optimized Associative Mapping container
    std::unordered_map<std::string, std::string> greetingMap;

    // Helper function to normalize text strings to uniform uppercase
    std::string toUpperCase(std::string str) {
        std::transform(str.begin(), str.end(), str.begin(), ::toupper);
        return str;
    }

public:
    LanguageDetector() {
        // Initialize the dictionary lookup cache database
        // You can expand this dictionary easily without affecting look-up speed O(1)
        greetingMap["HELLO"] = "ENGLISH";
        greetingMap["HOLA"] = "SPANISH"; //
        greetingMap["BONJOUR"] = "FRENCH"; //
        greetingMap["CIAO"] = "ITALIAN";
        greetingMap["HALLO"] = "GERMAN";
        greetingMap["ZEIN JIA"] = "CHINESE"; // Example placeholder
    }

    // Main classification process execution
    std::string detectLanguage(const std::string& inputWord) {
        // Case Normalization: Strip case sensitivity
        std::string normalizedWord = toUpperCase(inputWord);

        // Key-Value Efficiency: O(1) direct dictionary lookup
        auto it = greetingMap.find(normalizedWord);
        if (it != greetingMap.end()) {
            return it->second; // Return the matching verified language label
        }

        return "UNKNOWN"; // Fallback return for unrecognized tokens
    }
};

int main() {
    // Speed up standard stream processing buffer
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    LanguageDetector detector;
    std::string currentInput;
    int caseNumber = 1;

    // Sequential Word Processing stream loop
    while (std::cin >> currentInput) {
        // Early Exit: Check for termination sentinel at the very beginning
        if (currentInput == "#") { //
            break;
        }

        // Run detection logic
        std::string resultLanguage = detector.detectLanguage(currentInput);

        // Format output according to system standards
        std::cout << "Case " << caseNumber << ": " << resultLanguage << "\n";
        caseNumber++;
    }

    return 0;
}