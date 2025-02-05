import streamlit as st
import datetime

def run_test():
    st.subheader("😔 우울증 테스트")

    questions = [
        "1. 일 또는 여가 활동에서 흥미나 즐거움을 느끼지 못함",
        "2. 기분이 가라앉거나 우울하거나, 희망이 없음",
        "3. 잠드는 것이 어렵거나 너무 많이 잠",
        "4. 피로감을 느끼거나 에너지가 거의 없음",
        "5. 입맛이 없거나 과식을 함"
    ]

    responses = [st.slider(q, 0, 3, 0, 1) for q in questions]

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
        if "depression_score" in st.session_state:
            st.session_state["depression_score"].append(total_score)
        else:
            st.session_state["depression_score"] = [total_score]
