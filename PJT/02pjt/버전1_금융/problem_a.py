import csv
import numpy as np
import pandas as pd

# CSV 파일 경로
csv_path = "PJT/02pjt/ver1/NFLX.csv"

# CSV 파일을 DataFrame으로 읽어오기 (Data, Open, High, Low, Close)
df = pd.read_csv(csv_path, usecols=range(5))

print(df)