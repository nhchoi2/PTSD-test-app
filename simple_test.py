import streamlit as st

def run_test():
    # 상단에 이미지 추가
    st.image("A_minimalist_illustration_for_a_psychology_test,_f.png", caption="심리검사", width=600)
    st.subheader("📋 간단한 심리검사")

    # 질문 목록
    questions = [
        "최근 2주 동안 일상 활동에 대한 흥미나 즐거움이 거의 없었다.",
        "최근 2주 동안 기분이 가라앉거나 우울하거나 희망이 없었다.",
        "최근 2주 동안 잠에 어려움이 있었다 (잠을 너무 많이 자거나 잠을 잘 수 없었다).",
        "최근 2주 동안 피로감이나 에너지가 부족함을 느꼈다.",
        "최근 2주 동안 식욕이 감소하거나 과식했다.",
        "최근 2주 동안 자신이 실패자라고 느끼거나 자신 또는 가족을 실망시켰다.",
        "최근 2주 동안 집중하는 데 어려움이 있었다.",
        "최근 2주 동안 다른 사람들이 눈치챌 정도로 느리게 움직이거나 말하거나, 또는 너무 안절부절 못하거나 들떠 있었다.",
        "최근 2주 동안 자신이 죽는 것이 더 낫다고 생각하거나 자해할 생각을 했다.",
        "최근 2주 동안 불안하거나 초조한 느낌이 들었다."
    ]

    # 사용자 응답 수집
    responses = []
    for i, question in enumerate(questions):
        st.write(f"{i+1}. {question}")
        response = st.slider(
            "점수 선택:",
            min_value=0,
            max_value=5,
            value=0,
            step=1,
            format="%d",
            key=f"q{i}"
        )
        responses.append(response)

    # 결과 계산
    if st.button("결과 확인"):
        total_score = sum(responses)
        st.write(f"총점: {total_score}점")

        # 결과 해석
        if total_score <= 4:
            st.success("😊 현재 우울 증상이 거의 없습니다.")
        elif 5 <= total_score <= 9:
            st.info("😐 경미한 우울 증상이 있습니다. 생활 습관 개선을 고려해보세요.")
        elif 10 <= total_score <= 14:
            st.warning("😟 중간 정도의 우울 증상이 있습니다. 전문가와 상담을 고려해보세요.")
        elif 15 <= total_score <= 19:
            st.warning("😢 다소 심한 우울 증상이 있습니다. 전문가의 도움이 필요할 수 있습니다.")
        else:
            st.error("😭 심한 우울 증상이 있습니다. 즉시 전문가의 도움을 받으세요.")
