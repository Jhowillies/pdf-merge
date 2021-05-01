#!/bin/env/python
import os

from core import get_input_filenames
from core import PDF_EXTENSIONS, INPUT_DIRECTORY, OUTPUT_DIRECTORY
from core import merge_pdfs

def main():
    pdf_filenames = get_input_filenames(INPUT_DIRECTORY, PDF_EXTENSIONS)
    output_filename = os.path.join(OUTPUT_DIRECTORY, 'output.pdf')
    merge_pdfs(pdf_filenames, output_filename)

if __name__ == "__main__":
    main()
