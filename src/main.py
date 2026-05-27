"""
Main application workflow.

Coordinates:
- File detection
- Parsing
- File movement
- Logging
- Error handling
"""


from detector import scan_folder
from parser import extract_module
from mover import move_file

from config import DOWNLOADS_PATH
from logger import logger

def process_file(file):

    try:

        module = extract_module(
            file.name
        )


        moved_file = move_file(
            file,
            module
        )


        print(
            f"{file.name} -> {moved_file}"
        )


        logger.info(
            f"Moved file: {file.name}"
        )


    except PermissionError as error:

        logger.error(
            f"Permission denied: {error}"
        )


    except Exception as error:

        logger.error(
            f"File processing failed: {error}"
        )


def process_all_files():

    files = scan_folder(
        DOWNLOADS_PATH
    )


    print(
        "\nProcessing files:\n"
    )


    for file in files:

        process_file(
            file
        )


def main():

    logger.info(
        "Application started"
    )


    try:

        process_all_files()


    except Exception as error:

        logger.critical(
            f"Application failed: {error}"
        )


if __name__ == "__main__":

    main()