# M122 Automation Project

## Overview
This project is part of Module 122: *Automating Processes with a Scripting Language*.

The goal of the project is to automate a multi-step file processing workflow using Python.  
The script scans files from a defined directory, extracts information from filenames, processes the data, and generates structured output automatically.

The automation reduces repetitive manual work, improves consistency, and demonstrates software engineering concepts such as modular architecture, UML design, logging, error handling, and testing.

---

# Features

- Automatic file detection
- Filename parsing and module extraction
- Structured logging system
- Error handling and validation
- Organized input/output processing
- Modular Python architecture
- Configurable environment setup

---

# Technologies

- Python 3
- Filesystem operations
- Python logging module
- Environment variables
- Git & GitHub

---

# Project Structure

```txt
project-root/
│
├── docs/
│   ├── requirements/
│   ├── design/
│   │   ├── diagrams/
│   │   ├── architecture/
│   ├── testing/ 
│   └── grading/
│
├── src/
│   ├── main.py
│   ├── detector.py
│   ├── parser.py
│   ├── logger.py
│   └── config.py
│
├── tests/
├── input/
├── output/
├── logs/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
```

## Navigate into Project

```bash
cd m122-automation-project
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Usage

Run the script using:

```bash
python src/main.py
```

The script will:
1. Detect files inside the input directory
2. Parse relevant filename information
3. Process the files
4. Generate output
5. Write logs and errors

---

# Documentation

The complete project documentation is located in the `docs/` folder and includes:

- Requirements analysis
- UML activity diagram
- UML component diagram
- Design documentation
- Test protocol

---

# Testing

Test cases and testing documentation are located in:

```txt
tests/
docs/testing/
```

---

# Author

Nikola  
Module 122 – GIBZ Informatik
