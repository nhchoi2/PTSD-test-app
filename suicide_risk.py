import streamlit as st

def run_test():
    # 상단에 이미지 추가
    st.image("sui.png", caption="심리검사", width=600)
    # 상단 타이틀
    st.subheader("⚠️ 자살 위험성 평가")
    st.info('질문이 끝날 때 까지 있다 또는 없다의 버튼을 클릭해 주세요요')
    # 초기 질문 (필수 응답)
    st.write("### 1. 당신 자신을 정말 해치겠다는 생각을 했던 적이 있습니까?")
    suicide_thought = st.radio("응답을 선택하세요:", ["없다", "있다"], index=0)

    # 추가 문항 (초기 질문에서 '있다' 선택한 경우만 활성화)
    if suicide_thought == "있다":
        st.write("### 2. 다음 질문에 응답해주세요.")

        past_attempt = st.radio("과거에 당신을 위험에 빠뜨리는 행동을 한 적이 있습니까?", ["없다", "있다"], index=0)
        current_thought = st.radio("지금도 자신을 해칠 방법을 생각하고 있습니까?", ["없다", "있다"], index=0)

        if current_thought == "있다":
            method = st.text_input("어떤 방법을 생각하고 있습니까? (선택 사항)")

        action_intent = st.radio(
            "앞으로 한 달 내에 당신 자신을 해치거나 삶을 끝내겠다는 생각을 행동으로 옮길 가능성이 있습니까?",
            ["전혀 아니다", "약간 그렇다", "매우 그렇다"], index=0
        )

        protective_factor = st.radio(
            "당신 자신을 해치려는 행동을 멈추게 하거나 하지 못하게 막는 것이 있습니까?",
            ["있다", "없다"], index=0
        )

        if protective_factor == "있다":
            protective_reason = st.text_input("무엇이 당신을 막고 있습니까? (선택 사항)")

    # 결과 계산
    if st.button("결과 확인"):
        if suicide_thought == "없다":
            st.success("✅ **자살 위험성이 거의 없음**\n\n'당신 자신을 해칠 생각을 한 적이 있습니까?' 문항에 '없다'라고 응답하셨습니다.")
        else:
            if (past_attempt == "있다" or current_thought == "있다") and (action_intent == "전혀 아니다" and protective_factor == "있다"):
                st.info("🔹 **자살 위험성 낮음**\n\n과거 자살 시도가 있었거나 자살 계획에 대한 생각을 했지만, 현재 우발적인 자살 시도 가능성은 낮습니다.")
            elif action_intent in ["약간 그렇다", "매우 그렇다"] or protective_factor == "없다":
                st.error("🚨 **자살 위험성 높음**\n\n자살 가능성이 있거나 보호 요인이 없습니다. 즉시 전문가의 도움을 받아보세요.")
