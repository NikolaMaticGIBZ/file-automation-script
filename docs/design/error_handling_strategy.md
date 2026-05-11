# Error Handling Strategy

## Overview

The application must handle invalid files, missing folders, permission problems, and unexpected runtime errors safely.

The goal of the error handling strategy is to ensure the script continues running whenever possible while logging all important issues for debugging and maintenance.

---

# Error Handling Objectives

The application should:

- Prevent application crashes
- Log all important errors
- Continue processing other files if one file fails
- Provide understandable error messages
- Improve maintainability and debugging

---

# Planned Error Cases

## Invalid Filename Structure

### Description

A file does not contain a recognizable module identifier.

### Example

```txt
Homework.pdf
```

### Handling Strategy

- Skip the file
- Log warning message
- Continue processing remaining files

### Logged Information

- Filename
- Timestamp
- Reason for failure

---

## Unknown Module Identifier

### Description

The filename contains a module that is not configured.

### Example

```txt
M999_Project.pdf
```

### Handling Strategy

- Move file to fallback folder (optional)
- Or skip file
- Log warning message

### Logged Information

- Filename
- Unknown module name
- Timestamp

---

## Missing Target Folder

### Description

The configured destination folder does not exist.

### Handling Strategy

- Automatically create folder if possible
- Otherwise log error
- Continue processing

### Logged Information

- Missing folder path
- Creation result
- Timestamp

---

## Duplicate Filenames

### Description

A file with the same name already exists in the destination folder.

### Example

```txt
M122_Project.pdf
```

already exists.

### Handling Strategy

- Create renamed version
- Example:

```txt
M122_Project_V2.pdf
```

- Prevent overwriting existing files

### Logged Information

- Original filename
- New filename
- Timestamp

---

## Permission Errors

### Description

The script has insufficient permissions to access or move files.

### Handling Strategy

- Catch exception
- Log error message
- Continue processing remaining files

### Logged Information

- File path
- Exception message
- Timestamp

---

## Unexpected Runtime Errors

### Description

Unexpected exceptions during execution.

### Handling Strategy

- Catch exceptions using try-except
- Write detailed error logs
- Prevent complete application crash

### Logged Information

- Exception type
- Error message
- Stack trace (optional)
- Timestamp

---

# Logging Strategy

The logging system records:

- Information messages
- Warnings
- Errors
- File operations
- Duplicate handling
- Parsing failures

## Log File Location

```txt
logs/
```

## Example Log Entry

```txt
2026-05-12 14:32:11 | WARNING | Unknown module detected: M999
```

---

# Python Error Handling Techniques

The project uses:

- try-except blocks
- validation checks
- conditional logic
- logging module

## Example

```python
try:
    move_file(source, destination)
except PermissionError as error:
    logger.error(f"Permission denied: {error}")
```

---

# Benefits of the Error Handling Strategy

- Improved reliability
- Better debugging
- Easier maintenance
- Reduced risk of data loss
- Safer automation workflow