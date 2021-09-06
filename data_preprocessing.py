import pandas as pd
import numpy as np
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

# 5년치 데이터 하나로 합치기
excel_names = ["C:\\Users\\USER\\Desktop\\DS\\project1\\data\\2017_month.xlsx",
               "C:\\Users\\USER\\Desktop\\DS\\project1\\data\\2018_month.xlsx",
               "C:\\Users\\USER\\Desktop\\DS\\project1\\data\\2019_month.xlsx",
               "C:\\Users\\USER\\Desktop\\DS\\project1\\data\\2020_month.xlsx",
               "C:\\Users\\USER\\Desktop\\DS\\project1\\data\\2021_month.xlsx"]
appended_data = pd.DataFrame()
for name in excel_names:
    pd_data = pd.read_excel(name)
    appended_data = appended_data.append(pd_data)

# appended_data.to_excel("C:\\Users\\USER\\Desktop\\DS\\project1\\data\\merge_month.xlsx", index=False)


# "appended_data" : 원본 객체
# "summer_data" : 전체에서 6,7,8월 데이터만 가져옴
# "merge_genre" : <장르>열만 전처리


# 6,7,8월 데이터만 가져오기 (summer_data)
summer_data = appended_data[(appended_data["월"]==6) | (appended_data["월"]==7) |
                                         (appended_data["월"]==8)]

# summer_data.to_excel("C:\\Users\\USER\\Desktop\\DS\\project1\\data\\summer_data.xlsx", index=False)
summer_data = pd.DataFrame(summer_data,columns=["년도","월","순위","타이틀","가수","장르","해당년도"])


# "장르"열에서 "OST" 전처리
summer_data["장르"] = summer_data["장르"].replace(["OST / 드라마", "OST / 전체"], "OST")
# print(summer_data.head())

# "장르"열에서 "가요" 전처리
summer_data["장르"] = summer_data["장르"].replace(["가요 / R&B/소울","가요 / 댄스","가요 / 인디","가요 / 발라드",
                                               "가요 / 랩/힙합","가요 / 락","가요 / 블루스/포크","가요 / 일렉트로니카",
                                               "POP / 락","POP / 일렉트로니카"," 인디"," 댄스"," 랩/힙합"," 발라드",
                                               " 드라마"," 팝"," 일렉트로니카"," R&B/소울"," 락","OST / 해외영화",
                                               "가요 / 트로트","POP / R&B/소울","가요 / 전체"," 전체","POP / 팝","팝",
                                               "드라마","재즈 / 정통"],
                                       ["R&B/소울","댄스","인디","발라드","랩/힙합","락","블루스/포크","일렉트로니카",
                                        "POP","POP","인디","댄스","랩/힙합","발라드","OST","POP","일렉트로니카","R&B/소울",
                                        "락","OST","트로트","POP","전체","전체","POP","POP","OST","재즈"])

# "해당년도" 열 삭제
prepro_data = summer_data.drop("해당년도",axis=1)
# print(prepro_data.head(10))
prepro_data.to_excel("C:\\Users\\USER\\Desktop\\DS\\project1\\data\\preprocessing_data.xlsx", index=False)