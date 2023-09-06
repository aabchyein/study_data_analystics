<details>
<summary>db_NHIS.NSC2_BND</summary>

### DDA
| 변수명    | 변수 설명 | 변수값 설명 | |
|-----------|---------------|--------| ----- |
| RN_INDI | 개인고유번호 | 7자리의 개인 고유번호, 연계코드 | 범주형-명목형, 분석에 필요 |
| BTH_YYYY | 출생년도(1921~2015) | 대상자의 출생년도, 기준년도에서 출생년도를 뺀 값으로 산출됨 | 날짜형(순서형) 또는 범주형|
| DTH_YYYYMM | 사망연월 | 사망자의 사망연월, 년월로 표기됨 | 날짜형(순서형) 또는 범주형-연속형 |
| COD1 | 사망원인1 | 한국표준질병‧사인분류(KCD) 코드 사용, 사망 원인을 상위 1차 분류로 기재된 코드 | 범주형 |
| COD2 | 사망원인2 | 한국표준질병‧사인분류(KCD) 코드 사용, 사망 원인을 상위 2차 분류(상세 원인)로 기재된 코드 | 범주형, 이차 사망 원인 |

### 분석 기준 : 년도별 주요 사망 원인 분석(X:DTH_YYYYMM<사망연월>, Y:COD1<사망원인1>)

</details>


<details>
<summary>db_medicals.RecurrenceOfSurgery</summary>

### DDA
| 변수명 | 변수설명 | |
|-------------|---------------------|-------- |
| _id | Unique identifier for each row (각 행마다 고유한 식별자) | 범주형-명목형 |
| Unnamed: 0 | Index column (인덱스 열) | |
| 환자ID | Unique identifier for each patient (각 환자마다 고유한 식별자) | |
| Large Lymphocyte | 특정 의료 상태를 나타낼 수 있는 백혈구 중 하나인 대형 림프구 | |
| Location of herniation | Location of herniated disc in the spine (척추의 돌출 디스크 위치) | |
| ODI | Oswestry Disability Index(요통 환자의 기능적 장애를 측정하는 Oswestry 장애 지수) | |
| 가족력 | Family history of medical conditions (가족 내 질환 이력) |  |
| 간질성폐질환 | Chronic obstructive pulmonary disease (COPD) (만성 폐쇄성 폐질환) | |
| 고혈압여부 | Presence or absence of hypertension (고혈압 여부) | |
| 과거수술횟수 | Number of past surgeries (과거 수술 횟수) | |
| 당뇨여부 | Presence or absence of diabetes (당뇨 진단 여부) | |
| 말초동맥질환여부 | Presence or absence of peripheral arterial disease (말초동맥질환 여부) | |
| 빈혈여부 | Presence or absence of anemia (빈혈 여부) | |
| 성별 | Gender (성별) | |
| 스테로이드치료 | Use of steroid medication for treatment (스테로이드 치료 여부) | |
| 신부전여부 | Presence or absence of renal failure (신장 기능 장애 여부) | |
| 신장 | Height (신장) | |
| 심혈관질환 | Presence or absence of cardiovascular disease (심혈관 질환 여부) |  |
| 암발병여부 | Presence or absence of cancer (암 발병 여부) | |
| 연령 | Age at time of data collection (데이터 수집 시 나이) | |
| 우울증여부 | Presence or absence of depression (우울증 여부) | |
| 입원기간 | Length of hospital stay (입원 기간) | |
| 입원일자 | Date of admission to hospital (입원 일자) | |
| 종양진행여부 | Presence or absence of tumor progression (종양 진행 여부) | |
| 직업 | Occupation (직업) | |
| 체중 | Body weight (체중) | |
| 퇴원일자 | Date of discharge from hospital (퇴원 일자) | |
| 헤모글로빈수치 | Hemoglobin level in the blood (혈중 헤모글로빈 수치) | |
| 혈전합병증여부 | Presence or absence of thromboembolism (혈전 합병증 여부) | |
| 환자통증정도 | Severity of patient's pain (환자의 통증 정도) | |
| 흡연여부 | Presence or absence of smoking habit (흡연 여부) | |
| 통증기간(월) | Duration of pain, in months (통증 기간, 달 단위) | |
| 수술기법 | Surgical technique used (수술 기술) | |
| 수술시간 | Duration of surgery (수술 시간) | |
| 수술실패여부 | Presence or absence of surgical failure (수술 실패 여부) | |
| 수술일자 | Date of surgery (수술 일자) | |
| 재발여부 | 의료 상태 재발 여부 | |
| 혈액형 | Blood type (혈액형) | |
| 전방디스크높이(mm) | 전방 디스크 높이, 밀리미터 단위 | |
| 후방디스크높이(mm) | 후방 디스크 높이, 밀리미터 단위 | |
| 지방축적도 | Degree of fat accumulation (지방 축적 정도) | |
| Instability | Presence or absence of spinal instability (척추 불안정 여부) | |
| MF + ES | Presence or absence of Modic type I changes (Modic 타입 I 변화 여부) | |
| Modic change | Presence or absence of Modic changes (Modic 변화 여부) | |
| PI | Pelvic Incidence, measured in degrees (골반 기울기, 도 단위) | |
| PT | Pelvic Tilt, measured in degrees (골반 틸트, 도 단위) | |
| Seg Angle(raw) | Segmental angle, measured in degrees (세그먼트 각도, 도 단위) | |
| Vaccum disc | Presence or absence of vacuum phenomena in the disc (디스크 내 진공 현상 여부) | |
| 골밀도 | Bone density (골밀도) | |
| 디스크단면적 | Disc cross-sectional area (디스크 단면적) | |
| 디스크위치 | Location of the disc in the spine (척추의 디스크 위치) | |
| 척추이동척도 | Degree of spinal displacement (척추 이동 정도) | |
| 척추전방위증 | Presence or absence of spondylolisthesis (척추 전방 이탈증 여부) | |

### 분석 기준 : 연령별 퇴원까지 걸린 날짜 분석(X:<연령>, Y:<퇴원날짜>)

</details>