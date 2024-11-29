from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 初始化 WebDriver
chrome_driver_path = r'C:\Users\User\Desktop\BuyTickets\tools\chromedriver.exe'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# 設置瀏覽器全螢幕
driver.maximize_window()

try:
    # 開啟目標網址
    url = "https://tixcraft.com/activity/game/25_maroon5"
    driver.get(url)

    # 點擊 "全部拒絕" 按鈕（如果存在）
    try:
        print("嘗試點擊 '全部拒絕' 按鈕...")
        reject_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "onetrust-reject-all-handler"))
        )
        reject_button.click()
        print("'全部拒絕' 按鈕已點擊")
    except Exception as e:
        print(f"未找到 '全部拒絕' 按鈕或無法點擊: {e}")

    # 等待頁面加載並滾動視窗
    def scroll(num):
        js = f"var q=document.documentElement.scrollTop = {num}"
        driver.execute_script(js)
        time.sleep(1)

    scroll(500)

    # 點擊 "立即訂購" 按鈕
    print("嘗試點擊立即訂購按鈕...")
    try:
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button.btn.btn-primary.text-bold.m-0")
            )
        )
        button.click()
        print("立即訂購按鈕已點擊")
    except Exception as e:
        print(f"無法點擊立即訂購按鈕: {e}")

    # 選擇位子
    print("選擇位子...")
    scroll(1500)
    try:
        seat = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.ID, "17641_33")
            )
        )
        seat.click()
        print("成功選擇位子 id='17641_33'")
    except Exception as e:
        print(f"無法選擇位子: {e}")

    # 選擇票數
    print("選擇票數...")
    try:
        # 等待下拉選單元素出現
        elem_select_num = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#TicketForm_ticketPrice_02")
            )
        )

        # 使用 Select 選擇票數
        from selenium.webdriver.support.ui import Select
        select = Select(elem_select_num)  # 初始化 Select 對象
        select.select_by_value("1")       # 選擇 value="1"
        print("已成功選擇 1 張票")
    except Exception as e:
        print(f"選擇票數時發生錯誤: {e}")

    # 勾選 "我同意"
    print("勾選 '我同意'")
    try:
        accept = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#TicketForm_agree"))
        )
        accept.click()
    except Exception as e:
        print(f"勾選同意時發生錯誤: {e}")

    # 處理驗證碼（此處需進行圖片識別）
    print("處理驗證碼...")
    try:
        captcha_path = "captcha/screenshot.png"
        driver.save_screenshot(captcha_path)

        from PIL import Image
        import pytesseract
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        # 假設驗證碼在特定位置
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#yw0"))
        )
        location = element.location
        size = element.size
        image = Image.open(captcha_path)
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']
        captcha = image.crop((left, top, right, bottom))
        captcha.save("captcha/cropped_captcha.png")

        # 使用 Tesseract 識別驗證碼
        captcha_text = pytesseract.image_to_string(
            "captcha/cropped_captcha.png", lang="eng")
        print(f"識別的驗證碼為: {captcha_text.strip()}")

        # 輸入驗證碼
        input_captcha = driver.find_element(
            By.CSS_SELECTOR, "#TicketForm_verifyCode")
        input_captcha.send_keys(captcha_text.strip())
    except Exception as e:
        print(f"處理驗證碼時發生錯誤: {e}")

    # 確認張數
    print("按張數按紐...")
    try:
        confirm = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button.btn.btn-primary.btn-green")
            )
        )
        confirm.click()
        print("訂單已確認！")
    except Exception as e:
        print(f"確認張數時發生錯誤: {e}")

except Exception as e:
    print(f"發生錯誤: {e}")

finally:
    time.sleep(10000)
    # 關閉瀏覽器
    driver.quit()
    print("瀏覽器已關閉")
