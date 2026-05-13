# Parsing Logic

## Overview

The application extracts module identifiers from filenames to determine the correct destination folder for each downloaded file.

The parsing system validates filenames, detects supported module patterns, and returns structured information for further processing.

---

# Parsing Objectives

The parsing logic should:

- Detect module identifiers automatically
- Support multiple filename formats
- Validate filename structure
- Ignore unsupported files
- Improve automation reliability

---

# Parsing Workflow

## Step 1 — Receive Filename

The parser receives a filename from the detector module.

### Example

```txt
M122_Project.pdf
```

---

## Step 2 — Analyze Filename Structure

The parser checks whether the filename contains a supported module identifier.

### Supported Pattern

```txt
M<number>
```

### Examples

```txt
M122
M123
M114
```

---

## Step 3 — Extract Module Identifier

The parser extracts the module name from the filename.

### Example

Filename:

```txt
M122_Project.pdf
```

Extracted value:

```txt
M122
```

---

## Step 4 — Validate Module Identifier

The parser validates the extracted value.

### Validation Rules

- Must start with "M"
- Must contain numeric values
- Must match supported naming pattern

### Valid Examples

```txt
M122_Project.pdf
M123_Notes.docx
M114_Test.png
```

### Invalid Examples

```txt
Homework.pdf
notes.txt
module122.pdf
```

---

## Step 5 — Return Structured Result

The parser returns the extracted module information.

### Example Result

```python
{
    "module": "M122",
    "filename": "M122_Project.pdf",
    "valid": True
}
```

---

# Supported Naming Patterns

## Current Patterns

### Module Format

```txt
M122
M123
M114
```

### Full Filename Examples

```txt
M122_Project.pdf
M123_Assignment.docx
M114_Test.jpg
```

---

# Planned Future Extensions

The parser architecture supports future extensions.

## Possible Future Patterns

### Class Names

```txt
INFA1a
```

### Extended Formats

```txt
M122_LB02_Project.pdf
```

### Automatic Renaming

```txt
M122_Project_Nikola.pdf
```

---

# Invalid Filename Handling

Invalid filenames are skipped safely.

## Actions

- Log warning message
- Ignore unsupported file
- Continue processing remaining files

## Example Warning

```txt
WARNING | Invalid filename format: homework.pdf
```

---

# Parsing Techniques

The parser may use:

- String splitting
- Regular expressions (Regex)
- Validation checks

---

# Example Parsing Logic

## String Split Example

```python
filename = "M122_Project.pdf"
module = filename.split("_")[0]
```

---

## Regex Example

```python
import re

match = re.search(r"M\d+", filename)
```

---

# Benefits of the Parsing Logic

- Reliable automation
- Flexible architecture
- Easier maintenance
- Scalable naming support
- Reduced manual sorting