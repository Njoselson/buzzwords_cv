from buzzwordscv.cv import CV
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--file_name", default="cv.pdf")
args = parser.parse_args()

CV_NAME = args.file_name

cv = CV()
cv.save(CV_NAME)
