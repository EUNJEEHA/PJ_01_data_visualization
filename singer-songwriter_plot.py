import pandas as pd
import numpy as np
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams["font.family"] = "Malgun Gothic"
matplotlib.rcParams["axes.unicode_minus"] = False

# 엑셀 파일 불러오기(2017~2021)
df17 = pd.DataFrame()
df18 = pd.DataFrame()
df19 = pd.DataFrame()
df20 = pd.DataFrame()
df21 = pd.DataFrame()

df17 = pd.read_excel("C:\\Users\\USER\\Desktop\\DS\\project1\\2017_month_+2.xlsx")
df18 = pd.read_excel("C:\\Users\\USER\\Desktop\\DS\\project1\\2018_month_+2.xlsx")
df19 = pd.read_excel("C:\\Users\\USER\\Desktop\\DS\\project1\\2019_month_+2.xlsx")
df20 = pd.read_excel("C:\\Users\\USER\\Desktop\\DS\\project1\\2020_month_+2.xlsx")
df21 = pd.read_excel("C:\\Users\\USER\\Desktop\\DS\\project1\\2021_month_+2.xlsx")

# 2017년도 싱어송라이터 수
# 가수 == 작사가 or 가수 == 작곡가
is_lyricist = df17['가수'] == df17['작사가']
is_songwriter = df17['가수'] == df17['작곡가']
df17 = df17[is_lyricist | is_songwriter]
# print(df17.head())
# print(df17["가수"].count())

# [연도 : 곡 수] 형태의 데이터프레임으로 만들기
data_table = {"연도":"2017", "곡 수":df17["가수"].count()}
# print(data_table)
# print(type(data_table))
df_2017 = pd.DataFrame(data_table,index=range(0,1),columns=["연도","곡 수"])
print(df_2017)
print(type(df_2017))


# 2018년도 싱어송라이터 수
# 가수 == 작사가 or 가수 == 작곡가
is_lyricist = df18['가수'] == df18['작사가']
is_songwriter = df18['가수'] == df18['작곡가']
df18 = df18[is_lyricist | is_songwriter]
# print(df18.head())
# print(df18["가수"].count())

# [연도 : 곡 수] 형태의 데이터프레임으로 만들기
data_table = {"연도":"2018", "곡 수":df18["가수"].count()}
# print(data_table)
# print(type(data_table))
df_2018 = pd.DataFrame(data_table,index=range(0,1),columns=["연도","곡 수"])
print(df_2018)
print(type(df_2018))


# 2019년도 싱어송라이터 수
# 가수 == 작사가 or 가수 == 작곡가
is_lyricist = df19['가수'] == df19['작사가']
is_songwriter = df19['가수'] == df19['작곡가']
df19 = df19[is_lyricist | is_songwriter]
# print(df19.head())
# print(df19["가수"].count())

# [연도 : 곡 수] 형태의 데이터프레임으로 만들기
data_table = {"연도":"2019", "곡 수":df19["가수"].count()}
# print(data_table)
# print(type(data_table))
df_2019 = pd.DataFrame(data_table,index=range(0,1),columns=["연도","곡 수"])
print(df_2019)
print(type(df_2019))


# 2020년도 싱어송라이터 수
# 가수 == 작사가 or 가수 == 작곡가
is_lyricist = df20['가수'] == df20['작사가']
is_songwriter = df20['가수'] == df20['작곡가']
df20 = df20[is_lyricist | is_songwriter]
# print(df20.head())
# print(df20["가수"].count())

# [연도 : 곡 수] 형태의 데이터프레임으로 만들기
data_table = {"연도":"2020", "곡 수":df20["가수"].count()}
# print(data_table)
# print(type(data_table))
df_2020 = pd.DataFrame(data_table,index=range(0,1),columns=["연도","곡 수"])
print(df_2020)
print(type(df_2020))


# 2021년도 싱어송라이터 수
# 가수 == 작사가 or 가수 == 작곡가
is_lyricist = df21['가수'] == df21['작사가']
is_songwriter = df21['가수'] == df21['작곡가']
df21 = df21[is_lyricist | is_songwriter]
# print(df21.head())
# print(df21["가수"].count())

# [연도 : 곡 수] 형태의 데이터프레임으로 만들기
data_table = {"연도":"2021", "곡 수":df21["가수"].count()}
# print(data_table)
# print(type(data_table))
df_2021 = pd.DataFrame(data_table,index=range(0,1),columns=["연도","곡 수"])
print(df_2021)
print(type(df_2021))


# 하나의 데이터프레임으로 merge (2021년 제외)
df_merge = df_2017.append([df_2018,df_2019,df_2020], ignore_index=True)
print(df_merge)

# 막대 그래프
df_bar = df_merge.plot.bar(x="연도")
df_bar.set_xlabel("연도")
df_bar.set_ylabel("곡 수")
df_bar.set_title("연도별 싱어송라이터의 곡 수")
plt.ylim(100,300)
plt.savefig("C:\\Users\\USER\\Desktop\\DS\\project1\\data\\singersongwriter_bar.png",dpi=200)
plt.show()




# df_2017 = df.loc[(df_2017.가수 == df_2017.작사가) | (df_2017.가수 == df_2017.작곡가)]
# df_6.to_excel("C:\\Users\\USER\\Desktop\\DS\\project1\\data\\6_data.xlsx", index=False)
# print(df_2017.head())

# GenreCount_Summer = pd.DataFrame([df_6['장르'].value_counts(), df_7['장르'].value_counts(),
#                            df_8['장르'].value_counts()],
#                            index=['6월', '7월', '8월'])
# GenreCount_Summer = GenreCount_Summer.T
# print(GenreCount_Summer.head())

# print(type(df_list))  # 데이터프레임









