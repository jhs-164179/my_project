# 제가 진행했던 프로젝트 입니다

## GLADNet-CBAM
1. https://github.com/weichen582/GLADNet - GLADNet(GLobal illumination-Aware and Detail-preserving Network)
2. https://arxiv.org/abs/1807.06521 - CBAM(Convolutional Block Attention Module)

GLADNet 논문과 깃허브 오픈소스를 토대로 구현하고 CBAM을 결합시켜서 성능향상 확인

졸업논문에 사용

(가벼운 UNet을 구현하고 UNet, GLADNet, GLADNet+CBAM 을 PSNR, SSIM, NIQE 점수와 Google Cloud Vision API를 이용해 비교)

## 제주도 급속 전기차 충전소 최적 입지 선정 & 웹페이지에 시각화

제주도 위도-경도를 기준으로 머신러닝을 이용해서 최적의 전기차 충전소 입지 선정
기존에 설치되어있는 충전소 위치를 최적의 위치라고 가정하고 randomforestclassifier 학습
모델의 FP를 새로운 최적의 충전소 위치로 가정
최적의 충전소 위치(위도-경도)값들을 knn clustering을 이용해 군집화하고 군집의 중심점을 최종 충전소입지로 설정

## LSTM을 이용한 모션 데이터 분류
