# 0x06. Python - Classes and Objects

This directory is part of the `alu-higher_level_programming` repository. It introduces the basics of object-oriented programming in Python by building a `Square` class step by step.

## Learning Objectives

- What a class is and how to define one
- What an instance is and how to create one
- What `__init__` does
- What a private attribute is and how name mangling works (`__size` becomes `_Square__size`)
- How to validate the type and value of an attribute at instantiation
- How to raise `TypeError` and `ValueError` with custom messages

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files are interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- All files must end with a new line
- The first line of every file must be exactly `#!/usr/bin/python3`
- Code should follow the `pycodestyle` style (version 2.7.*)
- All files must be executable
- You are not allowed to import any module

## Files

| File | Description |
|------|-------------|
| `0-square.py` | Empty class `Square` that defines a square |
| `1-square.py` | `Square` with a private instance attribute `size`, set at instantiation (no type/value verification) |
| `2-square.py` | `Square` with an optional `size=0`; raises `TypeError("size must be an integer")` if `size` is not an integer and `ValueError("size must be >= 0")` if `size` is negative |

## Usage

Each task has a matching `*-main.py` test file. Make the files executable and run them:

```bash
chmod u+x *.py
./2-main.py
```

## Author

Cecilia
