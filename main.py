import streamlit as st
import streamlit.components.v1 as components
import simple_test, mbti_test, depression_test, suicide_risk, predict
import plotly.express as px

# ----- 기본 설정 -----
st.set_page_config(page_title="심리검사 대시보드", layout="wide")

# ----- CSS 스타일 적용 -----
st.markdown("""
    <style>
    .main-title {
        font-size: 38px;
        font-weight: bold;
        text-align: center;
        color: #333333;
        margin-bottom: 20px;
    }
    .sub-title {
        font-size: 20px;
        text-align: center;
        color: #666666;
        margin-bottom: 30px;
    }
    .card {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        text-align: center;
        font-size: 18px;
        font-weight: bold;
    }
    .dark-mode {
        background-color: #1e1e1e;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# ----- 다크 모드 지원 -----
theme = st.sidebar.radio("🌙 테마 선택", ["라이트 모드", "다크 모드"])
if theme == "다크 모드":
    st.markdown('<style>body { background-color: #1e1e1e; color: white; }</style>', unsafe_allow_html=True)

# ----- 사이드바 (네비게이션) -----
st.sidebar.image("A_pastel-toned,_dreamy,_and_clean_abstract_backgro.png", use_container_width=True)

# 사이드바 버튼 (새 창으로 열기)
st.sidebar.markdown('<div style="text-align: center; margin-top: 20px;">', unsafe_allow_html=True)
components.html(
    """
    <a href="https://boohoday.com/" target="_blank" style="text-decoration: none;">
        <button style="
            background-color: #333333; 
            color: white; 
            border: none; 
            padding: 10px 15px; 
            font-size: 16px; 
            border-radius: 5px; 
            cursor: pointer;">
            🚀 Software Developer
        </button>
    </a>
    """,
    height=70,
)
st.sidebar.markdown('</div>', unsafe_allow_html=True)

# ----- 사이드바 라디오 버튼 (심리검사 선택) -----
st.sidebar.title("🧠 심리검사 선택")
menu = st.sidebar.radio(
    "검사를 선택하세요:",
    ["대시보드", "간단한 심리검사", "MBTI 검사", "우울증 테스트", "자살 위험성 평가", "심리검사 결과 예측"]
)

# ----- 대시보드 (메인 페이지) -----
if menu == "대시보드":
    st.markdown('<h1 class="main-title">📊 심리검사 대시보드</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">당신의 심리 상태를 한눈에 분석하고 건강한 삶을 돕습니다.</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="card">📋 간단한 심리검사</div>', unsafe_allow_html=True)
        st.write("최근 검사 점수: **10점**")
        fig1 = px.line(x=[1, 2, 3, 4, 5], y=[5, 7, 9, 10, 10], labels={'x': '날짜', 'y': '점수'}, title="간단한 심리검사 추이")
        st.plotly_chart(fig1)

        st.markdown('<div class="card">🧩 MBTI 검사</div>', unsafe_allow_html=True)
        st.write("최근 검사 결과: **INTP**")

    with col2:
        st.markdown('<div class="card">😔 우울증 테스트</div>', unsafe_allow_html=True)
        st.write("최근 검사 점수: **12점**")
        fig2 = px.bar(x=["1월", "2월", "3월", "4월", "5월"], y=[5, 8, 10, 12, 12], labels={'x': '월', 'y': '점수'}, title="우울증 점수 변화")
        st.plotly_chart(fig2)

        st.markdown('<div class="card">⚠️ 자살 위험성 평가</div>', unsafe_allow_html=True)
        st.write("최근 검사 점수: **3점**")

# ----- 선택된 심리검사 실행 -----
elif menu == "간단한 심리검사":
    simple_test.run_test()
elif menu == "MBTI 검사":
    mbti_test.run_test()
elif menu == "우울증 테스트":
    depression_test.run_test()
elif menu == "자살 위험성 평가":
    suicide_risk.run_test()
elif menu == "심리검사 결과 예측":
    predict.run_prediction()

# ----- 방문자 카운트 -----
if "visitor_count" not in st.session_state:
    st.session_state["visitor_count"] = 0
st.session_state["visitor_count"] += 1
st.markdown(f'<p class="visit-count">👥 오늘 방문자 수: {st.session_state["visitor_count"]}</p>', unsafe_allow_html=True)
