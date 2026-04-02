## Space Complexity
**Space Complexity** is the total memory used by an algorithm relative to the input size. Like time complexity, it is expressed in Big-O notation.

### The Formula
$$\text{Total Space} = \text{Auxiliary Space} + \text{Input Space}$$

* **Input Space:** The memory required to store the initial input data (e.g., an array of size $n$).
* **Auxiliary Space:** The extra or temporary space used by the algorithm to solve the problem.

**Best Practice:** Do not modify the original input unless specifically asked to do so. A "clean" algorithm solves the problem using minimal auxiliary space.

### Common Space Complexities:
* **Variables:** `x = 5, y = 10` $\rightarrow O(1)$ (Constant Space)
* **Arrays/Lists:** A list of size $n$ $\rightarrow O(n)$ (Linear Space)

---

Would you like me to create a **cheat sheet table** of common complexities ($O(1), O(\log n), O(n), O(n^2)$) with real-world code examples for your repo?
