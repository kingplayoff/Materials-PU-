# 🧠 Problem Analysis: Happy Number

## 📋 Problem Description
*(Bạn copy phần mô tả đề bài hoặc dán link bài LeetCode vào đây)*
- **Link:** [LeetCode 20 - Happy Number](https://leetcode.com/)

---

## 🛠️ Section 1: Algorithm & Data Structure

### 1. Initial Approach (Hash Set)
We use `std::unordered_set<int>` as the primary data structure. It stores previously encountered numbers to detect cycles in $O(1)$ average time complexity per lookup.

**Algorithm Logic:**
- **Digit Extraction:** The helper function uses `n % 10` to get the digit and `n /= 10` to move to the next placeholder to calculate the sum of squares.
- **Detection:** If `n` becomes `1`, the function returns `true`. If the number already exists in the set, a loop is detected, and it returns `false`.

---

## 🚀 Section 2: Code Optimization (Floyd's Cycle-Finding)

Instead of maintaining a Hash Set which consumes auxiliary memory, we can drastically optimize the space complexity by applying **Floyd's Cycle-Finding Algorithm (Slow & Fast Pointers)**.

- **Slow Pointer:** Moves 1 step at a time ($f(x)$).
- **Fast Pointer:** Moves 2 steps at a time ($f(f(x))$).
- If they meet at `1`, it's a happy number. If they meet at any other number, a cycle is detected without using any extra memory container!

### 📊 Complexity Comparison
| Approach | Time Complexity | Space Complexity |
| :--- | :--- | :--- |
| **Hash Set** | $O(\log n)$ | $O(\log n)$ |
| **Two Pointers (Optimized)** | $O(\log n)$ | $O(1)$ (Strictly Optimized!) |

---

## 🔍 Section 3: Bug Hunting & Debug Strategy

During the implementation, several critical logical issues were encountered and resolved:
1. **Infinite Loops:** Forgetting to store results in the set or missing the slow/fast pointer update, causing the program to hang on non-happy numbers.
2. **Digit Logic Errors:** Using `n / 10` before `n % 10`, or forgetting to update `n /= 10` inside the loop, leading to incorrect calculations.
3. **Syntax (C++):** Forgetting the template type declaration for `std::unordered_set<int>`.

---

## 🔗 Section 4: Resource Sharing
- **My LeetCode Solution:** [Link to your LeetCode post]
- **Academic Reference:** Cross-referenced from my university Padlet portfolio.
