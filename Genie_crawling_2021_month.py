from selenium import webdriver
from bs4 import BeautifulSoup

import requests

driver = webdriver.Chrome("C:\myexam\chromedriver\chromedriver.exe")

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

song_data = []
for month in range(1, 9):
    rank = 1
    for page in range(1, 3):
        url = f"https://www.genie.co.kr/chart/top200?ditc=M&ymd=2021{month:02d}01&hh=15&rtm=N&pg={page}"
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        songs = soup.select('table > tbody > tr')
        i = 0
        for song in songs:
            title = song.select('a.title')[0].text.strip()
            singer = song.select('a.artist')[0].text

            select = driver.find_elements_by_css_selector('a.btn-info')[i].click()
            # time.sleep(1)

            genre = driver.find_elements_by_css_selector('span.value')[2].text
            # time.sleep(1)
            driver.back()

            i += 1

            song_data.append(['2021', month, rank, title, singer, genre])
            rank += 1

import pandas as pd

columns = ['년도', '월', '순위', '타이틀', '가수', '장르']
pd_data = pd.DataFrame(song_data, columns=columns)

pd_data.to_excel('C:\\myexam\\2021_month.xlsx', index=False)