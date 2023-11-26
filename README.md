<details>
<summary>Titanic From Disaster(타이타닉 참사)</summary>

  #### DDA (기술통계분석)
| Variable | Definition | 분석가 의견 |
| --- | --- | --- |
| PassengerId | 승객 고유 식별 번호| 수치형-이산형, 레코드 개수와 동일하기 때문에 분석에는 적당하지 않음 |
| survived | 생존여부( 0 = No, 1 = Yes ) | 범주형-명목형, 죽거나 살거나 두가지로 분류됨 |
| Pclass | 선실 등급 ( 1 = 1st, 2 = 2nd, 3 = 3rd) | 범주형-순서형, 티켓이 3개의 등급으로 분류됨 |
| Name | 승객 이름 | 범주형-명목형, 확인 결과 승객이 고유한 이름을 가지고 있음 |
| Sex | 승객 성별 | 범주형-명목형, 확인 결과 male/female 두가지로 분류됨 |
| Age | 승객 나이 | 수치형-이산형 |
| Sibsp | 함께 탑승한 형제, 자매, 배우자의 수 | 수치형-이산형, 타이타닉에 동승한 형제/자매/배우자를 합친수로 각각 다른 값이 존재 |
| Parch | 함께 탑승한 부모, 자녀의 수 | 수치형-이산형, 타이타닉에 동승한 부모님과 자녀를 합친수로 각각 다른 값이 존재 |
| Ticket | 티켓 번호 | 범주형-명목형, 탑승객마다 다른 티켓 번호를 가지고 있음 |
| Fare | 지불한 운임 비용 | 수치형-이산형 |
| Cabin | 선실 번호 | 범주형-명목형 |
| Embarked | 탑승한 항구(C = Cherbourg, Q = Queenstown, S = Southampton) | 범주형-명목형 |

</details>

<details>
<summary>TypeOfContractChannel(계약 유형 채널)</summary>

#### DDA (기술통계분석)
| Variable | Definition | Key | 분석가 의견 |
| --- | --- | --- | --- |
| id | 아이디 | | 수치형-이산형, 레코드 개수와 동일하기 때문에 분석에는 적당하지 않음 |
| type_of_contract | 계약방식 | 렌탈, 멤버십 | 범주형-명목형, 2개의 카테고리로 분류되어 순서나 계량적 의마가 없음 |
| type_of_contract2 | 계약종류 | Promotion, Normal, TAS, ... | 범주형-명목형, 데이터 간 순서나 계량적 의미 없음 |
| channel | 채널 | 서비스 방문, 홈쇼핑/방송, 렌탈 재계약... | 범주형-명목형, 20개의 카테고리로 나누어지고 순서나 계량적 의미가 없음 |
| datetime | 계약 날짜 | | 범주형-순서형, 계약 날짜는 날짜 간에 순서는 있지만 날짜 간의 간격이 일정하지 않고 동일하지 않음 |
| Term | 계약 기간 | 60, 36, 12, 39 | 범주형-명목형, 4개의 카테고리로 분류됨 |
| payment_type | 결제방식 | CMS, 카드이체, 무통장, ... | 범주형-명목형, 5개의 카테고리로 순서 상관없이 나누어짐 |
| product | 제품 | K1, K2, K3, K4, ... | 범주형-명목형, 순서 상관없는 6개의 제품 카테고리로 분류됨 |
| amount | 제품 가격 | | 수치형-이산형, 정수 값을 가지고 있으며 제품마다 각기 다른 가격을 가지고 있음 |
| state | 상태 | 계약확정, 해약확정, 기간만료, ... | 범주형-명목형, 4개의 카테고리로 분류됨 |
| overdue_count | 연체횟수 | | 수치형-이산형, 연속적인 값 중 하나의 정수값으로 표현됨 |
| overdue | 연체 | 있음, 없음 | 범주형-명목형, 2개의 카테고리로 분류. 대부분 없음에 해당되어 분석에는 적당하지 않음 |
| credit rating | 신용등급 | 1, 2, 5, 8, ... | 범주형-순서형, 신용등급은 일정 범위 내에서 순서대로 구분됨 |
| bank | 은행 | 새마을금고, 현대카드, 우리은행, ... | 범주형-명목형 |
| cancellation | 취소 | 정상, 해약 | 범주형-명목형, 정상 혹은 해약 2개의 범주로 분류됨 |
| age | 나이 | | 수치형-연속형, 나이는 연속적인 숫자로 표현되며 정수 또는 소수점 형태로도 표현이 가능함 |
| Mileage | 마일리지 | | 수치형-이산형, amount에 따라 마일리지가 달라짐 |

</details>
<details>
<summary><strong>다변수 검증 FlowChart</strong></summary>

![image](./images/HyeIn.drawio.png)
</details>

## 데이터 분석 공부
#### 🔲사용기술
<img src="https://img.shields.io/badge/ANACONDA-44A833?style=for-the-badge&logo=ANACONDA&logoColor=white"> <img src="https://img.shields.io/badge/GITHUB-181717?style=for-the-badge&logo=GITHUB&logoColor=white"> <img src="https://img.shields.io/badge/SELENIUM-43B02A?style=for-the-badge&logo=SELENIUM&logoColor=white"> <img src="https://img.shields.io/badge/PYTHON-3776AB?style=for-the-badge&logo=PYTHON&logoColor=white"> <img src="https://img.shields.io/badge/MONGODB-47A248?style=for-the-badge&logo=MONGODB&logoColor=white"> <img src="https://img.shields.io/badge/MYSQL-4479A1?style=for-the-badge&logo=MYSQL&logoColor=white"> <img src="https://img.shields.io/badge/VISUAL STUDIO CODE-007ACC?style=for-the-badge&logo=VISUAL STUDIO CODE&logoColor=white"> <img src="https://img.shields.io/badge/JUPYTER-F37626?style=for-the-badge&logo=JUPYTER&logoColor=white">
### ✅Pandas
: 파이썬의 데이터 분석과 조작을 위한 라이브러리<br><br>
<판다스를 선택하는 이유>
- 데이터를 다루기 쉬운 두 가지 기본 데이터 구조인 Series와 DataFrame을 제공
- 특정 조건을 만족하는 데이터를 빠르게 추출하거나 원하는 방식으로 정렬
- 데이터를 효과적으로 통합하거나 연관된 정보를 결합하는 데 유용
- 데이터에서 누락된 값 또는 이상한 값들을 처리하고 정제하는 다양한 도구를 제공
- 다양한 통계 및 집계 함수를 제공
- 시각화 지
- 유연성과 확장성 : 다양한 형태의 데이터를 처리할 수 있으며, 다른 라이브러리와 쉽게 통합
### ✅Pandas
