# Word Square Challenge

## Overview

This project solves the **Word Square Challenge**: given an integer `n` and `n²` letters, the program finds valid English word squares of size `n`.
It is implemented in **Python 3** with an **object-oriented design** and includes **unit tests** to demonstrate correctness.

---

## Project Structure

```
Word Square Challenge/
├── word_square_solver.py      # main solver code
├── enable1.txt                # optional local wordlist
├── tests/                     # unit tests
│   └── test_word_square_solver.py
├── requirements.txt           # Python dependencies
└── README.md
```

* `word_square_solver.py` – contains the `WordSquareSolver` class and CLI logic.
* `tests/` – contains pytest unit tests for core functionality.
* `enable1.txt` – optional local copy of Norvig's enable1 wordlist.
* `requirements.txt` – dependencies (e.g., pytest).

---

## Setup Instructions

It is recommended to use a **virtual environment** to isolate dependencies.

1. **Create a virtual environment**

```bash
python3 -m venv venv
```

2. **Activate the virtual environment**

```bash
# macOS / Linux
source venv/bin/activate

# Windows (PowerShell)
venv\Scripts\Activate.ps1
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## Running the Solver

The solver can be run directly from the command line:

```bash
python word_square_solver.py
```

By default, it will run the built-in challenge inputs:

```
4 aaccdeeeemmnnnoo
5 aaaeeeefhhmoonssrrrrttttw
5 aabbeeeeeeeehmosrrrruttvv
7 aaaaaaaaabbeeeeeeedddddggmmlloooonnssssrrrruvvyyy
```

Output will display valid word squares for each input.

---

## Using a Custom Input

You can modify the input inside the `main()` function or adapt the CLI to accept user input.

Example:

```python
n = 4
letters = "eeeeddnnrssrv"
solver = WordSquareSolver()
solutions = solver.solve(letters, n)
for sol in solutions:
    for row in sol:
        print(row)
```

---

## Running Tests

Unit tests are written using **pytest**.

From the project root:

# Run all tests
pytest

# Run with verbose output
pytest -v


Tests cover:

* Wordlist loading
* Candidate filtering
* Prefix map building

---

## Notes

* The solver uses a **prefix map optimization** to efficiently prune the search space.
* No 2D arrays are used; rows are represented as strings.
* Ensure Python 3.11+ (or compatible) is used.
* For reproducibility, it is recommended to keep `enable1.txt` locally, though the program can also download it automatically.

---

## References

* [Enable1 Wordlist by Peter Norvig](http://norvig.com/ngrams/enable1.txt)
