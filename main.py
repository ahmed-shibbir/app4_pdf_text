import pandas as pd
from fpdf import FPDF
import glob
from pathlib import Path


filepaths = glob.glob("files/*.txt")

pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    title = Path(filepath).stem.title()
    print(title)
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.cell(h=10, w=50, txt=title, ln=1)

    with open(filepath, 'r') as file:
        # Read the entire file content into a string
        file_contents = file.read()
        # pdf.add_page()
        pdf.set_font(family="Times", style="I", size=12)
        pdf.multi_cell(h=6, w=0, txt=file_contents)

pdf.output("output")