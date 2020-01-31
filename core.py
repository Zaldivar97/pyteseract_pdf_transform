from util.image_to_pieces import pdf_to_image, crop_image, text_to_json
import pytesseract
from pytesseract import Output
import sys



def pdf_to_data(lang, pdf_path):
    config = "-l "+lang+" --oem 1 --psm 3"
    img = pdf_to_image(pdf_path)
    width, height = img.size
    images = crop_image(width, img)
    text_images = [pytesseract.image_to_string(image, config=config) for image in images]
    text_to_json(text_images)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("""Uso: core.py [siglas_de_idioma] [pdf_path]
        Ejemplo de uso: core.py eng /home/user/test.pdf""")
        sys.exit(1)
    lang, pdf_path = sys.argv[1:]
    pdf_to_data(lang,pdf_path)