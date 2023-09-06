import pandas as pd

double_list = [
                [1000, '과자','2019-12-31','반품'],
                [2000, '음료', '2020-03-02', '정상'],
                [3000, '아이스크림', '2020-02-03','정상'],
                [1000,'과자','2019-12-31','반품']
               ]
double_columns = ['가격','종류','판매일자','반품여부']
df_saledays = pd.DataFrame(data=double_list, columns=double_columns)
print(df_saledays)

# 단일변수 처리 with apply()
def mean_subtraction(cell_value) :
    result = 1750 - cell_value    # 가격 평균 - 개별 값
    return result

mean_subtraction(750) # fuction 호출

df_saledays['가격'].apply(mean_subtraction)  # 각 cell당 평균과의 차이값

# 다변수 처리 with apply()
# BMI 구할 때 소스코드
# def calculate_bmi(row):
#     height_meters = row['height'] / 100  # Convert height to meters
#     bmi = row['weight'] / (height_meters ** 2)
#     return bmi
def calculate_sum(row):  # row라는 변수에 레코드 전체가 담겨서 내가 필요한 부분(column)만 뽑아 계산을 해서 return으로 던질 수 있음
    result = row['가격'] * 20
    return result

df_saledays['가격합'] = df_saledays.apply(calculate_sum, axis='columns')  # axis로 옵션을 줌. 기본은 index 옵션이 들어가 있음
# print(df_saledays)

# 판다스 데이터프레임 apply()
# Refer) https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html


# regexpress(정규식)
data = {'Names': ['김지수', '박지민', '이태용', '최수영']}

df_Name = pd.DataFrame(data)

print(df_Name)

pattern = r'^([가-힣])'   # 첫번째 글자가 한글인 것

df_Name_extract = df_Name['Names'].str.extract(pattern)
print(df_Name_extract)