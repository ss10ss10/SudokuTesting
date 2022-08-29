from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

option = webdriver.ChromeOptions()
option.add_argument("--headless")
driver = webdriver.Chrome(
    executable_path="/home/sulaiman/Documents/GitHub/SudokuTesting/chromedriver", chrome_options = option
)
driver.get("http://localhost:3000/")

total_buttons = driver.find_elements(By.CLASS_NAME, "button")
print(len(total_buttons))
