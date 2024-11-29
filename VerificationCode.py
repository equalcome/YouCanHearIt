from PIL import Image
import pytesseract

# 設置 Tesseract 的路徑
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 指定圖片的完整路徑
image_path = r'C:\Users\User\Desktop\BuyTickets\vcPic\hioo.png'

# 打開圖片
image = Image.open(image_path)

# 使用 Tesseract 識別圖片中的文字
text = pytesseract.image_to_string(image, lang='eng')

# 輸出識別結果
print("Verification code is")
print(text)
