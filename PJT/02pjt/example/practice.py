# 패키지 import
import numpy as np # 배열 계산
import pandas as pd # 데이터 추출, 분석
import matplotlib.pyplot as plt # 시각화

# CSV 파일 경로
csv_path = "PJT/02pjt/example/archive/google-stock-dataset-Monthly.csv"

# CSV 파일 읽어오기 (첫 번째, 마지막 열 제외)
df = pd.read_csv(csv_path, usecols=range(1, 7))

# 데이터 출력
# DataFrame 출력
print(df)

# 데이터 타입 확인
print(df.dtypes)

# 최저, 최고, 종가 그래프
# 날짜 데이터 변환
df["Date"] = pd.to_datetime(df["Date"])

# 그래프 그리기
plt.plot(df['Date'], df['Close'], label='Close')
plt.plot(df['Date'], df['Low'], label='Low')
plt.plot(df['Date'], df['High'], label='High')

# 그래프 제목 설정
plt.title('High, Low Prices over Time')

# x축 레이블 설정
plt.xlabel('Date')

# y축 레이블 설정
plt.ylabel('Price')

# 범례 표시
plt.legend()

# 그래프 표시
plt.show()

'''
# 2021년 이후 최저, 최고가 출력
# CSV 파일 읽어오기 (첫 번째, 마지막 열 제외)
new_df = pd.read_csv(csv_path, usecols=range(1, 7))

# 2022년 이후 데이터 필터링
df_after_2022 = new_df[new_df["Date"] >= "2022-01-01"]

# 출력하기
print(df_after_2022)

# 그래프 그리기
plt.plot(df_after_2022['Date'], df_after_2022['Low'], label='Low')
plt.plot(df_after_2022['Date'], df_after_2022['High'], label='High')

# 그래프 제목 설정
plt.title('High, Low Prices After 2022')

# x축 레이블 설정
plt.xlabel('Date')

# x 축 설정(회전시키기)
plt.xticks(rotation=45)

# y축 레이블 설정
plt.ylabel('Price')

# 범례 표시
plt.legend()

# 그래프 표시
plt.show()
'''
'''
# 원화로 바꾸기
# CSV 파일 읽어오기 (첫 번째, 마지막 열 제외)
new_df = pd.read_csv(csv_path, usecols=range(1, 7))

# 2022년 이후 데이터 필터링
df_after_2022 = new_df[new_df["Date"] >= "2022-01-01"]

# 원화 환율 (예시로 1달러당 1300원으로 가정)
exchange_rate = 1300

# 각 컬럼을 원화로 계산하여 추가
df["High(won)"] = df["High"] * exchange_rate
df["Low(won)"] = df["Low"] * exchange_rate
df["Close(won)"] = df["Close"] * exchange_rate

# 2022년 이후 데이터 필터링
df = df[new_df["Date"] >= "2022-01-01"]

# 수정된 데이터프레임 출력
print(df)

# 그래프 그리기
plt.plot(df['Date'], df['Low(won)'], label='Low(won)')
plt.plot(df['Date'], df['High(won)'], label='High(won)')
plt.plot(df['Date'], df['Close(won)'], label='Close(won)')

# 그래프 제목 설정
plt.title('High, Low, CLose Prices after 2022, exchange')

# x축 레이블 설정
plt.xlabel('Date')

# y축 레이블 설정
plt.ylabel('Price(won)')

# x 축 설정(회전시키기)
plt.xticks(rotation=45)

# 범례 표시
plt.legend()

# 그래프 표시
plt.show()
'''
'''
# 상관 관계 분석
# 가장 최근을 제외한 마지막 1년 추출
df = df.tail(13)

# 마지막 개월의 Close 가격
last_month_close = df['Close'].iloc[-1]

# 마지막 개월을 제외한 1년의 데이터와 마지막 개월의 종가 간의 상관 관계
High_Close_corr = df['High'].iloc[:-1].corr(df['Close'])
Low_Close_corr = df['Low'].iloc[:-1].corr(df['Close'])
Volume_Colse_corr = df['Volume'].iloc[:-1].corr(df['Close'])

print(f"지난 1년의 High 가격과 마지막 개월의 Close 가격과의 상관 관계: {High_Close_corr}")
print(f"지난 1년의 평균 최고가: {df['High'].iloc[:-1].mean()}")

print('----------------------------------------------')

print(f"지난 1년의 Low 가격과 마지막 개월의 Close 가격과의 상관 관계: {Low_Close_corr}")
print(f"지난 1년의 평균 최저가: {df['Low'].iloc[:-1].mean()}")

print('----------------------------------------------')

print(f"지난 1년의 거래량과 마지막 개월의 Close 가격과의 상관 관계: {Volume_Colse_corr}")
print(f"지난 1년의 평균 거래량: {df['Volume'].iloc[:-1].mean()}")

print('----------------------------------------------')

# 그래프 그리기
plt.plot(df['Date'], df['Close'], label='Close')
plt.plot(df['Date'], df['Low'], label='Low')
plt.plot(df['Date'], df['High'], label='High')

# 그래프 제목 설정
plt.title('High, Low Prices over Time')

# x축 레이블 설정
plt.xlabel('Date')

# y축 레이블 설정
plt.ylabel('Price')

# x 축 설정(회전시키기)
plt.xticks(rotation=45)

# 범례 표시
plt.legend()

# 그래프 표시
plt.show()
'''