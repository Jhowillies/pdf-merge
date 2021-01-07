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

## Installation
You need `python3` and `git` to run this using these directions.

We recommend using a virtual environment for literally all of your python
projects. After you have python3 the following steps will install `pdf-merge`.

1. Clone the repository
2. Create a virtual environment
3. Install dependencies.
4. Copy your pdfs into the input folder
5. Run the program
6. Have merged PDFs

These steps will clone the repository and create a virtual environment.
```
git clone https://github.com/Jhowillies/pdf-merge.git
cd pdf-merge
python3 -m venv venv
```

This steps will activate the virtual environment, but are different on
Linux and Windows.

On Linux:
```
. venv/bin/activate
```

On Windows:
```
venv\Scripts\activate
```

Next install the dependencies:
```
pip install -r requirements.txt
```

This is when you copy your PDF files into the input folder.

After copying files run this:
```
python pdf-merge.py
```

The output should now be in the `output` folder and titled `results.pdf`
