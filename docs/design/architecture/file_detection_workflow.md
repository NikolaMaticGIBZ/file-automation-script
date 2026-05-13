# File Detection Workflow

## Overview

The application automatically scans the Downloads folder, detects relevant files, extracts module identifiers from filenames, and moves the files into the correct module folders.

The workflow is designed to reduce manual file organization and improve consistency.

---

# Workflow Steps

## Step 1 — Start Application

The user starts the Python script manually or through a scheduled task.

### Actions

- Load configuration
- Initialize logging system
- Validate required folders

---

## Step 2 — Scan Downloads Folder

The script scans the configured Downloads directory for files.

### Actions

- Read folder contents
- Ignore unsupported entries
- Create list of detected files

### Example Directory

```txt
Downloads/
├── M122_Project.pdf
├── M123_Notes.docx
└── randomfile.txt
```

---

## Step 3 — Validate Filename Structure

Each filename is checked for valid module identifiers.

### Valid Examples

```txt
M122_Project.pdf
M123_Test.docx
```

### Invalid Examples

```txt
homework.pdf
notes.txt
```

### Actions

- Detect valid module pattern
- Skip invalid files
- Log warnings for invalid names

---

## Step 4 — Extract Module Identifier

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

## Step 5 — Resolve Target Folder

The application maps the detected module to a configured destination folder.

### Example Mapping

```txt
M122 → C:/School/M122/
M123 → C:/School/M123/
```

### Actions

- Load folder mapping
- Validate target folder
- Create folder if missing

---

## Step 6 — Handle Duplicate Files

Before moving the file, the application checks whether the filename already exists.

### Example

Existing file:

```txt
M122_Project.pdf
```

New file:

```txt
M122_Project.pdf
```

Generated duplicate-safe filename:

```txt
M122_Project_V2.pdf
```

---

## Step 7 — Move File

The application moves the file into the correct module directory.

### Actions

- Execute file move
- Confirm successful operation
- Log movement result

---

## Step 8 — Log Operations

All important operations are written into log files.

### Logged Events

- File detected
- Module extracted
- File moved
- Invalid filenames
- Duplicate handling
- Errors and warnings

---

## Step 9 — Finish Workflow

After all files are processed, the script ends safely.

### Final Actions

- Close logging operations
- Return execution summary (optional)

---

# Workflow Benefits

- Reduces repetitive manual work
- Improves organization
- Prevents misplaced files
- Provides traceable automation
- Supports scalable module management