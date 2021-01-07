#!/bin/env/python
from PyPDF2 import PdfFileMerger
import os

def main():
    pdf_filenames = []
    for directory, directories, files in os.walk('input'):
        for filename in files:
            file_path = os.path.join(directory, filename)
            if file_path.endswith('.pdf'):
                pdf_filenames.append(file_path)

    merger = PdfFileMerger()

    for pdf_file in pdf_filenames:
        merger.append(pdf_file)

    merger.write(os.path.join('output', 'output.pdf'))
    merger.close()

if __name__ == "__main__":
    main()
