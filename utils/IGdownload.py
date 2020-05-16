from bs4 import BeautifulSoup
import requests as req
import re
from selenium import webdriver
import sys
import os

sys.path.append('./geckodriver.exe')


class IGDownloader:

    @staticmethod
    def __validate_link(link):
        match = re.search(r"^https://www\.instagram.com/p/.+", link)
        if not match:
            raise Exception('Invalid link')

    def __get_download_src(self, link):
        self.__validate_link(link)
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        driver = webdriver.Firefox(
            executable_path='./geckodriver.exe', firefox_options=options)
        try:
            driver.get(link)
            html = driver.page_source
            driver.quit()
            soup = BeautifulSoup(html, 'html.parser')
            img_el = soup.find('img', attrs={'class': 'FFVAD'})
            return img_el['src']
        except Exception as e:
            print(e)

    @staticmethod
    def __ensure_folder_exists():
        if not os.path.exists("../images/"):
            os.mkdir("../images/")

    def download_img(self, link):
        self.__ensure_folder_exists()
        img_name = re.search(r"\/p/(.+[\w||\d])", link).group(1)
        src = self.__get_download_src(link)
        img_path = f"/images/{img_name}.jpg"
        response = req.get(src)
        if response.status_code == 200:
            with open("." + img_path, "wb") as f:
                f.write(response.content)
                return [img_name, img_path]


if __name__ == "__main__":
    Downloader = IGDownloader()
