# Configuration System

## Overview

The application uses a centralized configuration system to manage paths, folder mappings, and environment-specific settings.

The configuration system improves maintainability, flexibility, and scalability while avoiding hardcoded values inside the source code.

---

# Configuration Objectives

The configuration system should:

- Centralize important settings
- Avoid hardcoded paths
- Support different environments
- Improve maintainability
- Simplify future extensions

---

# Environment Variables

The application uses environment variables to store system-dependent paths and sensitive configuration values.

## Benefits

- Easier configuration changes
- Improved portability
- Better maintainability
- Reduced hardcoded values

---

# Planned Environment Variables

## DOWNLOADS_PATH

Defines the Downloads directory to monitor.

### Example

```env
DOWNLOADS_PATH=C:/Users/Nikola/Downloads
```

---

## LOG_PATH

Defines the folder for log files.

### Example

```env
LOG_PATH=logs/
```

---

## DEFAULT_UNKNOWN_PATH

Defines the fallback directory for unknown modules.

### Example

```env
DEFAULT_UNKNOWN_PATH=output/unknown/
```

---

# Module Folder Mapping

The application maps module identifiers to destination folders.

## Example Mapping

```json
{
  "M122": "C:/School/M122/",
  "M123": "C:/School/M123/",
  "M114": "C:/School/M114/"
}
```

---

# Configuration Files

## .env

Stores environment variables.

### Example

```env
DOWNLOADS_PATH=C:/Users/Nikola/Downloads
LOG_PATH=logs/
DEFAULT_UNKNOWN_PATH=output/unknown/
```

---

## module_mapping.json (planned)

Stores module-to-folder assignments.

### Example

```json
{
  "M122": "C:/School/M122/",
  "M123": "C:/School/M123/"
}
```

---

# Configuration Workflow

## Step 1 — Application Start

The application loads all configuration values.

### Actions

- Read environment variables
- Load mapping configuration
- Validate required paths

---

## Step 2 — Runtime Usage

The application uses configuration values during execution.

### Examples

- Determine Downloads folder
- Resolve module destination path
- Define logging location

---

## Step 3 — Error Handling

Invalid or missing configuration values are logged.

### Examples

- Missing environment variable
- Invalid folder path
- Missing mapping configuration

---

# Python Libraries

The project may use:

- os
- pathlib
- dotenv (optional)
- json

---

# Example Python Usage

```python
import os
from dotenv import load_dotenv

load_dotenv()

downloads_path = os.getenv("DOWNLOADS_PATH")
```

---

# Security and Maintainability Benefits

- Cleaner code
- Easier updates
- Better portability
- Reduced risk of configuration errors
- Environment-specific customization