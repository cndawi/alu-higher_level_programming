
# Python - Data Structures

This directory contains my solutions to the Python data structures project from the `alu-higher_level_programming` repository.

## Requirements

- Python 3 (tested on Ubuntu)
- Files start with `#!/usr/bin/python3`
- Files are executable (`chmod +x`)
- No imports allowed unless stated in the task

## Tasks

### 0. Print a list of integers
**File:** `0-print_list_integer.py`

A function that prints all integers of a list, one per line.

- Prototype: `def print_list_integer(my_list=[]):`
- Uses `str.format()` to print integers
- No casting integers into strings, no module imports

**Example:**

```
$ cat 0-main.py
#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_
