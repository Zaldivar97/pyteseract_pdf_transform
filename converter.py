from core.image_to_pieces import pdf_to_image, crop_image, text_to_json
import pytesseract
import sys


def pdf_to_data(lang, verbose, pdf_path):
    """
    Convierte el pdf indicado a estructura json legible y utilizable

    Parameters:
        lang (str): string de 3 caracteres indicador del lenguaje del training set de tesseract
        verbose (bool): parametro para indicar si se imprime en pantalla el json
        pdf_path (str): path relativo o absoluto del documento a procesar
    """
    config = "-l "+lang+" --oem 1 --psm 3"
    img = pdf_to_image(pdf_path)
    width, height = img.size
    images = crop_image(width, img)
    text_images = [pytesseract.image_to_string(image, config=config) for image in images]
    json = text_to_json(text_images, verbose=verbose)
    #with open("data.json", mode='w') as f:
    #    f.write(json)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        output = """Uso: converter.py [siglas_de_idioma] [verbose] [pdf_path]
                    verbose = 1/0
                    Ejemplo de uso: converter.py eng 1 /home/user/test.pdf"""
        print(output)
        sys.exit(1)
    lang, verbose, pdf_path = sys.argv[1:]
    pdf_to_data(lang, verbose, pdf_path)