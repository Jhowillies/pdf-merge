import os

from PIL import Image
from PyPDF2 import PdfFileMerger

INPUT_DIRECTORY = 'input'
OUTPUT_DIRECTORY = 'output'

PDF_EXTENSIONS = ['.pdf']
IMAGE_EXTENSIONS = ['.bmp', '.jpg', '.jpeg', '.webm', '.tiff', '.png', '.gif', '.ico']

def get_input_filenames(input_dir, extensions):
    filenames = []
    for directory, directories, files in os.walk(input_dir):
        for filename in files:
            file_path = os.path.join(directory, filename)
            for extension in extensions:
                if file_path.lower().endswith(extension):
                    filenames.append(file_path)
                    break
    return filenames

def merge_pdfs(pdf_filenames, output_filename):
    merger = PdfFileMerger()

    for pdf_file in pdf_filenames:
        merger.append(pdf_file)

    merger.write(output_filename)
    merger.close()

def convert_to_pdf(inputfile, outputfile):
    if not outputfile.endswith('.pdf'):
        raise ValueError("Outputfile must end in .pdf")
    image1 = Image.open(inputfile)
    im1 = image1.convert('RGB')
    im1.save(outputfile)
