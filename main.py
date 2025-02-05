import streamlit as st
import plotly.express as px
import datetime
import joblib
import numpy as np

# ----- 기본 설정 -----
st.set_page_config(page_title="심리검사 대시보드", layout="wide")

# ----- 머신러닝 모델 로드 -----
rf_model = joblib.load("rf_model.pkl")  # 랜덤 포레스트 모델 로드
svm_model = joblib.load("svm_model.pkl")  # SVM 모델 로드

# ----- 세션 상태 초기화 -----
if "simple_test_score" not in st.session_state:
    st.session_state["simple_test_score"] = []

if "mbti_score" not in st.session_state:
    st.session_state["mbti_score"] = []

if "depression_score" not in st.session_state:
    st.session_state["depression_score"] = []

if "suicide_risk_score" not in st.session_state:
    st.session_state["suicide_risk_score"] = []

if "test_dates" not in st.session_state:
    st.session_state["test_dates"] = []  # 검사 날짜 저장

# 🔹 값이 리스트가 아닐 경우 리스트로 변환 (에러 방지)
for key in ["simple_test_score", "mbti_score", "depression_score", "suicide_risk_score"]:
    if isinstance(st.session_state[key], int):
        st.session_state[key] = [st.session_state[key]]

# ----- 사이드바 (네비게이션) -----
st.sidebar.title("🧠 심리검사 선택")
menu = st.sidebar.radio(
    "검사를 선택하세요:", 
    ["대시보드", "간단한 심리검사", "MBTI 검사", "우울증 테스트", "자살 위험성 평가", "심리검사 결과 예측"]
)

# ----- 📊 대시보드 (검사 결과 확인) -----
if menu == "대시보드":
    st.title("📊 심리검사 대시보드")
    st.write("최근 검사 결과를 확인하세요.")

    col1, col2 = st.columns(2)

    # ✅ 검사 날짜 설정 (X축)
    dates = st.session_state["test_dates"] if st.session_state["test_dates"] else ["기록 없음"]
    
    # ✅ 검사 점수 설정 (Y축) - 기본값 0점 추가
    simple_scores = st.session_state["simple_test_score"] if st.session_state["simple_test_score"] else [0]
    mbti_scores = st.session_state["mbti_score"] if st.session_state["mbti_score"] else [0]
    depression_scores = st.session_state["depression_score"] if st.session_state["depression_score"] else [0]
    suicide_scores = st.session_state["suicide_risk_score"] if st.session_state["suicide_risk_score"] else [0]

    with col1:
        st.subheader("📋 간단한 심리검사")
        fig1 = px.line(
            x=dates, y=simple_scores, 
            labels={'x': '검사 날짜', 'y': '점수'}, 
            title="간단한 심리검사 점수 변화"
        )
        st.plotly_chart(fig1)

        st.subheader("🧩 MBTI 검사")
        fig2 = px.bar(
            x=dates, y=mbti_scores, 
            labels={'x': '검사 날짜', 'y': '점수'}, 
            title="MBTI 점수 변화"
        )
        st.plotly_chart(fig2)

    with col2:
        st.subheader("😔 우울증 테스트")
        fig3 = px.bar(
            x=dates, y=depression_scores, 
            labels={'x': '검사 날짜', 'y': '점수'}, 
            title="우울증 점수 변화"
        )
        st.plotly_chart(fig3)

        st.subheader("⚠️ 자살 위험성 평가")
        fig4 = px.line(
            x=dates, y=suicide_scores, 
            labels={'x': '검사 날짜', 'y': '점수'}, 
            title="자살 위험성 점수 변화"
        )
        st.plotly_chart(fig4)

# ----- 🤖 머신러닝 심리 상태 예측 -----
elif menu == "심리검사 결과 예측":
    st.title("🤖 심리 상태 예측 (AI)")

    st.write("아래에서 검사 점수를 입력하면 머신러닝 모델이 심리 상태를 예측합니다.")

    # ✅ 최근 검사 결과를 불러오고, 값이 없으면 기본값 설정
    simple_score = st.slider("📋 간단한 심리검사 점수", 0, 30, 
                             st.session_state["simple_test_score"][-1] if len(st.session_state["simple_test_score"]) > 0 else 10)
    mbti_score = st.slider("🧩 MBTI 검사 점수", 0, 20, 
                           st.session_state["mbti_score"][-1] if len(st.session_state["mbti_score"]) > 0 else 10)
    depression_score = st.slider("😔 우울증 테스트 점수", 0, 27, 
                                 st.session_state["depression_score"][-1] if len(st.session_state["depression_score"]) > 0 else 10)
    suicide_score = st.slider("⚠️ 자살 위험성 점수", 0, 10, 
                              st.session_state["suicide_risk_score"][-1] if len(st.session_state["suicide_risk_score"]) > 0 else 5)

    # ✅ 4개의 입력값을 포함한 배열 생성 (모델이 필요로 하는 feature 개수 맞춤)
    user_data = np.array([[simple_score, mbti_score, depression_score, suicide_score]])

    # 예측 실행 버튼
    if st.button("예측하기"):
        # 랜덤 포레스트 예측
        rf_prediction = rf_model.predict(user_data)[0]
        rf_prob = rf_model.predict_proba(user_data)

        # SVM 예측
        svm_prediction = svm_model.predict(user_data)[0]

        st.subheader(f"📊 랜덤 포레스트 예측 결과: {rf_prediction}")
        st.write(f"🌡 확률 분포: {rf_prob}")

        st.subheader(f"📈 SVM 예측 결과: {svm_prediction}")

        # 심리 상태에 따른 조치 권장
        if rf_prediction == "심각한 문제" or svm_prediction == "심각한 문제":
            st.error("🚨 심리 건강에 대한 추가적인 상담이 필요할 수 있습니다. 전문가와 상담해보세요.")
        elif rf_prediction == "경미한 문제" or svm_prediction == "경미한 문제":
            st.warning("⚠️ 경미한 심리적 문제가 있을 수 있습니다. 생활 습관을 점검해보세요.")
        else:
            st.success("✅ 정상적인 심리 상태입니다!")

# ----- 선택된 심리검사 실행 -----
elif menu == "간단한 심리검사":
    import simple_test
    simple_test.run_test()

elif menu == "MBTI 검사":
    import mbti_test
    mbti_test.run_test()

elif menu == "우울증 테스트":
    import depression_test
    depression_test.run_test()

elif menu == "자살 위험성 평가":
    import suicide_risk
    suicide_risk.run_test()
