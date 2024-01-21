import pytesseract
from PIL import Image

image = Image.open("03.png")
image = image.convert("L")
threshold = 125
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table, "1")
# image.show()
result = pytesseract.image_to_string(image)
print(result)
