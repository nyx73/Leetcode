# Q1. Can Make Arithmetic Progression From Sequence

## 🧩 Problem

A sequence is called an **Arithmetic Progression (AP)** if the difference between consecutive elements is constant.

Given an array `arr`, return `true` if it can be rearranged to form an arithmetic progression. Otherwise, return `false`.

---

## 💡 Key Insight

If the array can form an AP, then after sorting:


arr[i] - arr[i-1] should be same for all i


---

## 🧠 Approach

### Step 1: Sort the array
- This ensures elements are in order

### Step 2: Compute common difference

diff = arr[1] - arr[0]


### Step 3: Check all consecutive differences
- If any difference is not equal → return `False`

---

## ✅ Python Solution

```python
class Solution:
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        
        diff = arr[1] - arr[0]
        
        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] != diff:
                return False
        
        return True
```

🧪 Example 1
Input:
arr = [3,5,1]
Sorted:
[1,3,5]
Differences:
3 - 1 = 2  
5 - 3 = 2  ✅
``` id="ex1d"
```
### Output:
```  id="ex1o"
```
True
🧪 Example 2
Input:
arr = [1,2,4]
Sorted:
[1,2,4]
Differences:
2 - 1 = 1  
4 - 2 = 2  ❌
``` id="ex2d"
```
### Output:
```
 id="ex2o"
```
False
⏱️ Complexity
Type	Complexity
Time	O(n log n) (sorting)
Space	O(1)
🚀 Pro Tip

Whenever you see:

"rearrange to satisfy condition"

👉 Think:

🔁 Sort first, then validate pattern

🔥 Bonus (O(n) Approach Idea)

You can optimize further:

Use min, max
Check if (max - min) % (n - 1) == 0
Use a set to verify all expected values exist

(No sorting needed!)

# Q 2. Find Pivot Integer

## 🧩 Problem

Given a positive integer `n`, find an integer `x` such that:


sum(1 → x) == sum(x → n)


Return the pivot integer `x`.  
If no such integer exists, return `-1`.

---

## 💡 Key Insight

We know:


Total sum from 1 to n = n(n + 1) / 2


Let pivot = `x`

Then:

sum(1 → x) = x(x + 1) / 2
sum(x → n) = total_sum - sum(1 → x-1)


Instead of complicating, use a simpler idea 👇

---

## 🧠 Mathematical Trick

We want:

1 + 2 + ... + x = x + ... + n


This simplifies to:

x² = total_sum


👉 So:

x = √(n(n + 1) / 2)


---

## ✅ Approach

1. Compute:

total = n(n + 1) / 2

2. Check if `total` is a perfect square
3. If yes → return √total  
4. Else → return -1

---

## ✅ Python Solution (Optimal)

```python
class Solution:
 def pivotInteger(self, n: int) -> int:
     total = n * (n + 1) // 2
     
     x = int(total ** 0.5)
     
     if x * x == total:
         return x
     
     return -1
```

🧪 Example 1
Input:
n = 8
Total:
8 × 9 / 2 = 36
``` id="ex1calc"
```
### Check:

√36 = 6 ✅


### Output:
``` id="ex1out"
```
6
🧪 Example 2
Input:
n = 4
Total:
4 × 5 / 2 = 10
``` id="ex2calc"
```
### Check:

√10 ≠ integer ❌


### Output:
``` id="ex2out"
```
-1
⏱️ Complexity
Type	Complexity
Time	O(1)
Space	O(1)
🚀 Pro Tip

Whenever you see:

Sum of ranges
Equal partition

👉 Try converting to math equation instead of loops

This often reduces:

O(n) → O(1) ⚡

# Q3. Palindrome Number

## 🧩 Problem

Given an integer `x`, return `true` if `x` is a palindrome, otherwise return `false`.

A palindrome reads the same forward and backward.

---

## 💡 Examples

### Example 1

Input: x = 121
Output: true


### Example 2

Input: x = -121
Output: false


### Example 3

Input: x = 10
Output: false


---

## ⚠️ Key Observations

- Negative numbers are **not palindrome** ❌  
- Numbers ending with `0` (except `0` itself) are **not palindrome** ❌  

---

## 🧠 Approach 1: Convert to String (Easy)

### Idea:
- Convert number to string
- Compare with reversed string

---

### ✅ Python Code

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
```
🚀 Approach 2: Without Converting to String (Optimal)
💡 Idea

Reverse only half of the number:

Example:

12321 → reverse half → 123 | 21

Compare:

First half == reversed second half
🔁 Steps
If x < 0 → return False
If x % 10 == 0 and x != 0 → return False
Reverse half of number
Compare halves

### ✅ Python Code (Optimal)
```
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # For even digits: x == reversed_half
        # For odd digits: x == reversed_half // 10
        return x == reversed_half or x == reversed_half // 10
```
🧪 Example Walkthrough
Input:
x = 121

Steps:

x = 12, reversed = 1  
x = 1,  reversed = 12

Compare:

1 == 12 // 10 → 1 == 1 ✅
⏱️ Complexity
Type	Complexity
Time	O(log₁₀ n)
Space	O(1)
🔥 Pro Tip

Whenever you see:

Reverse number
Digit operations

👉 Prefer math-based solution over string for:

Better performance
Interview advantage 💯
