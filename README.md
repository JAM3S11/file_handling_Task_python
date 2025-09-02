# file_handling_Task_python

This repository is designed to help you learn and demonstrate your understanding of file handling in Python through a series of practical tasks. 

## Overview

Python provides powerful tools for working with files, allowing you to create, read, write, append, and handle errors gracefully. File handling is an essential skill for any Python developer, as it enables you to store, retrieve, and manipulate data efficiently.

## Tasks Breakdown

### 1. File Creation

- **Objective:** Learn how to create and write to a file in Python.
- **Instructions:**  
  Create a Python script named `file_handling_assignment.py`.  
  In the script:
  - Open (or create if it doesn't exist) a text file called `my_file.txt` in write mode (`'w'`).
  - Write at least three lines to the file. Each line should be a mix of strings and numbers to demonstrate different data types.
  - Close the file after writing.

### 2. File Reading and Display

- **Objective:** Practice reading and displaying file content.
- **Instructions:**  
  - Open `my_file.txt` in read mode (`'r'`).
  - Read the contents of the file.
  - Display each line on the console.
  - Handle the file closing appropriately.

### 3. File Appending

- **Objective:** Learn how to append data to an existing file without overwriting its contents.
- **Instructions:**  
  - Open `my_file.txt` in append mode (`'a'`).
  - Add (append) three more lines of text to the file.
  - Ensure the previous content is preserved.
  - Close the file after appending.

### 4. Error Handling

- **Objective:** Understand how to manage common file-related exceptions in Python.
- **Instructions:**  
  - Use `try`, `except`, and `finally` blocks to handle potential exceptions such as:
    - `FileNotFoundError`: Raised when the file does not exist.
    - `PermissionError`: Raised when there are insufficient permissions to perform file operations.
    - Any other relevant exceptions.
  - Ensure that files are closed properly, even if an error occurs.

## Example Structure

Your final script should demonstrate:
- Clear comments explaining each operation.
- Robust error handling.
- Proper resource management using `with` statements or explicit `close()` calls.
- Output that confirms each step (e.g., prints statements after writing, reading, and appending).

## Getting Started

1. Clone this repository.
2. Create the required script (`file_handling_assignment.py`).
3. Follow the task breakdown above.
4. Run your script and observe the results on the console.

## Additional Resources

- [Python File Handling Documentation](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Python Exceptions Documentation](https://docs.python.org/3/library/exceptions.html)

## License

This repository is open for educational purposes.
