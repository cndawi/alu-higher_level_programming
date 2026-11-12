# 0x0A. Python - Inheritance

This directory is part of the `alu-higher_level_programming` repository. It covers inheritance in Python: how classes inherit from other classes, and how to inspect objects and their classes.

## Learning Objectives

- What a superclass, base class, or parent class is
- What a subclass is
- How to list all attributes and methods of a class or an object (`dir()`)
- When an instance is exactly of a class, and when it is of a class or one of its parents
- The difference between `type()`, `isinstance()`, and `issubclass()`
- How to inherit from a built-in class such as `list`
- How to write doctests in a text file

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files are interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- All files must end with a new line
- The first line of every file must be exactly `#!/usr/bin/python3`
- Code should follow the `pycodestyle` style (version 2.7.*)
- All files must be executable
- All modules, classes, and functions must be documented with docstrings
- You are not allowed to import any module

## Files

| File | Description |
|------|-------------|
| `0-lookup.py` | Function `lookup(obj)` that returns the list of available attributes and methods of an object |
| `1-my_list.py` | Class `MyList` that inherits from `list` and has `print_sorted()`, which prints the list sorted in ascending order |
| `tests/1-my_list.txt` | Doctests for `1-my_list.py` |
| `2-is_same_class.py` | Function `is_same_class(obj, a_class)` that returns `True` if the object is exactly an instance of the specified class, otherwise `False` |
| `3-is_kind_of_class.py` | Function `is_kind_of_class(obj, a_class)` that returns `True` if the object is an instance of, or inherits from, the specified class, otherwise `False` |
| `4-inherits_from.py` | Function `inherits_from(obj, a_class)` that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class, otherwise `False` |

## Usage

Each task has a matching `*-main.py` test file. Make the files executable and run them:

```bash
chmod u+x *.py
./1-main.py
```

Run the doctests for `1-my_list.py`:

```bash
python3 -m doctest -v ./tests/1-my_list.txt
```

Example (`1-main.py`):

```python
#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)
```

Output:

```
[1, 4, 2, 3, 5]
[1, 2, 3, 4, 5]
[1, 4, 2, 3, 5]
```

## Author

cecilia

