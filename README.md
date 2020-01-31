# pyteseract_pdf_transform
Script para convertir el texto del pdf a json. Manteniendo el orden de las rondas y partidos 

## Herramientas
El script utiliza el modulo pytesseract que es un wrapper para el paquete binario **tesseract**.
Tesseract es un motor de reconocimiento óptico de caracteres para varios sistemas operativos.
Cabe destacar que antes de utilizar se debe tener instalado este paquete.

## Instalación binario
```bash
sudo apt install tesseract-ocr
```
Ademas se deben descargar los training sets dependiendo del idioma, por ejemplo, si se desea el 
training set para el idioma ingles:

```bash
sudo apt install tesseract-ocr-eng
```
Se debe indicar el path de estos training sets mediante la variable de entorno TESSDATA_PREFIX, en mi caso, los datasets estan en /usr/share/tesseract-ocr/4.00/tessdata/
```bash
export TESSDATA_PREFIX=/usr/share/tesseract-ocr/4.00/tessdata/
```
## Instalación modulo python
En mi caso, utilizando conda
```bash
conda install --name myenv -c conda-forge pytesseract
```
## Uso pytesseract
```python
import pytesseract
text_from_image = pytesseract.image_to_string(some_image)
```
## Uso converter
converter.py [siglas_de_idioma] [verbose(1/0)] [pdf_path]
```bash
python converter.py eng 1 ./docs/mds.pdf
```
