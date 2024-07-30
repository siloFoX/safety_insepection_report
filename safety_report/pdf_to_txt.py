from tqdm import tqdm
from PIL import Image
import pytesseract
import fitz
import env
import os
import io

def extract_txt_from_pdf (src_pdf = env.PDF_SRC, src_txt = env.TXT_SRC) :
    pdf_paths = os.listdir(src_pdf)
    is_file_exist = False
    for filename in pdf_paths :
        if filename.endswith(".pdf") :
            pdf_abs_path = os.path.join(src_pdf, filename)
            txt_abs_path = os.path.join(src_txt, filename.replace(".pdf", ".txt"))
            is_file_exist = True

            pdf = fitz.open(pdf_abs_path)
            text = ""
            for page_idx in tqdm(range(pdf.page_count), desc = "Extracting text from " + filename) :
                page = pdf.load_page(page_idx)
                pix = page.get_pixmap()

                img_data = pix.tobytes("png")
                img = Image.open(io.BytesIO(img_data))

                ocr_text = pytesseract.image_to_string(img, lang = "kor")
                text += ocr_text

            with open(txt_abs_path, 'w', encoding = "utf-8") as txt_file :
                txt_file.write(text)
            
            pdf.close()
            
    return is_file_exist
        


if __name__ == "__main__" :
    print(extract_txt_from_pdf())