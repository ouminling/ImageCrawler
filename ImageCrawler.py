import base64
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from concurrent.futures import ThreadPoolExecutor
import urllib3
import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 用户输入网址
input_url = input("请输入网址: ")
print(f"用户输入的网址: {input_url}")
urls = [input_url]

base_folder = r"D:\\Download"

def create_driver():
    print("正在创建 WebDriver 实例...")
    edge_options = Options()
    edge_options.add_argument("--headless")
    edge_options.add_argument("--ignore-certificate-errors")
    edge_options.add_argument("--disable-gpu")
    edge_options.add_argument("--no-sandbox")
    edge_options.add_argument("--disable-dev-shm-usage")
    driver_path = r"C:\\Users\\oml\\AppData\\Local\\edgedriver_win64\\msedgedriver.exe"
    service = Service(driver_path)
    return webdriver.Edge(service=service, options=edge_options)

def download_images_from_url(url, index):
    print(f"\n正在处理第 {index} 个网页: {url}")
    driver = create_driver()
    driver.get(url)
    print("等待网页加载...")
    time.sleep(5)
    # 滚动页面以确保所有图片都被加载
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.TAG_NAME, "img")))
    html = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html, 'lxml')

    # 获取 <div class="title"> 内的 <a> 标签的 title 内容作为文件夹名
    title_tag = soup.select_one('div.title a[title]')
    folder_name = title_tag['title'] if title_tag else f"webpage_{index}"
    print(f"文件夹名: {folder_name}")

    # 仅查找 <div class="title"> 内的 <a> 标签
    title_links = soup.select('div.title a[href]')
    print(f"共找到 {len(title_links)} 个匹配的链接")
    
    # 替换 URL 中的 "index" 为 "slide"
    new_urls = [urljoin(url, link['href'].replace('index', 'slide')) for link in title_links if 'index' in link['href']]
    print(f"转换后的链接数量: {len(new_urls)}")

    for new_url in new_urls:
        print(f"处理新的 URL: {new_url}")
        download_images(new_url, folder_name)  # 修改参数顺序

def download_images(url, folder_name):  # 修改参数名称
    print(f"开始下载图片: {url}")
    driver = create_driver()
    driver.get(url)
    print("等待图片加载...")
    time.sleep(5)
    # 滚动页面以确保所有图片都被加载
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    html = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html, 'lxml')
    img_tags = soup.find_all('img')
    print(f"找到 {len(img_tags)} 张图片")
    save_folder = os.path.join(base_folder, folder_name)  # 使用 folder_name
    os.makedirs(save_folder, exist_ok=True)
    
    for img_index, img in enumerate(img_tags):
        img_url = urljoin(url, img.get('src'))
        print(f"正在下载图片 {img_index + 1}: {img_url}")
        try:
            response = requests.get(img_url, stream=True, timeout=30, verify=False)
            response.raise_for_status()
            file_ext = os.path.splitext(urlparse(img_url).path)[1] or '.jpg'
            file_name = os.path.join(save_folder, f'image_{img_index}{file_ext}')
            with open(file_name, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"成功下载: {file_name}")
        except Exception as e:
            print(f"下载失败: {e}")

if __name__ == "__main__":
    print("开始多线程图片下载...")
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(download_images_from_url, url, idx) for idx, url in enumerate(urls, start=1)]
        for future in futures:
            future.result()
    print("所有下载任务已完成。")