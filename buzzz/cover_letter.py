from fpdf import FPDF
import cowsay
import lorem
import json
import numpy as np

class CoverLetter(FPDF):
    def __init__(self):
        super().__init__()
        self.set_font("courier", size=11)
        self.add_page()
        self.left_margin = 10
        self.cover_letter = "buzzz/data/cover_letter_antimetal.txt"

        self.cell(txt="**Nathaniel Joselson**", markdown=True,ln=1)
        self.cell(txt="1(917)332-7756", markdown=True,ln=1)
        self.cell(txt="New York, NY", markdown=True,ln=1)
        self.ln()
        self.add_cover_letter()
        self.add_flower()

    def save(self, name: str):
        print(f"Saving PDF to {name}")
        self.output(name)

    def add_cover_letter(self):
        cover_letter = open(self.cover_letter).read()
        self.set_x(self.left_margin)
        self.multi_cell(w=175, txt=cover_letter, ln=1)

    def add_flower(self):
        self.set_x(self.left_margin)
        self.set_font("courier", size=9)
        flower = open("buzzz/data/flower.txt").read()
        self.multi_cell(w=190, txt=flower)


if __name__ == "__main__":
    pdf = FPDF()
    pdf.set_font("courier")
    pdf.add_page()
    pdf.multi_cell(w=150, txt="hello\nhello")
    pdf.ln()
    pdf.set_text_color(255, 255, 255)
    pdf.multi_cell(w=150, txt="invisible")
    pdf.output("fpdftest.pdf")
