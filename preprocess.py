import numpy as np
import pandas as pd
import json
import fitz #(pymupdf)
import re
import docx
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#Run this once then delete
nltk.download('punkt') #for tokenization
nltk.download('stopwords') #a list of stopwards like "the" "is" "in" and a buncha other irrelevant words

#Lets organize everything into a Class for preprocessing portion


class TextPrepocessor:

    def __init__(self):
        pass
    def extract_text_pdf(self, pdf_path):
        pass
    def extract_text_docx(self, docx_path):
        pass
    def extract_text_txt(self, txt_path):
        pass
    def extract_text(self, file_path):
        pass
    def clean_text(self, text):
        pass
    def remove_stopwords(self, text):
        pass
    def remove_punctuation(self, text):
        pass
    def preprocess(self, text):
        pass
    def process_doc(self, file_path):
        pass

# Right here we should make a function for extracting skills from the text?

if __name__ == "__main__":
    preprocessor = TextPrepocessor()

    pdf_path = "replace with path to resume"
    result = preprocessor.process_document(pdf_path)

    #maybe here we put the text results here with some print statements

    #maybe here we put extracted skills results (AKA the skills that were found)


pdf_path = ""

doc = fitz.open(pdf_path)

for page_num, page in enumerate(doc, start=1):
    text = page.get_text()
    print(text)
    
doc.close()
