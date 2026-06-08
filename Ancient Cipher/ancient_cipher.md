# 🧠 Detailed Problem Analysis: Ancient Cipher

## 📋 Problem Description
*Below is the structural statement and system evaluation requirement for the Ancient Cipher verification problem:*

![Problem Statement](Q12.png)

- **Official Platform Link:** [Providence University OJ - Ancient Cipher](https://cpex.cs.pu.edu.tw/)

---

## 🛠️ Section 1: Algorithm & Data Structure Foundation

### 1. Primary Data Structure Choice
To track and compare character mappings efficiently, the algorithm relies on structural frequency arrays:
- **Frequency Counter Tables / Fixed Arrays:** Since the problem statement restricts the alphabet size exclusively to uppercase English letters (`A` through `Z`), we map alphabet frequencies into two fixed arrays of size 26.
- **Sorting Containers (`std::sort` or sorted lists):** Used to normalize the frequency counts of both strings, allowing a direct structural comparison.

### 2. Functional Mechanics
The validation logic determines if an encrypted string can map back to an original string by focusing on a core mathematical constraint: **The exact permutation and substitution mappings do not care about *which* specific characters appear, but they strictly require that the *multiset of character frequencies* must be identical.**

The processing steps run as follows:
- **Frequency Distribution Mapping:** Count the occurrences of each uppercase letter in the original string and the encrypted string separately.
- **Frequency Value Normalization:** Sort both frequency lists in ascending order. Sorting strips away the character identity and isolates the structural distribution patterns.
- **Equivalence Assessment:** Compare the sorted arrays element-by-element. If both sorted lists match perfectly, it guarantees that a valid combination of substitution and substitution permutation exists, returning `"YES"`. If any mismatch is found, it returns `"NO"`.

---

## 🚀 Section 2: Advanced Code Optimization Strategies

To ensure clean processing of high-volume text streams, the solution integrates two optimization strategies:

### 1. Fixed $O(1)$ Space Frequency Buckets
Instead of allocating dynamic dictionary hash collections that incur rehashing and overhead costs, using fixed-size 26-element integer lists handles mapping updates at a constant $O(1)$ space and indexing runtime layout.

### 2. Built-in Sorting Normalization
Python’s native `.sort()` utilizes **Timsort**, which executes in $O(K \log K)$ time. Since $K = 26$ is a small constant, sorting the frequency tables takes negligible time, making the runtime complexity scale linearly with the length of the string: $O(N)$.

### 📊 Structural Complexity Comparison Chart
| Optimization Phase | Time Complexity | Space Complexity | Resource Benefit |
| :--- | :--- | :--- | :--- |
| **Brute Force Permutation Map** | $O(N!)$ | $O(N)$ | Computationally impossible due to combinatorial explosion. |
| **Dynamic Hash Multiset Match** | $O(N + K \log K)$ | $O(K)$ | Flexible, but introduces hashing function overhead. |
| **Fixed 26-Array Distribution** | **$O(N)$ Strict** | **$O(1)$ Fixed (26)** | **Maximum execution speed with no overhead.** |

*Note: $N$ is the length of the strings, and $K = 26$ represents the constant size of the alphabet.*

---

## 🔍 Section 3: Bug Hunting & Debugging Diagnostics

During the engineering lifecycle of this solution, the following technical traps were caught and resolved:

### 1. Common Logical Pitfalls (Bugs Checked)
- **String Length Mismatch:** Forgetting to check if the two strings have identical lengths before analyzing character distributions. If lengths differ, a valid cipher mapping is mathematically impossible. Skipping this check can cause false positives.
- **Unsorted Distribution Matches:** Comparing the frequency buckets directly without sorting them first. Direct comparison forces character-to-character frequency matches, which breaks the substitution rule (e.g., swapping all `A`s with `B`s).
- **Index Translation Inversions:** Writing incorrect ASCII offset calculations (such as `ord(char) - ord('a')` instead of using uppercase `'A'`), which leads to `IndexError` runtime faults during verification.

### 2. Debug Strategy Blueprint
- **Substitution Swap Tests:** Run a simple test case like `AABB` vs `BBAA` to confirm the frequency arrays handle sorted distributions correctly and output a valid `"YES"` state.
- **Structural Mismatch Checks:** Test strings that have identical characters but different distribution shapes (e.g., `AAA` vs `ABC`) to ensure the sorted frequency checker catches the distribution mismatch and flags it as `"NO"`.

---

## 🔗 Section 4: Resource Sharing
- **My Solution (Python Script):** [ancient_cipher.py](ancient_cipher.py)
- **Academic Reference Portfolio:** [Character Frequency Distribution Isomorphism Problems](https://leetcode.com/)