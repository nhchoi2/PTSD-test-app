import streamlit as st
import streamlit.components.v1 as components
import simple_test, mbti_test, depression_test, suicide_risk, predict
import plotly.express as px

# ----- 기본 설정 -----
st.set_page_config(page_title="심리검사 대시보드", layout="wide")

# ----- 세션 상태 초기화 (최초 실행 시) -----
if "simple_test_score" not in st.session_state:
    st.session_state["simple_test_score"] = 0
    st.session_state["mbti_score"] = 0
    st.session_state["depression_score"] = 0
    st.session_state["suicide_risk_score"] = 0

# ----- 사이드바 (네비게이션) -----
st.sidebar.image("A_pastel-toned,_dreamy,_and_clean_abstract_backgro.png", use_column_width=True)
st.sidebar.title("🧠 심리검사 선택")
menu = st.sidebar.radio(
    "검사를 선택하세요:",
    ["대시보드", "간단한 심리검사", "MBTI 검사", "우울증 테스트", "자살 위험성 평가", "심리검사 결과 예측"]
)

# ----- 📊 대시보드 (실제 검사 결과 반영) -----
if menu == "대시보드":
    st.markdown('<h1 style="text-align: center;">📊 심리검사 대시보드</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📋 간단한 심리검사")
        st.write(f"최근 검사 점수: **{st.session_state['simple_test_score']}점**")
        fig1 = px.line(x=["1월", "2월", "3월", "4월", "최근 검사"], 
                       y=[5, 7, 9, 10, st.session_state['simple_test_score']], 
                       labels={'x': '날짜', 'y': '점수'}, title="간단한 심리검사 점수 변화")
        st.plotly_chart(fig1)

        st.subheader("🧩 MBTI 검사")
        st.write(f"최근 검사 점수: **{st.session_state['mbti_score']}점**")

    with col2:
        st.subheader("😔 우울증 테스트")
        st.write(f"최근 검사 점수: **{st.session_state['depression_score']}점**")
        fig2 = px.bar(x=["1월", "2월", "3월", "4월", "최근 검사"], 
                      y=[5, 8, 10, 12, st.session_state['depression_score']], 
                      labels={'x': '월', 'y': '점수'}, title="우울증 점수 변화")
        st.plotly_chart(fig2)

        st.subheader("⚠️ 자살 위험성 평가")
        st.write(f"최근 검사 점수: **{st.session_state['suicide_risk_score']}점**")

# ----- 선택된 심리검사 실행 -----
elif menu == "간단한 심리검사":
    score = simple_test.run_test()
    if score is not None:
        st.session_state["simple_test_score"] = score

elif menu == "MBTI 검사":
    score = mbti_test.run_test()
    if score is not None:
        st.session_state["mbti_score"] = score

elif menu == "우울증 테스트":
    score = depression_test.run_test()
    if score is not None:
        st.session_state["depression_score"] = score

elif menu == "자살 위험성 평가":
    score = suicide_risk.run_test()
    if score is not None:
        st.session_state["suicide_risk_score"] = score

elif menu == "심리검사 결과 예측":
    predict.run_prediction()
