from PyPDF2 import PdfFileWriter, PdfFileReader
import os

from core import get_input_filenames
from core import PDF_EXTENSIONS, INPUT_DIRECTORY, OUTPUT_DIRECTORY
from core import convert_to_pdf


def main():
    filenames = get_input_filenames(INPUT_DIRECTORY, PDF_EXTENSIONS)

    for f in filenames:
        inputpdf = PdfFileReader(open(f, "rb"))

        for i in range(inputpdf.numPages):
            output = PdfFileWriter()
            output.addPage(inputpdf.getPage(i))
            with open(os.path.join(OUTPUT_DIRECTORY, "{}-{}.pdf".format(os.path.basename(f), i)), "wb") as outputStream:
                output.write(outputStream)

if __name__ == "__main__":
    main()
