import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# ----- 1. 데이터 준비 -----
# 예제 데이터셋 생성 (각 심리검사 점수 + 정신 건강 상태)
data = {
    "simple_test_score": np.random.randint(0, 30, 100),  # 간단한 심리검사 점수
    "mbti_score": np.random.randint(0, 20, 100),  # MBTI 검사 점수 (추상적 지표)
    "depression_score": np.random.randint(0, 27, 100),  # 우울증 테스트 점수 (PHQ-9 기준)
    "suicide_risk_score": np.random.randint(0, 10, 100),  # 자살 위험성 점수
    "mental_health_status": np.random.choice(["정상", "경미한 문제", "심각한 문제"], 100)  # 레이블
}

df = pd.DataFrame(data)

# ----- 2. 데이터셋 분할 -----
X = df.drop(columns=["mental_health_status"])  # 입력 데이터 (Feature)
y = df["mental_health_status"]  # 예측 대상 (Label)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ----- 3. 랜덤 포레스트 모델 훈련 -----
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)
rf_acc = accuracy_score(y_test, y_pred_rf)
print(f"랜덤 포레스트 정확도: {rf_acc:.2f}")

# ----- 4. SVM 모델 훈련 -----
svm_model = SVC(kernel="linear", probability=True)
svm_model.fit(X_train, y_train)
y_pred_svm = svm_model.predict(X_test)
svm_acc = accuracy_score(y_test, y_pred_svm)
print(f"SVM 정확도: {svm_acc:.2f}")

# ----- 5. 모델 저장 -----
joblib.dump(rf_model, "rf_model.pkl")
joblib.dump(svm_model, "svm_model.pkl")
print("🎯 모델 저장 완료: rf_model.pkl, svm_model.pkl")
