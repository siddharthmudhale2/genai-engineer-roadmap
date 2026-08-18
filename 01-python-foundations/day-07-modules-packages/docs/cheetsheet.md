# ⚡ Day 7 — Python Modules & Packages

> **Phase:** Python Foundations  
> **Status:** ✅ Completed

---

## 📖 Quick Definitions

| Concept | Definition |
|---|---|
| **Module** | A Python `.py` file containing reusable code such as functions, classes, and variables. |
| **Package** | A directory used to organize related Python modules. |
| **`import`** | Loads a module or package so its functionality can be used. |
| **`from ... import ...`** | Imports specific objects from a module or package. |
| **Alias** | An alternative name assigned to an imported module or object. |
| **`__init__.py`** | A special file commonly used to initialize and define a regular Python package. |
| **`__name__`** | A special variable containing the name under which the current module is being executed. |
| **`__main__`** | The value of `__name__` when a Python file is executed directly. |
| **Absolute Import** | An import that specifies the complete package path. |
| **Relative Import** | An import that refers to a module relative to the current package. |

---

# 📦 Module

A module is a Python file containing reusable code.

Example:

```text
calculator.py