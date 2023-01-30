**모션-그래프샘플** = 모션별 데이터 시각화 디렉터리<br>

**164179_LSTM_classification.ipynb** = lstm을 이용한 분류<br>

**check.h5** = 학습한 모델 저장<br>
**Data description** = 데이터 설명<br>
**epoch.log** = 학습 과정 저장 데이터<br>
**model_shape_info.png** = 모델 구조 이미지<br>

**train.csv** = train 데이터<br>
**val.csv** = validation 데이터(test 데이터) -> val.csv 정확도로 모델 성능 측정<br>

# base model
keras.io 의 Working with RNNs - MNIST 숫자 분류 모델
## 최적화
### overfitting 방지 기법
dropout(비율 = .2)<br>
early stopping<br>
가중치 감쇠(regularizers.l2)<br>

### 성능 향상 기법
학습률 조정(ReduceLROnPlateau)<br>
마지막 layer(Fully connected layer)에 softmax 적용<br>
parameter 조정(optimizer, batch size, 차원 수)<br>

### ver 1.
optimizer sgd, rmsprop, adam 비교하여 가장 좋은 성능(정확도)를 낸 adam 사용<br>
layer normalization 적용<br>

### ver 2.
l2 가중치 감쇠, 조기멈춤, 드롭아웃, 학습률 조정 적용<br>

### ver 3.
layer normalization 제거<br>
batch normalization 적용<br>