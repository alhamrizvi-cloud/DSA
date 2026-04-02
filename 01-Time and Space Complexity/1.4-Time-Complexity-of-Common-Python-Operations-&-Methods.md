# Python Data Structures: Time Complexity Reference

This document outlines the Big O time complexity for common operations on built-in Python data structures, including Lists, Sets, and Dictionaries.

## 1. Lists
Python lists are dynamic arrays. Operations that happen at the end of the list are generally faster than those that require shifting elements.

| Operation | Average Case | Worst Case | Notes |
| :--- | :--- | :--- | :--- |
| **Copy** | $O(n)$ | $O(n)$ | Requires traversing the whole list. |
| **Append** | $O(1)$ | $O(1)$ | Amortized constant time. |
| **Pop last** | $O(1)$ | $O(1)$ | Removing from the end requires no shifting. |
| **Pop intermediate** | $O(n)$ | $O(n)$ | Requires shifting all subsequent elements. |
| **Get Item** | $O(1)$ | $O(1)$ | Direct access via index. |
| **Set Item** | $O(1)$ | $O(1)$ | Index-based assignment. |
| **Delete Item** | $O(n)$ | $O(n)$ | Requires shifting elements to fill the gap. |
| **Insert** | $O(n)$ | $O(n)$ | Requires shifting elements to make room. |
| **Iteration** | $O(n)$ | $O(n)$ | Proportional to list length. |
| **Get Slice** | $O(k)$ | $O(k)$ | $k$ is the length of the slice. |
| **Del Slice** | $O(n)$ | $O(n)$ | Shifts remaining items after deletion. |
| **Set Slice** | $O(n+k)$ | $O(n+k)$ | $k$ is the length of the new slice. |
| **Extend** | $O(k)$ | $O(k)$ | $k$ is the length of the added list. |
| **Sort** | $O(n \log n)$ | $O(n \log n)$ | Uses Timsort. |
| **Membership (x in s)**| $O(n)$ | $O(n)$ | Linear search through the list. |
| **Min/Max** | $O(n)$ | $O(n)$ | Must check every element. |
| **Length** | $O(1)$ | $O(1)$ | Python stores the size as a property. |

---

## 2. Sets
Sets are implemented using Hash Tables, making lookups extremely fast.

| Operation | Average Case | Worst Case | Notes |
| :--- | :--- | :--- | :--- |
| **Membership (x in s)**| $O(1)$ | $O(n)$ | Constant time unless there are hash collisions. |
| **Length** | $O(1)$ | $O(1)$ | Constant time access. |

---

## 3. Dictionaries
Dictionaries store data as Key-Value pairs using a Hash Table.

| Operation | Average Case | Amortized Worst Case |
| :--- | :--- | :--- |
| **Get Item** | $O(1)$ | $O(n)$ |
| **Set Item** | $O(1)$ | $O(n)$ |
| **Delete Item** | $O(1)$ | $O(n)$ |
| **Copy** | $O(n)$ | $O(n)$ |
| **Iteration** | $O(n)$ | $O(n)$ |

> **Note on Amortized Time:** In dictionaries and sets, "Worst Case" $O(n)$ is very rare in modern Python. It only occurs if the hash function is poor and causes significant "collisions" where many keys map to the same spot.

---

### Key Concepts

* **Shifting:** When you delete or insert in the middle of a list, Python has to physically move every item after that index one spot over. This is why these operations are $O(n)$.
* **Hash Tables:** Dictionaries and Sets use hashing to find values instantly, which is why they are generally preferred for membership checks over lists.
