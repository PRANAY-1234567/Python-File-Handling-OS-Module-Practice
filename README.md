# Python File Handling & OS Module Practice

A beginner-friendly Python practice project covering **file handling**, **directory management**, and the **OS module**. This project demonstrates how Python can be used to work with files and folders, read and write data, navigate directories, and manage file pointers.

## 📌 Project Overview

This project was created to practice Python's built-in `os` module and file-handling operations.

The program demonstrates how to:

* Get and change the current working directory
* Create and remove folders
* Create nested directory structures
* List files and folders
* Rename files and directories
* Open files
* Read file contents
* Write and append data to files
* Check file properties
* Use file pointers with `tell()` and `seek()`
* Work with different file-opening modes

## 🛠️ Technologies Used

* **Python 3**
* **OS Module**
* **File Handling**
* **VS Code**

## 📂 Topics Covered

### 1. OS Module

The project demonstrates commonly used `os` functions:

```python
import os

os.getcwd()
os.chdir()
os.mkdir()
os.makedirs()
os.listdir()
os.rename()
os.rmdir()
os.remove()
os.popen()
```

These functions can be used to interact with the operating system and manage files and directories.

### 2. File Opening Modes

The project covers different file modes:

| Mode | Purpose                                        |
| ---- | ---------------------------------------------- |
| `r`  | Read an existing file                          |
| `w`  | Write to a file and overwrite existing content |
| `a`  | Append data to the end of a file               |
| `r+` | Read and write                                 |
| `w+` | Write and read                                 |
| `a+` | Append and read                                |

### 3. Reading Files

Examples include:

```python
file.read()
file.readline()
file.readlines()
file.read(4)
```

These methods are used to read complete files, individual lines, multiple lines, or a specific number of characters.

### 4. Writing to Files

The project demonstrates:

```python
file.write()
file.writelines()
```

Example:

```python
file.writelines(["Python\n", "Java\n", "SQL\n", "PowerBI"])
```

### 5. File Pointer Management

The project also demonstrates:

```python
file.tell()
file.seek()
```

`tell()` returns the current position of the file pointer, while `seek()` moves the pointer to a specific position.

Example:

```python
print(file.tell())
file.seek(0)
print(file.read())
```

### 6. File Properties

The project includes examples of checking file information:

```python
file.name
file.mode
file.readable()
file.writable()
file.closed
```

These properties and methods help understand the current state and permissions of an opened file.

## 📁 Example Files

The practice code works with example files such as:

```text
marker.txt
PEN.txt
Walmart.txt
```

It also demonstrates creating directories such as:

```text
FirstClass
SecondClass
Pranay
A/
└── B/
    └── C/
        └── D/
            └── E/
```

## 🔑 Important Concept: Raw Strings

When working with Windows paths, backslashes can sometimes create escape-sequence issues.

Instead of:

```python
os.chdir("C:\Users\ASUS\Desktop\Evening class")
```

a raw string can be used:

```python
os.chdir(r"C:\Users\ASUS\Desktop\Evening class")
```

Another option is to use double backslashes:

```python
os.chdir("C:\\Users\\ASUS\\Desktop\\Evening class")
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Open the project

Open the project folder in **VS Code** or another Python IDE.

### 3. Run the Python file

```bash
python filename.py
```

Make sure Python 3 is installed on your system.

## 🎯 Learning Outcomes

After completing this practice project, I gained hands-on understanding of:

* Python file handling
* Directory and file management
* Working with Windows file paths
* File reading and writing
* File append operations
* File modes
* File pointers
* `seek()` and `tell()`
* Basic OS-level operations using Python

## 🚀 Future Improvements

Possible improvements to this project include:

* Using `with open()` for safer file handling
* Adding exception handling with `try-except`
* Creating a menu-driven file management application
* Adding file and folder existence checks
* Building a small command-line file manager
* Adding logging for file operations

## 👨‍💻 Author

**Pranay Jadhao**

B.E. in Electronics & Telecommunication Engineering

**Skills:** Python | SQL | Excel | Power BI | Manual Testing | Selenium

---

⭐ This repository is part of my Python learning and practice journey.

