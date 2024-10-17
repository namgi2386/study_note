import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import base64

# 크롬 드라이버 경로 설정
chrome_driver_path = ''  # 여기에 크롬 드라이버 경로를 입력하세요.
service = Service(chrome_driver_path)

# 크롬 브라우저 실행
driver = webdriver.Chrome(service=service)

# 구글 이미지 검색 페이지로 이동
search_query = 'cat'
driver.get(f"https://www.google.com/search?q={search_query}&tbm=isch")

# 페이지 로딩 대기
time.sleep(3)

# 스크롤 다운을 통해 더 많은 이미지 로드
num_scrolls = 5  # 스크롤을 5번 내리기 (필요에 따라 조정)
body_elem = driver.find_element("tag name", "body")

for _ in range(num_scrolls):
    body_elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

# 페이지 소스 가져오기
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# 이미지 태그 추출
images = soup.find_all('img', class_='YQ4gaf')

# 저장할 폴더 생성
if not os.path.exists('images'):
    os.makedirs('images')

# 다운로드할 이미지 개수
download_limit = 10  # 원하는 이미지 개수로 설정

# 이미지 다운로드
downloaded = 0
for idx, img in enumerate(images):
    if downloaded >= download_limit:
        break

    img_url = img.get('src')
    if img_url:
        # Base64 데이터 URL 처리
        if img_url.startswith('data:'):
            # Base64 데이터 파싱
            header, base64_data = img_url.split(',', 1)
            img_data = base64.b64decode(base64_data)
            with open(f'images/{search_query}_{downloaded}.jpg', 'wb') as handler:
                handler.write(img_data)
            print(f"Downloaded image {downloaded + 1} (Base64)")
        else:
            # HTTP/HTTPS URL 처리
            try:
                img_data = requests.get(img_url).content
                with open(f'images/{search_query}_{downloaded}.jpg', 'wb') as handler:
                    handler.write(img_data)
                print(f"Downloaded image {downloaded + 1} (HTTP)")
            except Exception as e:
                print(f"Could not download image {idx}: {e}")
        
        downloaded += 1

# 브라우저 종료
driver.quit()
