from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import os
import base64

# ChromeDriver 경로 설정
CHROME_DRIVER_PATH = ''  # ChromeDriver 경로로 변경하세요.
DOWNLOAD_FOLDER = 'cat_images'  # 다운로드 폴더
SEARCH_QUERY = 'cat'

# 다운로드 폴더 생성
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

# Selenium 설정
chrome_options = Options()
chrome_options.add_argument("--headless")  # 헤드리스 모드 (브라우저 창을 띄우지 않음)
service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=chrome_options)

# 이미지 검색 페이지 열기
driver.get(f'https://www.google.com/search?hl=en&tbm=isch&q={SEARCH_QUERY}')

# 스크롤 다운하여 이미지 로드
for _ in range(5):  # 스크롤을 5번 내림
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.implicitly_wait(2)

# 이미지 요소 가져오기
soup = BeautifulSoup(driver.page_source, 'html.parser')
img_elements = soup.find_all('img')

# 이미지 다운로드
for i, img in enumerate(img_elements):
    if i >= 20:  # 20장 다운로드
        break
    # 이미지 URL 찾기
    img_url = img.get('src') or img.get('data-src') or img.get('srcset')
    
    if img_url:
        if img_url.startswith('data:image'):
            # data URL인 경우
            try:
                # data URL에서 base64 데이터 추출
                header, encoded = img_url.split(',', 1)
                img_data = base64.b64decode(encoded)
                with open(os.path.join(DOWNLOAD_FOLDER, f'cat_image_{i+1}.jpg'), 'wb') as handler:
                    handler.write(img_data)
                print(f'Downloaded {i+1} image from data URL.')
            except Exception as e:
                print(f'Could not download image {i+1} from data URL: {e}')
        else:
            # 일반 URL인 경우
            try:
                img_data = requests.get(img_url).content
                with open(os.path.join(DOWNLOAD_FOLDER, f'cat_image_{i+1}.jpg'), 'wb') as handler:
                    handler.write(img_data)
                print(f'Downloaded {i+1} image: {img_url}')
            except Exception as e:
                print(f'Could not download image {i+1}: {e}')
    else:
        print(f'Image {i+1} does not have a valid URL.')

# 브라우저 종료
driver.quit()
