import os
from pathlib import Path

import pytest
from pypdf import PdfReader

from buzzz.cv import CV

CV_NAME = "cv.pdf"


@pytest.fixture(scope="function")
def setup():
    cv_path = Path(CV_NAME)
    if cv_path.exists():
        os.remove(cv_path)


def test_01_script_produces_pdf(setup):
    # If we don't have any pdf
    cv_path = Path(CV_NAME)
    assert not cv_path.exists()
    # when make a CV class and save it
    cv = CV()
    cv.save(CV_NAME)
    # then there is a "cv.pdf" that is written in the base folder.
    assert cv_path.exists()


def test_02_CV_has_contact_information(setup):
    # If we make a CV
    cv = CV()
    # when we save it
    cv.save(CV_NAME)
    # then the pdf when read will have this information
    reader = PdfReader(CV_NAME)
    page = reader.pages[0]
    text = page.extract_text()
    assert "Nathaniel Joselson" in text
    assert "I am" in text
