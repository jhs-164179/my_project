# data_project

# 전기차 충전소 입지 선정에 관한 코드입니다
**final_2** = 가공한 데이터들을 merge하여 최종 데이터 셋을 만드는 디렉터리<br>
**final_data** = 가공한 최종 데이터들이 있는 디렉터리<br>

**model_testing** = 사용한 머신러닝 모델들을 저장한 폴더<br>

**preprocessing.ipynb** = 전처리 과정<br>
**final_of_final_preprocessing.csv** = 전처리 과정이 끝난 데이터 셋<br>

**machine_learning.ipynb** = 머신러닝 모델을 이용한 데이터 분석 과정<br>

**web** = 백엔드로 **Django**를 이용해 생성한 웹 페이지 

## 데이터 분석 개요
현재 설치되어 있는 950개의 급속 충전소가 최적의 입지에 설치되었다고 가정
위도-경도 값 기준으로 데이터 셋 생성
분류모델들을 비교하여 정확도가 가장 높은 모델 선택
FP(False Positive)를 최적의 입지로 설정
클러스터링 모델의 실루엣계수와 응집도를 비교하여 적절한 군집의 개수 선택
FP값들을 군집화하여 군집별 중심점을 최종 충전소 입지로 선정

## 데이터 셋 생성
공공데이터 포털, 제주 데이터 허브 등의 사이트에서 파일 다운로드, 크롤링 등을 이용하여 취득한 정보를 pandas를 이용해 merge<br>
제주도의 위도-경도 값 기준으로 97945개의 데이터를 갖는 데이터 셋 생성<br>
위도-경도 단위 데이터를 얻기 어려운 인구수,교통량,차량등록수 데이터는 시,읍,면 단위로 수집하여 merge<br>
경제활동인구수는 15세 이상 인구에 경제활동비율을 곱하여 추정치 산출<br>

## 전처리
1. 문자열 처리
공백, 특수문자 등 쓸데없는 문자 제거<br>

2. 결측치 처리 & 중복 제거
pandas fillna, dropduplicates 함수 사용<br>

3. encoding, scaling
t,f 값을 갖는 데이터 -> Label Encoder<br>
인구수 등의 수치형 데이터 -> MinMax Scaler<br>

4. pca분석, 차원압축
pandas df.corr 함수를 이용해 상관계수 분석<br>
pca분석을 통해 8개 컬럼을 2개의 컬럼으로 차원 압축<br>

5. 최종 변수
독립변수: 침수우려여부, cctv 설치 여부, 관광객 수, 인구, 전기차 전년대비 증감율, 인구, 전기차 2개년 통계(차원 압축 데이터)<br>
종속변수: 급속 충전기 설치 유무<br>

## 지도학습 분류 model 
**Grid Search CV 분석 결과**
1. Logistic Regression : acc 68%
2. GaussianNB : acc 49.5%
3. KNeighborsClassifier : acc 57.5%
4. RandomForestClassifier : acc 69%

RandomForestClassifier를 사용하여 분류

## 비지도학습 클러스터링(군집화) model
Kmeans Clustering model 사용
1. 실루엣 계수 분석
2. 응집도 분석
3. 도출한 최적의 군집별 중심점을 최종 최적의 충전소 입지로 선정

## 웹 사이트 시각화
카카오 맵 api를 이용하여 최적의 충전소 입지에 마커 생성 후 시각화