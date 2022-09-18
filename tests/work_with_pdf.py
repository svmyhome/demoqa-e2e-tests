from PyPDF2 import PdfReader
import pytest

def test_pdf():
    pdf_docs = PdfReader('../resouces/ISTQB_CTFL_PT_Syllabus_2018_GA.pdf')
    numbers_of_pages = len(pdf_docs.pages)
    print(numbers_of_pages)
    get_text = pdf_docs.pages[1].extract_text()
    print(get_text)
    assert 'Version 2018 Page 2 of 59 9 December 2018 ' in get_text