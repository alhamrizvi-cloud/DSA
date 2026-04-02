# Time Complexity

## 1. The Common Misconception
A common mistake is defining **Time Complexity** as the literal time (in seconds or milliseconds) it takes to run a piece of code.

### Why is "Time Taken" wrong?
1.  **Hardware Dependency:** The same code might take **5 seconds** on a modern MacBook but **15 seconds** on an older i7 Dual Core processor.
2.  **External Factors:** Execution time also depends on the current server load or other background processes running on the machine.


---

## 2. The Real Definition
**Time Complexity** is the **rate of increase in time** required by an algorithm with respect to the **increase in input size ($n$)**.

* As the value of $n$ increases, how does the number of operations grow?
* If $n$ goes up, the rate of operations goes up accordingly.

---

## 3. Big-O Notation ($O$)
Time complexity is calculated using **Big-O Notation**, which focuses on the total number of operations performed by the code rather than the clock time.

### Example: Basic Loop
```python
# Python Example
for i in range(1, 6):
    print("hello")
```

**Step-by-step Operations:**
1.  **Initialization:** `i = 1` (1 operation)
2.  **Comparison:** `i < 6` (checked every iteration)
3.  **Execution:** `print("hello")` (1 operation)
4.  **Increment:** `i` increases (1 operation)

In your notes, for a fixed range like 1 to 6, this results in a constant number of operations. However, when we introduce a variable $n$, the growth becomes linear.

---

## 4. Rules for Calculating Time Complexity
To simplify $TC$ and focus on scalability, we follow these three rules:

1.  **Always calculate for the Worst Case:** Prepare for the scenario where the algorithm takes the maximum number of steps.
2.  **Avoid Constant Values:** In Big-O, we drop constants. For example, $O(3n)$ is simplified to $O(n)$.
3.  **Ignore Lower Order Bounds:** We only care about the fastest-growing term. $O(n^2 + n)$ becomes $O(n^2)$.

### Example: Variable Input
```python
# What if the range is (1, n + 1)?
for i in range(1, n + 1):
    print("hello")
```
If we count the operations (Compare + Increment + Print), we might get $3 \times n$ operations. According to the rules, we drop the constant **3**, making the Time Complexity **$O(n)$**.

---

## 5. Why Always Calculate the "Worst Case"?
Consider a program that checks age categories:
```python
if age >= 80:
    print("Senior")
elif age >= 60:
    print("Senior-Mid")
# ... many more conditions ...
else:
    print("Teen")
```

* **Best Case:** The first condition is met (`age = 85`). The code stops after 2 operations.
* **Worst Case:** None of the conditions match until the very last `else`.

**Why we focus on the Worst Case:**
It provides a **guarantee**. If a developer knows the code performs efficiently even in the worst-case scenario (e.g., maximum server load or largest possible input), the system is considered reliable and scalable.

Here is the updated content for your repository, incorporating the new rules, notations, and the introduction to space complexity.

---

## Rule 2: Ignore Constants and Lower-Order Terms
When calculating Big-O, we only care about the term that grows the fastest as $n$ approaches infinity.

**Example:** $TC = O(8n^6 + 3n^2 + 15)$
1.  **Drop Constants:** The $+15$ is a fixed number. As $n$ becomes massive (like $10^6$), 15 becomes irrelevant.
2.  **Drop Coefficients:** The multiplier $8$ is a constant. We focus on the rate of growth, so $8n^6$ is simplified to $n^6$.
3.  **Ignore Lower-Order Bounds:** $n^6$ grows much faster than $n^2$. For very large inputs, the $n^2$ term contributes almost nothing to the total time compared to $n^6$.

**Final Time Complexity:** $O(n^6)$

---

## Types of Time Complexity
In interviews and academic theory, we use three main notations to describe the bounds of an algorithm:

| Notation | Bound | Case | Description |
| :--- | :--- | :--- | :--- |
| **Big-O ($O$)** | Upper Bound | **Worst Case** | The algorithm will **never** take more time than this. |
| **Theta ($\Theta$)** | Tight Bound | **Average Case** | The actual/exact growth rate of the algorithm. |
| **Omega ($\Omega$)** | Lower Bound | **Best Case** | The algorithm will take **at least** this much time. |

---

## Nested Loops and $O(n^2)$

### Example 1: Independent Nested Loop
```python
for i in range(1, n + 1):       # Runs n times
    for j in range(1, n + 1):   # Runs n times for every i
        print(i, j)
```
Total operations: $n \times n = n^2$.
**Time Complexity:** $O(n^2)$

### Example 2: Dependent Nested Loop
```python
for i in range(1, n + 1):
    for j in range(1, i + 1): # j depends on the current value of i
        print("hello")
```
**Calculation:**
* When $i=1$, $j$ runs 1 time.
* When $i=2$, $j$ runs 2 times.
* ...
* When $i=n$, $j$ runs $n$ times.

Total operations = $1 + 2 + 3 + \dots + n = \frac{n(n+1)}{2}$
Expanding this, we get: $\frac{n^2 + n}{2} \rightarrow \frac{1}{2}n^2 + \frac{1}{2}n$
Applying **Rule 2** (ignore constants and lower terms):
**Time Complexity:** $O(n^2)$
