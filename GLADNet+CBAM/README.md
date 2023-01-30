**checkpoint** = 학습한 모델을 저장하는 디렉터리<br>
**compare_img** = 결과 이미지들을 psnr,ssim,niqe 점수를 이용하여 비교하는 디렉터리<br>
**data** = train, test, eval 데이터(이미지)가 있는 디렉터리<br>
**model** = 테스트 단계에서 저장된 모델을 가져오는 디렉터리<br>
**models** = simple_unet, original_gladnet의 model.py가 저장되어있는 디렉터리<br>
**paper_readme** = gladnet, cbam 영문 readme.md파일 저장 디렉터리<br>
**results** = 논문그대로 train한 후 test한 이미지를 저장한 디렉터리<br>
**sample** = train단계에서 변화된 검증용 데이터를 저장한 디렉터리<br>
**test_results** = data의 test데이터를 test한 결과를 저장한 디렉터리<br>
**main.py** = 실행 파일<br>
**model.py** = GLADNet+CBAM 모델, 학습 및 테스트 과정 등의 클래스 정의<br>
**utils.py** = 데이터 증강, 이미지 불러오기, 이미지 저장 함수<br>

# GLADNet
입력된 저조도 이미지에 대해 조명 측정 단계 - 세부 재구성 단계를 이용해 밝기를 향상시키는 모델

## 조명 측정 단계
인코더-디코더 네트워크를 이용해 고정 크기의 조명 측정치를 생성<br>
U-Net, Resnet의 구조와 유사<br>
1. Resize 함수와 nearest neighbor interporation을 사용하여 입력이미지를 고정된 크기로 다운샘플링<br>
2. CNN+Relu의 다운샘플링(CNN stride=2로 구현)-업샘플링(Resize 함수로 구현) 블록을 통과(인코더-디코더 네트워크)<br>
잔차(residual)를 학습할 수 있도록 다운 샘플링 블록의 출력은 같은 사이즈를 처리하는 업 샘플링 블록의 특징 맵으로 전달 후 합산<br>
3. Resize 함수와 CNN을 통과하여 원래 이미지의 크기를 가지는 밝기 정보 특징 맵 획득

## 세부 재구성 단계
CNN을 이용해 입력 이미지와 조명 측정 단계의 출력값을 이용해(잔차 학습) 세부사항을 보완하여 이미지 품질 향상<br>
ResNet의 구조와 유사<br>
1. 조명 측정 단계의 특징 맵과 입력 이미지를 결합
2. CNN+Relu 5개를 거치며 이미지와 밝기 정보를 조합하고 최종적으로 품질이 향상된 이미지 생성

# CBAM
특징 맵을 입력받아 Channel, Spatial 두 가지 Attention 모듈을 거쳐 보완된 특징 맵 출력<br>

## Channel Attention 모듈
1. 계산 효율의 향상을 위해 차원을 1x1로 압축
2. Max, Avg 풀링 & MLP 적용한 두가지 Attention map 생성
3. 각각의 Attention map 결합 & sigmoid 함수 적용 정규화(중요한 정보는 강조하고 불필요한 정보는 억제)<br>
특징 맵에서 '무엇'이 중요한지에 대한 정보를 가지는 Channel Attention map 생성

## Spatial Attention 모듈
1. 입력받은 특징 맵에 Channel Attention map을 곱한 값을 입력받아 Max, Avg 풀링 & 7x7 CNN 적용
2. sigmoid 함수 적용 정규화<br>
'어디'에 중요한 게 있는지에 대한 정보를 가지는 Spatial Attention map 생성<br>
3. 최종적으로 입력 값인 특징 맵에 Channel, Spatial Attention map을 곱해주어 개선된 성능을 가지는 특징 맵 생성
