#! /usr/bin/env python3

import time
import pdf2image
import pytesseract

try:
    from PIL import Image
except ImportError:
    import Image

def pdf_to_img(pdf_file):
    return pdf2image.convert_from_path(pdf_file)

def ocr_core(file):
    text = pytesseract.image_to_string(file, lang="eng+fra")
    return text

from timeit import default_timer as timer

for i in range(3,4):
    print(i)
    start = timer()
    outfile = open("{}.txt".format(i),"a") 
    
    images = pdf_to_img("{}.pdf".format(i))
    texts = []
    
    for pg, img in enumerate(images):
        texts.append(ocr_core(img))
        
    outfile.write('\n'.join(texts))
    outfile.close()
    
    end = timer()
    print((end - start)/60)
