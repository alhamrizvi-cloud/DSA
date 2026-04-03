# 🔢 Reversing a Number

## 🧠 Core Logic (Mathematics)

We use basic number properties:

* **Last digit extraction**:
  `last_digit = n % 10`
  → gives the rightmost digit

* **Remove last digit**:
  `n = n // 10`
  → removes the rightmost digit

* **Build reversed number**:
  `rev = rev * 10 + last_digit`
  → shifts digits left and adds new digit

---

### 📌 Example

For `n = 1234`

| Step | n    | last_digit | rev      |
| ---- | ---- | ---------- | -------- |
| 1    | 1234 | 4          | 0→4      |
| 2    | 123  | 3          | 4→43     |
| 3    | 12   | 2          | 43→432   |
| 4    | 1    | 1          | 432→4321 |

---

## 🐍 Python Code

```python
def reverse_number(n):
    num = n
    rev = 0

    while num > 0:
        digit = num % 10
        rev = (rev * 10) + digit
        num = num // 10

    return rev
```

---

## 🔁 Check Palindrome

```python
def is_palindrome(n):
    num = n
    rev = 0

    while num > 0:
        digit = num % 10
        rev = (rev * 10) + digit
        num = num // 10

    return n == rev
```

---

## ⏱️ Time Complexity

### Logic:

* Each loop removes **1 digit**
* If number has `d` digits → loop runs `d` times

### Math:

* Number of digits in `n` = **log₁₀(n)**

### ✅ Final:

```
Time Complexity = O(log10(n))
```

---

## 💾 Space Complexity

* We only use:

  * `num`
  * `rev`
  * `digit`

* No extra data structures

### ✅ Final:

```
Space Complexity = O(1)
```

---

## ⚡ Quick Summary

* `% 10` → get last digit
* `// 10` → remove last digit
* `rev = rev * 10 + digit` → build reverse
* Time → `O(log n)`
* Space → `O(1)`
