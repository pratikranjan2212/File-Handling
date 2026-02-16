# File Handling in Python

## Overview
File handling is a core skill in Python that allows you to read, write, and manipulate files on your system. Python provides built-in functions and methods to work with files efficiently.

## Opening Files

### Basic Syntax
```python
file = open("filename.txt", "mode")
```

### File Modes
"r" - Read (default). Opens file for reading; file must exist.
"a" - Append. Opens file for appending; creates file if it doesn't exist.
"w" - Write. Opens file for writing; creates or overwrites file.
"x" - Create. Creates a new file; fails if file already exists.
"b" - Binary mode (combine with other modes: "rb", "wb").
"t" - Text mode (default; combine with other modes: "rt", "wt").
"+" - Read and write (combine: "r+", "w+", "a+").
