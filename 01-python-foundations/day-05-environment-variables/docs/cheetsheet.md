# ⚡ Day 5 — Environment Variables & API Secrets

> **Phase:** Python Foundations  
> **Status:** ✅ Completed

---

## 📖 Quick Definitions

| Concept | Definition |
|---|---|
| **Environment Variable** | A configuration value supplied to a process through its environment instead of being hard-coded in source code. |
| **`os`** | Python standard-library module for interacting with the operating system. |
| **`os.environ`** | Dictionary-like mapping containing environment variables available to the process. |
| **`os.getenv()`** | Retrieves an environment variable and returns `None` if it doesn't exist by default. |
| **`.env`** | Local configuration file commonly used to store environment-variable values during development. |
| **`python-dotenv`** | Python package used to load variables from a `.env` file. |
| **`load_dotenv()`** | Loads variables from `.env` into the process environment. |
| **`.gitignore`** | Git file that specifies files and directories that should normally be ignored. |
| **`.env.example`** | Safe template showing required environment variables without containing real secrets. |
| **API Key** | A credential used to authenticate an application when accessing an API. |

---

# 🔐 Why Environment Variables?

Never hard-code secrets:

```python
API_KEY = "real-secret-key"
```

Instead:

```python
import os

API_KEY = os.getenv("API_KEY")
```

Conceptually:

```text
Environment
     ↓
API_KEY
     ↓
Python Application
     ↓
External API
```

---

# 🐍 `os`

## Definition

`os` is a Python standard-library module that provides interfaces for interacting with the operating system.

```python
import os
```

No installation is required.

---

# 🔹 `os.environ`

Access an environment variable:

```python
import os

api_key = os.environ["API_KEY"]
```

If the variable doesn't exist, this can raise:

```text
KeyError
```

---

# 🔹 `os.getenv()`

Retrieve an environment variable:

```python
import os

api_key = os.getenv("API_KEY")
```

If the variable doesn't exist:

```text
None
```

---

# 🔄 `os.environ` vs `os.getenv()`

| `os.environ` | `os.getenv()` |
|---|---|
| Mapping-like object | Function |
| `os.environ["KEY"]` | `os.getenv("KEY")` |
| Missing key can raise `KeyError` | Missing key returns `None` by default |
| Direct access | Convenient retrieval |

---

# 📄 `.env`

Example:

```text
API_KEY=my-demo-secret
APP_ENV=development
```

The `.env` file is commonly used for local development configuration.

⚠️ Do not commit real `.env` files containing secrets to GitHub.

---

# 📦 `python-dotenv`

Install:

```powershell
pip install python-dotenv
```

Import:

```python
from dotenv import load_dotenv
```

Load `.env`:

```python
load_dotenv()
```

Read the variable:

```python
import os

api_key = os.getenv("API_KEY")
```

Complete pattern:

```python
import os

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
```

---

# 🚫 `.gitignore`

Create:

```text
.gitignore
```

Example:

```text
.env
__pycache__/
*.pyc
venv/
.venv/
```

This prevents Git from normally tracking these files.

---

# 📋 `.env.example`

Example:

```text
API_KEY=
APP_ENV=development
```

It documents the required configuration without exposing the real secret.

---

# 🔄 `.env` vs `.env.example`

| `.env` | `.env.example` |
|---|---|
| Contains real local values | Contains placeholders |
| Private | Safe to commit |
| Usually ignored | Usually committed |
| Used by application | Used as configuration template |

---

# 🛡️ Secret-Safe Pattern

### ❌ Bad

```python
API_KEY = "sk-real-secret"
```

### ✅ Good

```python
import os

API_KEY = os.getenv("API_KEY")
```

### Better validation

```python
import os

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY is not configured")
```

---

# ⚠️ Never Print Secrets

❌ Don't:

```python
print(API_KEY)
```

✅ Do:

```python
if API_KEY:
    print("API key loaded successfully")
else:
    print("API key missing")
```

---

# 🤖 GenAI Connection

GenAI applications may require:

```text
OPENAI_API_KEY
GEMINI_API_KEY
ANTHROPIC_API_KEY
HUGGINGFACE_TOKEN
VECTOR_DB_API_KEY
DATABASE_URL
```

Keep credentials outside source code.

```text
.env / Secret Manager
          ↓
     Environment
          ↓
     Python App
          ↓
       AI API
```

---

# 🚨 If a Secret Is Leaked

Immediately:

1. Revoke the exposed credential.
2. Generate a new credential.
3. Remove the secret from the project.
4. Check Git history if necessary.
5. Update the application.
6. Never reuse the leaked credential.

Deleting the secret from the latest file does not necessarily remove it from Git history.

---

# 💼 Interview Questions

### What is an environment variable?

A configuration value provided through the process environment instead of being hard-coded in source code.

### Why shouldn't API keys be hard-coded?

Because source code can be shared or committed to a public repository, exposing the credential.

### What is `.env`?

A local configuration file commonly used to store environment-variable values during development.

### What does `load_dotenv()` do?

It loads variables from a `.env` file into the process environment.

### What is `.gitignore`?

A Git configuration file that specifies files and directories that Git should normally ignore.

### What is `.env.example`?

A template documenting required environment variables without exposing their real values.

### Difference between `os.environ` and `os.getenv()`?

`os.environ["KEY"]` can raise `KeyError` when the variable doesn't exist, while `os.getenv("KEY")` returns `None` by default.

### Should `.env` be committed to GitHub?

Not when it contains real secrets.

---

# 📌 Quick Revision

```text
Environment Variable
        ↓
External Configuration

.env
        ↓
Local Configuration

python-dotenv
        ↓
Loads .env

load_dotenv()
        ↓
Loads Variables

os.getenv()
        ↓
Reads Variables

.gitignore
        ↓
Keeps .env Out of Git

.env.example
        ↓
Safe Configuration Template
```

---

# 🎯 Key Takeaways

- ✅ Never hard-code API keys.
- ✅ Use environment variables for configuration and secrets.
- ✅ Use `.env` for local development.
- ✅ Keep `.env` in `.gitignore`.
- ✅ Use `.env.example` as a safe template.
- ✅ Use `python-dotenv` to load `.env`.
- ✅ Validate required configuration.
- ✅ Never print or expose real secrets.
- ✅ Rotate credentials immediately if they are leaked.
- ✅ These practices are essential for production GenAI applications.