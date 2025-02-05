import streamlit as st
import streamlit.components.v1 as components
import simple_test, mbti_test, depression_test, suicide_risk

# ----- 기본 설정 -----
st.set_page_config(page_title="심리검사 앱", layout="wide")

# ----- 메인 화면 (기본 정보) -----
st.markdown('<h1 class="main-title">💡 심리검사 앱</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">당신의 심리 상태를 분석하고 건강한 삶을 돕습니다.</p>', unsafe_allow_html=True)

# ----- CSS 스타일 적용 -----
st.markdown("""
    <style>
    .main-title {
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        color: #333333;
    }
    .sub-title {
        font-size: 20px;
        text-align: center;
        color: #666666;
    }
    .visit-count {
        font-size: 18px;
        font-weight: bold;
        text-align: center;
        margin-top: 30px;
    }
    .sidebar-button {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ----- 사이드바 (네비게이션) -----
# 사이드바 상단 이미지
st.sidebar.image("A_pastel-toned,_dreamy,_and_clean_abstract_backgro.png", use_container_width=True)

# 사이드바 라디오 버튼 (심리검사 선택)
st.sidebar.title("🧠 심리검사 선택")
menu = st.sidebar.radio(
    "검사를 선택하세요:",
    ["간단한 심리검사", "MBTI 검사", "우울증 테스트", "자살 위험성 평가"])

# ----- 선택된 페이지 실행 -----
if menu == "간단한 심리검사":
    simple_test.run_test()
elif menu == "MBTI 검사":
    mbti_test.run_test()
elif menu == "우울증 테스트":
    depression_test.run_test()
elif menu == "자살 위험성 평가":
    suicide_risk.run_test()

# ----- 방문자 카운트 -----
if "visitor_count" not in st.session_state:
    st.session_state["visitor_count"] = 0

st.session_state["visitor_count"] += 1
st.markdown(f'<p class="visit-count">👥 오늘 방문자 수: {st.session_state["visitor_count"]}</p>', unsafe_allow_html=True)


