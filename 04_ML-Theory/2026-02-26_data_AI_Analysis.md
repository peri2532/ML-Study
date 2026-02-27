데이터 전처리 (Data Preprocessing)
1.1 데이터 전처리 개념

분석 전에 데이터를 정비하는 모든 작업을 의미한다.

불필요한 컬럼 제거

결측치 처리

범주형 → 수치형 변환

정규화/표준화

샘플링

1.2 표본추출 (Sampling)

모집단을 대표할 수 있도록 데이터를 추출하는 과정

주요 방법

단순임의추출

층화임의추출

체계적추출

집락추출

2️⃣ 기술통계 & 추론통계
2.1 평균 (Mean)
𝑥
ˉ
=
1
𝑛
∑
𝑖
=
1
𝑛
𝑥
𝑖
x
ˉ
=
n
1
	​

i=1
∑
n
	​

x
i
	​

2.2 분산 (Variance)
𝑠
2
=
∑
𝑖
=
1
𝑛
(
𝑥
𝑖
−
𝑥
ˉ
)
2
𝑛
−
1
s
2
=
n−1
∑
i=1
n
	​

(x
i
	​

−
x
ˉ
)
2
	​

2.3 표준편차 (Standard Deviation)
𝑠
=
𝑠
2
s=
s
2
	​

2.4 사분위 범위 (IQR)
𝐼
𝑄
𝑅
=
𝑄
3
−
𝑄
1
IQR=Q
3
	​

−Q
1
	​

3️⃣ 확률분포 (Probability Distribution)
3.1 정규분포 (Normal Distribution)

확률밀도함수(PDF):

𝑓
(
𝑥
)
=
1
2
𝜋
𝜎
2
𝑒
−
(
𝑥
−
𝜇
)
2
2
𝜎
2
f(x)=
2πσ
2
	​

1
	​

e
−
2σ
2
(x−μ)
2
	​


표기:

𝑋
∼
𝑁
(
𝜇
,
𝜎
2
)
X∼N(μ,σ
2
)
3.2 표준정규분포 (Standard Normal Distribution)
𝑍
=
𝑋
−
𝜇
𝜎
Z=
σ
X−μ
	​

𝑍
∼
𝑁
(
0
,
1
)
Z∼N(0,1)
3.3 t-분포
𝑡
=
𝑥
ˉ
−
𝜇
𝑠
/
𝑛
t=
s/
n
	​

x
ˉ
−μ
	​


자유도:

𝑑
𝑓
=
𝑛
−
1
df=n−1
3.4 카이제곱분포
𝜒
2
=
∑
(
𝑂
−
𝐸
)
2
𝐸
χ
2
=∑
E
(O−E)
2
	​

3.5 F-분포
𝐹
=
𝑆
1
2
𝑆
2
2
F=
S
2
2
	​

S
1
2
	​

	​

4️⃣ 가설검정
4.1 1종 오류
𝛼
=
𝑃
(
Type I Error
)
α=P(Type I Error)
4.2 2종 오류
𝛽
=
𝑃
(
Type II Error
)
β=P(Type II Error)
4.3 검정력
𝑃
𝑜
𝑤
𝑒
𝑟
=
1
−
𝛽
Power=1−β
5️⃣ 연관규칙 분석 (Association Rule)
5.1 지지도 (Support)
𝑆
𝑢
𝑝
𝑝
𝑜
𝑟
𝑡
(
𝐴
→
𝐵
)
=
𝐴
∩
𝐵
전체거래수
Support(A→B)=
전체거래수
A∩B
	​

5.2 신뢰도 (Confidence)
𝐶
𝑜
𝑛
𝑓
𝑖
𝑑
𝑒
𝑛
𝑐
𝑒
(
𝐴
→
𝐵
)
=
𝑆
𝑢
𝑝
𝑝
𝑜
𝑟
𝑡
(
𝐴
∩
𝐵
)
𝑆
𝑢
𝑝
𝑝
𝑜
𝑟
𝑡
(
𝐴
)
Confidence(A→B)=
Support(A)
Support(A∩B)
	​


또는

𝐶
𝑜
𝑛
𝑓
𝑖
𝑑
𝑒
𝑛
𝑐
𝑒
(
𝐴
→
𝐵
)
=
𝑃
(
𝐵
∣
𝐴
)
Confidence(A→B)=P(B∣A)
5.3 향상도 (Lift)
𝐿
𝑖
𝑓
𝑡
(
𝐴
→
𝐵
)
=
𝐶
𝑜
𝑛
𝑓
𝑖
𝑑
𝑒
𝑛
𝑐
𝑒
(
𝐴
→
𝐵
)
𝑆
𝑢
𝑝
𝑝
𝑜
𝑟
𝑡
(
𝐵
)
Lift(A→B)=
Support(B)
Confidence(A→B)
	​

6️⃣ 분류모델 평가 (Classification Metrics)

오차행렬 구성:

	실제 양성	실제 음성
예측 양성	TP	FP
예측 음성	FN	TN
6.1 정밀도 (Precision)
𝑃
𝑟
𝑒
𝑐
𝑖
𝑠
𝑖
𝑜
𝑛
=
𝑇
𝑃
𝑇
𝑃
+
𝐹
𝑃
Precision=
TP+FP
TP
	​

6.2 재현율 (Recall, Sensitivity)
𝑅
𝑒
𝑐
𝑎
𝑙
𝑙
=
𝑇
𝑃
𝑇
𝑃
+
𝐹
𝑁
Recall=
TP+FN
TP
	​

6.3 특이도 (Specificity)
𝑆
𝑝
𝑒
𝑐
𝑖
𝑓
𝑖
𝑐
𝑖
𝑡
𝑦
=
𝑇
𝑁
𝑇
𝑁
+
𝐹
𝑃
Specificity=
TN+FP
TN
	​

6.4 정확도 (Accuracy)
𝐴
𝑐
𝑐
𝑢
𝑟
𝑎
𝑐
𝑦
=
𝑇
𝑃
+
𝑇
𝑁
𝑇
𝑃
+
𝑇
𝑁
+
𝐹
𝑃
+
𝐹
𝑁
Accuracy=
TP+TN+FP+FN
TP+TN
	​

6.5 F1 Score
𝐹
1
=
2
×
𝑃
𝑟
𝑒
𝑐
𝑖
𝑠
𝑖
𝑜
𝑛
×
𝑅
𝑒
𝑐
𝑎
𝑙
𝑙
𝑃
𝑟
𝑒
𝑐
𝑖
𝑠
𝑖
𝑜
𝑛
+
𝑅
𝑒
𝑐
𝑎
𝑙
𝑙
F1=2×
Precision+Recall
Precision×Recall
	​

7️⃣ 머신러닝 알고리즘 정리

PDF 기준 포함 알고리즘:

지도학습

K-Nearest Neighbors (KNN)

Decision Tree

Random Forest

SVM

Logistic Regression

비지도학습

Clustering

PCA

딥러닝

ANN

DNN

CNN

RNN

8️⃣ 머신러닝 파이썬 라이브러리
라이브러리	역할
pandas	데이터 처리
numpy	수치 연산
matplotlib	시각화
seaborn	통계 시각화
statsmodels	통계 분석
scikit-learn	머신러닝
tensorflow	딥러닝