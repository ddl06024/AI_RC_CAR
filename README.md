# AI_RC_CAR 개발 명세
## 프로젝트 소개
- RC카 모형과 아두이노, 라즈베리파이를 이용하여 자율주행 자동차 제작
- 인공지능 기술을 활용하여 자동차가 나아가야할 방향 및 속도를 예측

## 개발 환경
- 언어: C, Python
- 사용 프로그램: 아두이노 IDE, Thonny
- 딥러닝 프레임워크: keras

## 라이브러리
- matplotlib: `sudo pip install matplotlib numpy`로 설치
- gfortran: `sudo pip install gfortran libblas-dev liblapack-dev`로 설치
- scipy: `sudo pip install scipy`로 설치
- scikit-learn: `sudo pip in stall scikit-learn`로 설치
- keras: `pip install keras`로 설치
- pandas: `pip install pandas`로 설치 

## 하드웨어 
- 아두이노: 자동차 바퀴의 구동을 담당
- 라즈베리파이4: CPU의 역할
- L9110S 모터 드라이브
- 라즈베리파이 카메라 모듈

## 파일 
- Self_driving.py: 자동차 구동
- Tf_learn.py: 딥러닝 모델 학습과 이미지를 받아 자동차의 속도와 방향 예측
- rc_car_interface.py: 자동차의 인터페이스 -> 자동차에 연결된 카메라로 이미지 받아옴, 아두이노와 통신
- Get_image_data.py: 이미지 데이터 전처리
- motor2.ino: 바퀴의 속도 구동

## 구현 영상
