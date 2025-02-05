import streamlit as st
import datetime

def run_test():
    st.subheader("📋 간단한 심리검사")

    questions = [
        "1. 최근 2주 동안 일상 활동에 대한 흥미나 즐거움을 느끼지 못함",
        "2. 최근 2주 동안 기분이 가라앉거나, 우울하거나, 희망이 없음",
        "3. 최근 2주 동안 잠들기 어렵거나 계속 잠을 자는 것이 어려움, 또는 잠을 너무 많이 잠",
        "4. 최근 2주 동안 피로감을 느끼거나 에너지가 부족함",
        "5. 최근 2주 동안 식욕이 감소하거나 과식을 함"
    ]

    responses = [st.slider(q, 0, 5, 0, 1) for q in questions]

    if st.button("결과 확인"):
        total_score = sum(responses)
        st.write(f"### 🔹 총점: {total_score}점")

        # 검사 날짜 저장
        today = datetime.date.today().strftime("%Y-%m-%d")
        if "test_dates" in st.session_state:
            st.session_state["test_dates"].append(today)
        else:
            st.session_state["test_dates"] = [today]

        # 점수 저장
        if "simple_test_score" in st.session_state:
            st.session_state["simple_test_score"].append(total_score)
        else:
            st.session_state["simple_test_score"] = [total_score]
