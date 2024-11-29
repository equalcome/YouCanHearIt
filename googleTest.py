from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

# 指定 ChromeDriver 的路徑
service = Service(
    'C:\\Users\\User\\Desktop\\BuyTickets\\tools\\chromedriver.exe')  # 修改為您的實際路徑
driver = webdriver.Chrome(service=service)

try:
    # 1. 打開 Google 網站
    driver.get("https://www.google.com")
    print("成功打開 Google 網站")

    # 2. 找到搜尋框並輸入「Selenium」
    search_box = driver.find_element(By.NAME, "q")  # 使用元素名稱來定位搜尋框
    search_box.send_keys("Selenium")  # 輸入關鍵字
    search_box.send_keys(Keys.RETURN)  # 模擬按下 Enter 鍵
    print("已輸入搜尋內容")

    # 3. 等待頁面加載
    time.sleep(2)  # 暫停 2 秒讓搜尋結果加載

    # 4. 取得搜尋結果的標題
    results = driver.find_elements(By.XPATH, "//h3")  # 定位搜尋結果的標題
    print("搜尋結果：")
    for i, result in enumerate(results[:5], start=1):  # 只打印前 5 個結果
        print(f"{i}. {result.text}")

finally:
    # 5. 關閉瀏覽器
    driver.quit()
    print("已關閉瀏覽器")
