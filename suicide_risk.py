import streamlit as st

def run_test():
    """ 자살 위험성 평가 실행 함수 (P4 Screener 기반) """
    st.subheader("⚠️ 자살 위험성 평가")

    # 기본 질문: 자살 생각 여부
    st.write("### 1. 당신 자신을 해치겠다는 생각을 한 적이 있습니까?")
    suicide_thought = st.radio(
        "응답을 선택하세요:", ["없다", "있다"], index=0
    )

    responses = []

    # 자살 생각이 '있다'를 선택한 경우만 추가 문항 표시
    if suicide_thought == "있다":
        st.write("### 2. 다음 질문에 응답해주세요.")

        past_attempt = st.radio("2. 과거에 당신을 위험에 빠뜨리는 행동을 한 적이 있습니까?", ["없다", "있다"], index=0)
        current_thought = st.radio("3. 지금도 자신을 해칠 방법을 생각하고 있습니까?", ["없다", "있다"], index=0)

        if current_thought == "있다":
            method = st.text_input("어떤 방법을 생각하고 있습니까? (선택 사항)")

        action_intent = st.radio(
            "4. 앞으로 한 달 내에 당신 자신을 해치거나 삶을 끝내겠다는 생각을 행동으로 옮길 가능성이 있습니까?",
            ["전혀 아니다", "약간 그렇다", "매우 그렇다"], index=0
        )

        protective_factor = st.radio(
            "5. 당신 자신을 해치려는 행동을 멈추게 하거나 하지 못하게 막는 것이 있습니까?",
            ["있다", "없다"], index=0
        )

        if protective_factor == "있다":
            protective_reason = st.text_input("무엇이 당신을 막고 있습니까? (선택 사항)")

        # 점수 계산
        responses.append(1 if past_attempt == "있다" else 0)
        responses.append(1 if current_thought == "있다" else 0)
        responses.append(1 if action_intent in ["약간 그렇다", "매우 그렇다"] else 0)
        responses.append(1 if protective_factor == "없다" else 0)

    # 검사 결과 확인 버튼
    if st.button("결과 확인"):
        total_score = sum(responses)

        # 기본 질문이 "없다"면 자동으로 점수를 0으로 설정
        if suicide_thought == "없다":
            total_score = 0

        st.write(f"### 🔹 총점: {total_score}점")

        # 결과 해석
        if total_score == 0:
            st.success("✅ 자살 위험성이 거의 없음")
        elif total_score <= 2:
            st.info("🔹 자살 위험성 낮음 → 전문가 상담을 고려해보세요.")
        else:
            st.error("🚨 자살 위험성이 높음 → 즉시 전문가의 도움을 받으세요!")

        # 💡 검사 점수를 세션 상태에 저장 → 대시보드에서 자동 반영
        st.session_state["suicide_risk_score"] = total_score
