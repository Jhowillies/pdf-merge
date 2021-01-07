# pdf-merge
A tool to merge multiple PDFs into a single document.

The way this tool functions is simple. Put any amount of PDF files in any
directory structure in the `input` folder.

Run `python pdf-merge.py` and the files will be merged into a single PDF.
The resulting PDF will be called output.pdf and placed in the `output` folder.

The order in which the files are merged is the order in which they would appear
in `os.walk`. Basically name your files so that they exist on the filesystem
in the order in which you want them merged.

Quick and dirty. pdf-merge at your service.
