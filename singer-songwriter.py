import pandas as pd
import numpy as np
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams["font.family"] = "Malgun Gothic"
matplotlib.rcParams["axes.unicode_minus"] = False


driver = webdriver.Chrome("C:\myexam\chromedriver\chromedriver.exe")

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

song_data = []
for month in range(1, 13):
    rank = 1
    for page in range(1, 3):
        url = f"https://www.genie.co.kr/chart/top200?ditc=M&ymd=2017{month:02d}01&hh=15&rtm=N&pg={page}"
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        songs = soup.select('table > tbody > tr')
        i = 0
        for song in songs:
            title = song.select('a.title')[0].text.strip()
            singer = song.select('a.artist')[0].text

            # 더보기 버튼 누르기
            select = driver.find_elements_by_css_selector('a.btn-info')[i].click()

            # 장르 데이터 크롤링
            genre = driver.find_elements_by_css_selector('span.value')[2].text

            # 작사가, 작곡가 데이터 크롤링
            try:
                lyricist = driver.find_elements_by_css_selector('span.value')[4].text
            except:
                lyricist = "-"

            try:
                songwriter = driver.find_elements_by_css_selector('span.value')[5].text
            except:
                songwriter = "-"

            driver.back()

            i += 1

            song_data.append(['2017', month, rank, title, singer, genre, lyricist, songwriter])
            rank += 1

import pandas as pd

columns = ['년도', '월', '순위', '타이틀', '가수', '장르', "작사가", "작곡가"]
pd_data = pd.DataFrame(song_data, columns=columns)

print(pd_data.head(10))

pd_data.to_excel("C:\\Users\\USER\\Desktop\\DS\\project1\\2017_month_+2.xlsx", index=False)








