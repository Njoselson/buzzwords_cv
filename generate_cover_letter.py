from buzzwordscv.cover_letter import CoverLetter
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--file_name", default="cover_letter.pdf")
args = parser.parse_args()

COVER_LETTER_NAME = args.file_name


cover_letter = CoverLetter()
cover_letter.save(COVER_LETTER_NAME)
