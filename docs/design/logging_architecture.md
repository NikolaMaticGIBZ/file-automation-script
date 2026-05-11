# Logging Architecture

## Overview

The application uses a structured logging system to track file operations, warnings, errors, and important runtime events.

Logging improves debugging, traceability, and maintainability of the automation process.

---

# Logging Objectives

The logging system should:

- Record important operations
- Help identify runtime problems
- Support debugging and testing
- Provide execution traceability
- Improve maintainability

---

# Logging Levels

The application uses multiple logging levels.

## INFO

Used for normal application events.

### Examples

- File detected
- File moved successfully
- Folder created
- Application started

### Example Entry

```txt
2026-05-12 14:22:11 | INFO | File moved successfully: M122_Project.pdf
```

---

## WARNING

Used for non-critical problems.

### Examples

- Unknown module identifier
- Invalid filename format
- Duplicate filename detected

### Example Entry

```txt
2026-05-12 14:24:03 | WARNING | Unknown module identifier: M999
```

---

## ERROR

Used for critical problems that prevent an operation.

### Examples

- Permission denied
- File move failed
- Missing configuration
- Unexpected exceptions

### Example Entry

```txt
2026-05-12 14:25:41 | ERROR | Permission denied while moving file
```

---

# Log File Location

All logs are stored inside:

```txt
logs/
```

Example:

```txt
logs/application.log
```

---

# Logged Information

The system logs:

- Timestamp
- Log level
- Filename
- Module identifier
- Target path
- Error messages
- Duplicate handling
- Runtime events

---

# Logging Workflow

## Application Start

The logger initializes when the application starts.

### Actions

- Create log file if missing
- Configure log format
- Set logging level

---

## Runtime Logging

During execution, the logger records all important operations.

### Examples

- File detection
- Parsing results
- File movement
- Errors and warnings

---

## Application End

The logger records application completion.

### Example

```txt
2026-05-12 14:31:55 | INFO | File processing completed
```

---

# Python Logging Module

The project uses Python’s built-in logging module.

## Benefits

- Standardized logging
- Multiple log levels
- Easy file output
- Maintainable implementation

---

# Example Implementation

```python
import logging

logging.basicConfig(
    filename="logs/application.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logging.info("Application started")
```

---

# Benefits of the Logging Architecture

- Easier debugging
- Better traceability
- Improved maintainability
- Faster problem analysis
- Better testing support