#!/bin/env/python
import os

from core import get_input_filenames
from core import IMAGE_EXTENSIONS, INPUT_DIRECTORY, OUTPUT_DIRECTORY
from core import convert_to_pdf

def main():
    image_filenames = get_input_filenames(INPUT_DIRECTORY, IMAGE_EXTENSIONS)
    output_filenames = [f.rsplit('.', 1)[0] + '.pdf' for f in image_filenames]
    zipped = zip(image_filenames, output_filenames)
    for input, output in zipped:
        output = os.path.join(OUTPUT_DIRECTORY, os.path.basename(output))
        convert_to_pdf(input, output)

if __name__ == "__main__":
    main()
