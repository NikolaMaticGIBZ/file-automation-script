# Folder Architecture

## Overview

The project uses a modular folder structure to separate responsibilities and improve maintainability.

---

## Root Directory

Contains global project configuration and documentation files.

### Files

- README.md  
  General project overview and usage instructions.

- requirements.txt  
  Python dependencies required for the project.

- .gitignore  
  Defines files and folders ignored by Git.

---

## src/

Contains the main Python source code.

### Purpose

The source folder separates application logic from documentation and generated data.

### Modules

- main.py  
  Entry point of the application.

- detector.py  
  Detects and validates files from the input directory.

- parser.py  
  Extracts module information from filenames.

- logger.py  
  Handles logging functionality.

- config.py  
  Stores environment configuration and constants.

---

## docs/

Contains all project documentation required for Module 122.

### Subfolders

- requirements/  
  Functional and non-functional requirements.

- design/  
  UML diagrams and architecture documentation.

- testing/  
  Test protocols and test evidence.

---

## tests/

Contains test scripts and future automated tests.

---

## input/

Contains files that will be processed by the script.

---

## output/

Contains generated output files after processing.

---

## logs/

Contains runtime log files and error logs.

---

## Architecture Benefits

- Separation of concerns
- Better maintainability
- Easier debugging
- Scalable structure
- Cleaner documentation organization