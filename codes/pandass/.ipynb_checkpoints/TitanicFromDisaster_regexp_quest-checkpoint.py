# 퀘스트
# Name 변수로 성씨와 결혼 유무 컬럼 생성
# hint : 성씨 컬럼에 Nan 없어야 함.

import pandas as pd

df_TFD =pd.read_csv('datasets/TitanicFromDisaster_train.csv')
df_name = pd.DataFrame(df_TFD['Name'])
print(df_name)

# Name에서 성씨 가져오기
pattern = '^([A-z]*)'
df_Name_extract = df_name['Name'].str.extract(pattern)
print(df_Name_extract)

# last name 컬럼 생성
df_name['LastName'] = df_Name_extract
print(df_name)

# 결혼 유무 (Mr/Mrs/Miss) 가져오기
pattern = '(Mrs|Mr|Miss)'
df_Marriage = df_name['Name'].str.extract(pattern)
print(df_Marriage)

# 결혼 유무 컬럼 생성
df_name['MARSTA'] = df_Marriage
print(df_name)

# 결혼 유무에 NaN값 들어있는 컬럼 drop 시키기
df_name = df_name.dropna().copy()
print(df_name)