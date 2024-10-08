from fpdf import FPDF
import cowsay
import json
import numpy as np

BUZZWORDS = [
    "AI",
    "Machine learning",
    "Metaverse",
    "VR",
    "LLM",
    "NLP",
    "Metaverse",
    "data2vec",
    "representation learning",
]


class CV(FPDF):
    def __init__(self):
        super().__init__()
        self.set_font("courier", size=9)
        self.add_page()
        self.left_margin = 10
        self.cow_start = 7 
        self.buzzwords = BUZZWORDS

        self.add_contact_information(
            title="Senior Machine Learning Engineer",
            location="New York, NY, USA",
            email="nathaniel.joselson@gmail.com",
            linkedin="\nlinkedin.com/in/nathaniel-joselson-301687132/",
            phone_num="1(917)332-7756",
            github="https://github.com/Njoselson",
            blog="https://njoselson.github.io/",
            lanugages="English, Swedish"
        )

        self.add_name()
        self.add_about_me()
        # self.add_flower()
        self.add_experiences()

    def save(self, name: str):
        print(f"Saving PDF to {name}")
        self.output(name)

    def generate_buzzword_line(self):
        line = ""
        while len(line) <= 150:
            line += np.random.choice(self.buzzwords)
            line += "  "
        return line

    def buzz_ln(self):
        buzzword_line = self.generate_buzzword_line()
        self.set_text_color(255, 255, 255)
        self.cell(w=150, txt=buzzword_line, ln=1)
        self.set_text_color(0, 0, 0)

    def add_name(self):
        self.set_xy(self.left_margin, 13)
        self.multi_cell(w=150, txt="**Nathaniel Joselson**", markdown=True)

    def add_contact_information(self, **kwargs):
        self.set_xy(80, self.cow_start)
        self.multi_cell(
            w=150,
            txt=self.reformat_cowsay(
                cowsay.get_output_string(
                    "cow",
                    "".join([f"{item[0]}: {item[1]} \n" for item in kwargs.items()]),
                )
            ),
        )

    def reformat_cowsay(self, cowsay_text: str):
        move_amt = 16
        lines = [line for line in cowsay_text.split("\n")]
        moved_lines = [" " * move_amt + line for line in lines[:-7]]
        final_text = "\n".join(moved_lines + lines[-7:])
        return final_text

    def add_about_me(self):
        about_me = open("buzzwordscv/data/about_me.txt").read().replace("\n", " ")
        self.set_x(self.left_margin)
        self.multi_cell(w=97, txt=about_me)

    def add_flower(self):
        self.set_xy(self.left_margin+40,53)
        flower = open("buzzwordscv/data/flower.txt").read()
        self.multi_cell(w=190, txt=flower)

    def format_experience(self, experience):
        self.set_x(self.left_margin)
        self.cell(w=90, txt=f'**{experience["name"]}**', markdown=True)
        self.cell(w=100, txt=experience["dates"], align="R", ln=1)
        self.set_x(self.left_margin)
        self.multi_cell(
            w=180, txt=f'__{experience["description"]}__', ln=1, markdown=True
        )
        for skill in experience["skills"]:
            self.write(txt="~ ")
            self.set_x(self.left_margin + 3)
            self.multi_cell(w=180, txt=skill, ln=1, markdown=True)

    def add_experiences(self):
        experiences = json.load(open("buzzwordscv/data/experience.json"))

        self.set_xy(self.left_margin, self.cow_start+ 58)
        self.multi_cell(w=150, txt="**Work Experience**", markdown=True)
        for experience in experiences["work_experiences"]:
            self.buzz_ln()
            self.format_experience(experience)

        self.buzz_ln()
        self.set_x(self.left_margin)
        self.multi_cell(w=150, txt="**Academics**", markdown=True)
        for experience in experiences["academics"]:
            self.buzz_ln()
            self.format_experience(experience)

        self.buzz_ln()
        self.set_x(self.left_margin)
        self.multi_cell(w=150, txt="**Skills**", markdown=True)
        for experience in experiences["skills"]:
            self.buzz_ln()
            self.format_experience(experience)


if __name__ == "__main__":
    pdf = FPDF()
    pdf.set_font("courier")
    pdf.add_page()
    pdf.multi_cell(w=150, txt="hello\nhello")
    pdf.ln()
    pdf.set_text_color(255, 255, 255)
    pdf.multi_cell(w=150, txt="invisible")
    pdf.output("fpdftest.pdf")
