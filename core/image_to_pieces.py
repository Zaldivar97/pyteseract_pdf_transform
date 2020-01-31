from pdf2image import convert_from_path
from PIL import Image
from io import BytesIO
import json


def text_to_json(text_images, verbose = False):
    columns = []
    for i, text_image in enumerate(text_images):
        text = text_image.splitlines()
        text = list(filter(str.strip, text))
        text = list(filter((']').__ne__, text))
        text = list(filter(('[').__ne__, text))    
        match_counter = 1
        rows = []
        temp_row = {}
        for j in range(0,len(text),2):
            if i > 0 and i != len(text_images)-1:
                if j < len(text) / 2 - 1:
                    rows.append({f'match-{match_counter}':f'{text[j*2]} vs {text[j*2+2]}'})
                temp_dict = {'winner':text[j],'results':text[j+1]}
                columns[i-1][f'round-{i}'][match_counter-1].update(temp_dict)
            if i == len(text_images)-1:
                if j == 0:
                    temp_row = {f'match-1':f'{text[j]} vs {text[j+4]}'}
                if j < 3:
                    temp_dict = {'winner':text[j*2],'results':text[j*2+1]}    
                    columns[i-1][f'round-{i}'][match_counter-1].update(temp_dict)
                if j > 3:
                    temp_dict = {'winner':text[j-2],'results':text[j-1]}   
                    temp_row.update(temp_dict)
                    rows.append(temp_row)
            elif i == 0:
                rows.append({f'match-{match_counter}':f'{text[j]} vs {text[j+1]}'})
            match_counter = match_counter + 1
        columns.append({f'round-{i+1}': rows} )
    output = json.dumps(columns, indent=4)
    if verbose:
        print(output)
    return output



def pdf_to_image(pdf_path):
    """
    Convierte el pdf a imagen para posterior trasformacion

    Parameters:
        pdf_path (str): el path relativo o absoluto del pdf

    Returns:
        Imagen representativa del pdf
    """
    try:
        pdf = convert_from_path(pdf_path, fmt='jpeg', dpi=200)
        tempfile = BytesIO()
        pdf[0].save(tempfile,'JPEG')
    except Exception:
        print("Error convirtiendo el pdf a imagen")
    return Image.open(tempfile, mode='r')

def crop_image(width, image):
    """
    Divide la imagen representativa del pdf en varias partes

    Arguments:
        width (int): ancho de la imagen (pdf)

    Returns:
        lista con las distintas imagenes en que fue dividido el pdf    
    """
    left, TOP, right, BOTTOM = 260, 300, width/3, 1850
    images = []
    divisor = 2
    for i in range(5):
        img = image.crop((left,TOP,right,BOTTOM))
        images.append(img)
        left = right
        if i == 1:
            image = image.crop((width/2, 0, width-200, BOTTOM))
            width, local_size = image.size
            left = 0
            divisor = 3
            right = (i * width / divisor) + 30
        elif i>1:
            right = i * width / divisor
        else:
            right = right + right / divisor

    return images