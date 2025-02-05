import streamlit as st
import joblib
import numpy as np

# ----- 1. 모델 로드 -----
rf_model = joblib.load("rf_model.pkl")  # 랜덤 포레스트 모델 로드
svm_model = joblib.load("svm_model.pkl")  # SVM 모델 로드

def predict_mental_health(simple_score, mbti_score, depression_score, suicide_score):
    user_data = np.array([[simple_score, mbti_score, depression_score, suicide_score]])
    
    # 랜덤 포레스트 예측
    rf_prediction = rf_model.predict(user_data)[0]
    rf_prob = rf_model.predict_proba(user_data)
    
    # SVM 예측
    svm_prediction = svm_model.predict(user_data)[0]
    
    return rf_prediction, svm_prediction, rf_prob

# ----- 2. Streamlit UI -----
def run_prediction():
    st.title("🧠 심리 상태 예측")

    st.write("아래에서 검사 결과 점수를 입력하세요. 머신러닝 모델이 심리 상태를 예측해 줍니다.")

    simple_score = st.slider("📋 간단한 심리검사 점수", 0, 30, 10)
    mbti_score = st.slider("🧩 MBTI 검사 점수", 0, 20, 10)
    depression_score = st.slider("😔 우울증 테스트 점수", 0, 27, 10)
    suicide_score = st.slider("⚠️ 자살 위험성 점수", 0, 10, 5)

    if st.button("예측하기"):
        rf_result, svm_result, rf_prob = predict_mental_health(simple_score, mbti_score, depression_score, suicide_score)
        
        st.subheader(f"📊 랜덤 포레스트 예측 결과: {rf_result}")
        st.write(f"🌡 확률 분포: {rf_prob}")
        
        st.subheader(f"📈 SVM 예측 결과: {svm_result}")
        
        if rf_result == "심각한 문제" or svm_result == "심각한 문제":
            st.error("🚨 심리 건강에 대한 추가적인 상담이 필요할 수 있습니다. 전문가와 상담해보세요.")
        elif rf_result == "경미한 문제" or svm_result == "경미한 문제":
            st.warning("⚠️ 경미한 심리적 문제가 있을 수 있습니다. 생활 습관을 점검해보세요.")
        else:
            st.success("✅ 정상적인 심리 상태입니다!")
