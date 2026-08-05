What is Python?
Definition

Python is a high-level, interpreted, general-purpose programming language widely used in Artificial Intelligence, Machine Learning, Data Science, Web Development, Automation, and Backend Development.

Interview Definition

Python is an interpreted, object-oriented, high-level programming language known for its simplicity, readability, and extensive ecosystem, making it one of the most popular languages for AI and software development.

Why Python for Generative AI?

Python dominates the AI ecosystem because most modern AI libraries are built for Python.

Examples:

NumPy
Pandas
Scikit-Learn
TensorFlow
PyTorch
Hugging Face Transformers
LangChain
LangGraph
OpenAI SDK
FastAPI

Instead of reinventing the wheel, Python lets us use mature, well-supported libraries.

What is PyPI?
Definition

PyPI (Python Package Index) is the official repository of Python packages.

Think of it as an App Store for Python libraries.

Interview Definition

PyPI is the official package repository that hosts and distributes Python packages for installation using package managers such as pip.

Why Do We Need PyPI?

Imagine writing every library yourself.

Need HTTP requests?

Write thousands of lines.

Need AI?

Write PyTorch yourself.

Impossible.

Instead:

pip install requests

downloads the library from PyPI.

What is pip?
Definition

pip is Python's package manager.

It installs libraries from PyPI.

Syntax
pip install package_name

Example:

pip install pandas
Common Commands

Install:

pip install requests

Upgrade:

pip install --upgrade requests

List packages:

pip list

Freeze:

pip freeze
What is a Virtual Environment?
Definition

A Virtual Environment is an isolated Python environment that contains its own Python interpreter and installed packages.

Each project can have different library versions without conflicts.

Interview Definition

A virtual environment is an isolated workspace that keeps a project's dependencies separate from other Python projects and the global Python installation.

Why Do We Need It?

Suppose:

Project A

Needs:

OpenAI 1.90

Project B

Needs:

OpenAI 2.x

Without a virtual environment:

Both projects share the same installation.

Version conflicts occur.

With a virtual environment:

Each project has its own dependencies.

Real-World Analogy

Think of a virtual environment as separate kitchens.

Restaurant A

Uses Indian spices.

Restaurant B

Uses Italian spices.

Each kitchen has its own ingredients.

They don't interfere.

Industry Usage

Every professional AI project uses virtual environments.

Examples:

OpenAI SDK
FastAPI
LangChain
Hugging Face
CrewAI
PyTorch
Common Mistakes

❌ Installing packages globally.

❌ Committing venv/ to GitHub.

❌ Forgetting to activate the environment.

Best Practices

✅ One virtual environment per project.

✅ Commit requirements.txt.

✅ Ignore venv/.

Revision Notes
pip installs packages.
PyPI hosts packages.
Virtual environments isolate dependencies.
Use one virtual environment per project.