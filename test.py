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

try:
    # 開啟目標網址
    url = "https://tixcraft.com/activity/game/25_maroon5"
    driver.get(url)

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

except Exception as e:
    print(f"發生錯誤: {e}")

finally:
    # 關閉瀏覽器
    time.sleep(10)
    driver.quit()
    print("瀏覽器已關閉")
