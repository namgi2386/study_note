from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

chrome_driver_path = ''  # 여기에 크롬 드라이버 경로를 입력하세요.
service = Service(chrome_driver_path)
driver = webdriver.Chrome()

# 구글 이미지 검색 페이지로 이동
driver.get(f"https://www.google.co.kr/imghp?hl=ko&ogbl")


my_keyword = "cat"
scroll_cnt = 10
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.send_keys(my_keyword + Keys.ENTER)

elem = driver.find_element(By.TAG_NAME, 'body')
for i in range(10):
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.1)

images = driver.find_element(By.CSS_SELECTOR, "rg_i.Q4LuWd")
links = [image.get_attribute('src') for image in images.get_attribute('src') is not None]

for k,i in enumerate(links):
    url = i
    urllib.request.urlretrieve(url , str(k)+'.jpg' )
print('완료')