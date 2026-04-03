# 🟢 PART 1 — Concept Building (Solid Basics)
Time: 2 hours

## 1️⃣ Sum of Digits

### ❓ Task:

Given `n`, return the **sum of its digits**

### 💡 Example:

```text
Input: 5873
Output: 5+8+7+3 = 23
```

## 2️⃣ Product of Digits

### ❓ Task:

Return the **product of digits**

### 💡 Example:

```text
Input: 234
Output: 2*3*4 = 24
```

---

## 3️⃣ Count Even & Odd Digits

### ❓ Task:

Count how many digits are **even** and **odd**

### 💡 Example:

```text
Input: 123456
Output: even = 3, odd = 3
```

# 🟡 PART 2 — Tricky (this will level you up)

## 4️⃣ Reverse Only Half Number

### ❓ Task:

Reverse only **half of the digits** and compare with other half

👉 Basically optimized palindrome check

### 💡 Hint:

* Stop loop when `rev >= num`

---

## 5️⃣ Check Strong Number

### ❓ Task:

A number is **Strong** if:
[
sum(factorial of digits) = number
]

### 💡 Example:

```text
Input: 145
1! + 4! + 5! = 1 + 24 + 120 = 145 ✅
```

---

## 6️⃣ Remove One Digit to Make Palindrome

### ❓ Task:

Return `True` if you can remove **exactly one digit** to make it palindrome

### 💡 Example:

```text
Input: 12321 → True (already palindrome)
Input: 1231 → remove 2 → 131 → True
Input: 1234 → False
```

---

# 🚀 How to solve (IMPORTANT)

For ALL problems use:

```python
digit = n % 10
n = n // 10
```

# ⚡ Difficulty Flow

```text
1 → basic loop
2 → same logic
3 → condition building
4 → optimization thinking
5 → math + loops
6 → real interview logic
```
