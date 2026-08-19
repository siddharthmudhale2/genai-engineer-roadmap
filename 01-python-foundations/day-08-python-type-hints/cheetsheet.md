# ⚡ Day 8 — Python Type Hints

> **Phase:** Python Foundations  
> **Topic:** Type Hints  
> **Status:** ⏳ In Progress

---

## 📖 Quick Definitions

| Concept | Definition |
|---|---|
| **Type Hint** | An optional annotation that specifies the expected data type of a variable, parameter, or return value. |
| **Variable Annotation** | A type hint attached to a variable. |
| **Parameter Annotation** | A type hint specifying the expected type of a function parameter. |
| **Return Type Annotation** | A type hint specifying the expected type returned by a function. |
| **`Any`** | Indicates that a value can be of any type. |
| **`Optional`** | Indicates that a value can be a specified type or `None`. |
| **`Union`** | Indicates that a value can be one of several specified types. |
| **Type Alias** | A reusable name given to a type annotation. |
| **`TypedDict`** | Used to describe the expected keys and value types of a dictionary. |
| **Static Type Checking** | Analyzing code for type-related problems without executing it. |

---

# 🐍 Basic Type Hint

## Syntax

```python
variable: type = value