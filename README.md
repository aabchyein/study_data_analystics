<details>
<summary>Titanic From Disaster</summary>

#### DDA (기술통계분석)
| Variable | Definition | Key | 분석가 의견 |
| --- | --- | --- | --- |
| PassengerId | 승객 아이디 | | 수치형-이산형, 레코드 개수와 동일하기 때문에 분석에는 적당하지 않음 |
| survived | Survival | 0 = No, 1 = Yes | 범주형-명목형, 죽거나 살거나 두가지로 분류됨 |
| Pclass | Ticket class | 1 = 1st, 2 = 2nd, 3 = 3rd | 범주형-순서형, 티켓이 3개의 등급으로 분류됨 |
| Name | Name | | 범주형-명목형, 확인 결과 승객이 고유한 이름을 가지고 있음 |
| Sex | Sex | | 범주형-명목형, 확인 결과 male/female 두가지로 분류됨 |
| Age | Age in years | | 수치형-이산형 |
| Sibsp | # of siblings / spouses aboard the Titanic | | 수치형-이산형, 타이타닉에 동승한 형제/자매/배우자를 합친수로 각각 다른 값이 존재 |
| Parch | # of parents / children aboard the Titanic | | 수치형-이산형, 타이타닉에 동승한 부모님과 자녀를 합친수로 각각 다른 값이 존재 |
| Ticket | Ticket number | | 범주형-명목형, 탑승객마다 다른 티켓 번호를 가지고 있음 |
| Fare | Passenger fare(운임) | | 수치형-이산형 |
| Cabin | Cabin number(좌석번호) | | 범주형-명목형 |
| Embarked | Port of Embarkation(승선 항) | C = Cherbourg, Q = Queenstown, S = Southampton | | 범주형-명목형 |

</details>

<details>
<summary>TypeOfContractChannel</summary>

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
<summary>다변수 검증 Flowchart</summary>

### ■ 다변수 검증 FlowChart
![image](./images/혜인.drawio.png)

</details>
