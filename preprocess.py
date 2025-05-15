import numpy as np
import pandas as pd
import json
import fitz #(pymupdf)

pdf_path = ""

doc = fitz.open(pdf_path)

for page_num, page in enumerate(doc, start=1):
    text = page.get_text()
    print(text)
    
doc.close()