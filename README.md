# M122 Automation Project

## Overview

This project is part of Module 122: *Automating Processes with a Scripting Language*.

The goal of this project is to automate the organization of downloaded school files. The application scans a configured folder, extracts module identifiers from filenames (for example `M122`), categorizes files automatically, and moves them into the correct module folders.

The automation reduces repetitive manual work, improves organization, minimizes mistakes, and demonstrates software engineering concepts such as modular architecture, UML design, logging, error handling, configuration systems, graphical interfaces, and testing.

---

# Features

* Automatic file detection
* Filename parsing and module extraction
* Dynamic module-folder mapping
* Configurable subfolder naming
* Automatic folder creation
* Duplicate file handling (`_V2`, `_V3`, ...)
* Structured logging system
* Error handling and validation
* Environment variable configuration
* Modular Python architecture
* Configurable project setup
* Graphical User Interface (GUI)
* File selection before execution
* Select All / Deselect All controls
* Scrollable file list
* Live file statistics
* Progress bar with live status updates
* Discord webhook reporting
* Weekly automated execution
* Windows Task Scheduler integration
* Custom executable (.exe) support

---

# Technologies

* Python 3
* Tkinter GUI
* Filesystem operations
* Python logging module
* Environment variables
* JSON configuration
* Discord Webhooks
* Windows Task Scheduler
* Git & GitHub
* python-dotenv
* discord-webhook
* PyInstaller

---

# Project Structure

```txt
project-root/
│
├── assets/
│   └── icon.ico
│
├── docs/
│   ├── requirements/
│   ├── design/
│   │   ├── diagrams/
│   │   └── architecture/
│   │
│   └── testing/
│
├── src/
│   ├── main.py
│   ├── gui.py
│   ├── detector.py
│   ├── parser.py
│   ├── logger.py
│   ├── config.py
│   ├── mover.py
│   ├── discord_reporter.py
│   ├── scheduler_runner.py
│   └── test_discord.py
│
├── config/
│   └── module_mapping.json
│
├── tests/
├── logs/
│
├── input/          (development/testing only)
├── output/         (development/testing only)
│
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
```

---

# Configuration

The application uses environment variables and JSON configuration.

## .env

Example:

```env
DOWNLOADS_PATH=./input
LOG_PATH=./logs
DEFAULT_UNKNOWN_PATH=./output/unknown
MAPPING_FILE=./config/module_mapping.json
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/...
```

---

## module_mapping.json

Example:

```json
{
    "modules": {
        "M122":"./output/M122",
        "M123":"./output/M123",
        "M114":"./output/M114"
    },

    "subfolders": {
        "exercise":"Exercises",
        "theory":"Theory",
        "code":"Code"
    }
}
```

---

# Installation

## Clone repository

```bash
git clone <repository-url>
```

## Navigate into project

```bash
cd file-automation-script
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Create environment file

Copy:

```txt
.env.example
```

to:

```txt
.env
```

Adjust the paths if necessary.

---

# Usage

## Python Version

Run the application:

```bash
python src/main.py
```

---

## GUI Version

Run:

```bash
python src/gui.py
```

The GUI provides:

* File scanning
* File selection via checkboxes
* Select All / Deselect All controls
* Live file statistics
* Scrollable file list
* Progress bar
* Status updates
* Error messages
* Sorting summary

---

## EXE Version

Build executable:

```bash
pyinstaller --onefile --windowed --icon=assets/icon.ico --name="M122 File Organizer" src/gui.py
```

Executable output:

```txt
dist/
└── M122 File Organizer.exe
```

---

# Discord Reporting

The application can send automation summaries to a Discord channel using webhooks.

Features:

* Weekly reports
* File processing summaries
* Success and error notifications
* Automated execution feedback

Configuration is performed using the `DISCORD_WEBHOOK_URL` environment variable.

---

# Scheduled Automation

The project supports fully automated execution using Windows Task Scheduler.

Example configuration:

* Frequency: Weekly
* Day: Sunday
* Time: 12:00

The scheduler automatically:

1. Scans the configured folder
2. Sorts files
3. Creates a summary report
4. Sends the report to Discord

---

# Workflow

1. Scan configured input directory
2. Detect files
3. Extract module identifier
4. Resolve module destination
5. Categorize files automatically
6. Create folders if needed
7. Handle duplicate filenames
8. Move files
9. Write logs
10. Display results

---

# Example Output Structure

```txt
M122/
├── Exercises/
│   └── LB01.docx
│
├── Theory/
│   └── Notes.pdf
│
├── Code/
│   └── project.py
│
└── random.zip
```

---

# Documentation

Project documentation includes:

* Requirements analysis
* UML activity diagram
* UML component diagram
* Design documentation
* Parsing documentation
* Error handling strategy
* Logging architecture
* Configuration system
* Test protocol

---

# Testing

Test cases and testing documentation:

```txt
tests/
docs/testing/
```

---

# Author

Nikola

GIBZ Informatik
Module 122 – Automating Processes with a Scripting Language
