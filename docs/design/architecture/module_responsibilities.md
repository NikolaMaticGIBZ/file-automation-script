# Module Responsibilities

## Overview

The project is divided into multiple Python modules to separate responsibilities and improve maintainability.

The application automates the organization of downloaded school files by detecting module identifiers in filenames and moving files into the correct module folders automatically.

---

# main.py

## Responsibility

Acts as the main entry point of the application and coordinates the complete workflow.

## Tasks

- Start the application
- Initialize configuration and logging
- Execute file detection
- Call parsing and moving logic
- Handle overall workflow control

## Dependencies

- detector.py
- parser.py
- logger.py
- config.py

---

# detector.py

## Responsibility

Detects files inside the Downloads folder.

## Tasks

- Scan configured Downloads directory
- Detect newly downloaded files
- Ignore unsupported or invalid files
- Return list of detected files

## Possible Extensions

- Real-time folder monitoring
- Recursive scanning
- File type filtering

---

# parser.py

## Responsibility

Extracts module information from filenames.

## Tasks

- Read filenames
- Detect module identifiers
- Validate naming patterns
- Return structured module information

## Example

Filename:

```txt
M122_Project.pdf
```

Extracted module:

```txt
M122
```

## Supported Naming Patterns

- M122
- M123
- INFA1a (future extension)

---

# logger.py

## Responsibility

Handles application logging and error tracking.

## Tasks

- Write information logs
- Write warning messages
- Write error logs
- Save logs into log files

## Logged Information

- Detected files
- Moved files
- Duplicate file handling
- Parsing errors
- Permission errors

## Benefits

- Easier debugging
- Better traceability
- Improved maintainability

---

# config.py

## Responsibility

Stores configuration values and environment variables.

## Tasks

- Store Downloads folder path
- Store module-folder mappings
- Load environment variables
- Define constants and paths

## Configuration Examples

- Downloads directory
- Output module folders
- Logging locations

## Benefits

- Avoid hardcoded values
- Easier configuration changes
- Better scalability

---

# Planned Future Modules

## mover.py (optional)

Could handle dedicated file movement logic separately from detection and parsing.

## watcher.py (optional)

Could monitor the Downloads folder continuously in real time.

---

# Design Principles

The module architecture follows these principles:

- Single Responsibility Principle
- Modular design
- Low coupling
- Easier testing
- Better maintainability
- Scalable architecture