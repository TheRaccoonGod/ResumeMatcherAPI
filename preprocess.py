import numpy as np
import pandas as pd
import string
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
        
        self.stop_words = set(stopwords.words('english'))
        self.keep_terms = {'c', 'r', 'with'}
        self.stop_words = self.stop_words - self.keep_terms

    def extract_text_pdf(self, pdf_path):
        
        text = ""

        try:
            doc = fitz.open(pdf_path)

            for page_num, page in enumerate(doc,start=1):
                text += page.get_text()
            doc.close()
            
            return text
        
        except Exception as e:
            print("There was an error extracting text from PDF: {e}")
            return ""

    def extract_text_docx(self, docx_path):
        
        try:
            doc = docx.Document(docx_path)
            text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
            return text
        
        except Exception as e:
            print(f"There was an error extracting text from Docx: {e}")
            return ""

    def extract_text_txt(self, txt_path):
        
        try:
            with open(txt_path, 'r', encoding='utf-8') as file:
                text = file.read()
            return text
        
        except Exception as e:
            print(f"There was an error extracting text from TXT: {e}")
            return ""

    def extract_text(self, file_path):
        file_extension = file_path.split('.')[-1].lower()

        if file_extension == 'pdf':
            return self.extract_text_pdf(file_path)
        elif file_extension == 'docx':
            return self.extract_text_docx(file_path)
        elif file_extension == 'txt':
            return self.extract_text_txt(file_path)
        else:
            print(f"File is NOT Supported. Choose another Option")
            return ""

    def clean_text(self, text):
        
        text = text.lower() #All lowercase

        text = re.sub(r'\s+',' ', text).strip() # Remove whitespace

        # Do you know how to remove URLs?

        text = re.sub(r'\S+@\S+','', text) # Remove email addresses

        # Do you know how to remove phone numbers?

        return text

    def remove_stopwords(self, text):
        
        tokens = word_tokenize(text)
        filtered_tokens = [word for word in tokens if word.lower() not in self.stop_words]
        return ' '.join(filtered_tokens)

    def remove_punctuation(self, text):
        
        translator = str.maketrans('','',string.punctuation)
        return text.translate(translator)

    def preprocess(self, text):
        
        text = self.clean_text(text)
        text = self.remove_punctuation(text)
        text = self.remove_stopwords(text)
        return text

    def process_doc(self, file_path):
        raw_text = self.extract_text(file_path)
        processed_text = self.preprocess(raw_text)

        return {
            "raw text": raw_text,
            "processed_text": processed_text
        }

# Right here we should make a function for extracting skills from the text?
def extract_skills(text, skills_db=None):

    if skills_db is None:
        skills_db = [
            #Languages
            "python", "java", "javascript", "c++", "c#", "typescript", "scala", "r", "bash", "powershell",

            # Data Science/ML
            "machine learning", "deep learning", "natural language processing", "nlp", "data analysis", "data science", "data mining", "data visualization", "big data", "predictive modeling",
            "statistical analysis", "regression", "classification", "clustering", "scikit-learn", "tensorflow", "pytorch", "pandas", "numpy", "matplotlib", "neural networks", "tableau", "power bi", "keras",

            # Web Development
            "html", "css", "react", "angular", "node.js", "django", "flask", "rest api", "backend", "frontend", "full stack",

            #Databases
            "sql", "mysql", "postgresql", "nosql", "mangodb", "oracle", "sql server", "sqlite", "database management", "data modeling",

            #Cloud
            "aws", "azure", "gcp", "cloud computing", "docker", "kubernetes", "git", "github",

            #Soft skills
            "communication", "leadership", "teamwork", "problem solving", "critical thinking", "project management", "time management"
        ]

    skills_db = [skill.lower() for skill in skills_db]
    text_lower = text.lower()

    # Find skills
    found_skills = []
    for skill in skills_db:
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text_lower):
            found_skills.append(skill)
    
    return found_skills

if __name__ == "__main__":
    preprocessor = TextPrepocessor()

    pdf_path = "replace with path to resume"
    result = preprocessor.process_document(pdf_path)

    #maybe here we put the text results here with some print statements

    #maybe here we put extracted skills results (AKA the skills that were found)
    skills = extract_skills(result["raw_text"])
    print(f"Found Skills: {skills}")
