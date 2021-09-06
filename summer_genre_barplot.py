import pandas as pd
import numpy as np
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams["font.family"] = "Malgun Gothic"
matplotlib.rcParams["axes.unicode_minus"] = False


df = pd.DataFrame()
df = pd.read_excel("C:\\Users\\USER\\Desktop\\DS\\project1\\data\\preprocessing_data.xlsx")
# print(df.head())

genre = df["장르"]
# print(genre.head(10))
genre_list = df["장르"].unique()
print(genre_list)
# print(type(genre_list))

df_list = df.groupby("장르")["월"].agg(**{"count":"count"}).reset_index()
df_list.sort_values(by=["count"],axis=0)
print(df_list)
# print(type(df_list))  # 데이터프레임

# 막대 그래프
df_bar = df_list.plot.bar(x="장르")
df_bar.set_xlabel("장르")
df_bar.set_ylabel("곡 수")
df_bar.set_title("여름에 인기있는 장르 그래프")
plt.savefig("C:\\Users\\USER\\Desktop\\DS\\project1\\data\\summer_bar.png",dpi=200)
plt.show()

# 파이 그래프
df_list.groupby(['장르']).sum().plot(kind='pie', y='count',figsize=(8,8),startangle=90,
                          counterclock=False,shadow=True,autopct="%1.1f%%")
plt.savefig("C:\\Users\\USER\\Desktop\\DS\\project1\\data\\summer_pie.png",dpi=200)
plt.show()
