from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
filename = "Screenshot_13.jpg"
img1 = Image.open(filename)
text = pytesseract.image_to_string(img1)
print("Hasil: ",text)
