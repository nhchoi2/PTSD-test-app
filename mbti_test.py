import streamlit as st

def run_test():
        # 상단에 이미지 추가
    st.image("mbti.png", caption="심리검사", width=600)
    st.subheader("🧩 MBTI 성격 유형 검사")

    # MBTI 질문 구성
    questions = {
        "E-I": [
            "1. 새로운 사람들과 쉽게 친해지는 편이다.",
            "2. 혼자 있는 것보다 사람들과 함께 있는 것이 더 좋다.",
            "3. 대화에서 내가 주도하는 경우가 많다.",
            "4. 혼자서 조용한 시간을 보내는 것보다 사람들과 어울리는 것이 좋다.",
            "5. 새로운 모임에 가면 먼저 말을 거는 편이다."
        ],
        "S-N": [
            "6. 나는 현재 상황을 중요하게 여기고 세부 사항에 집중하는 편이다.",
            "7. 나는 직관적으로 큰 그림을 보는 것을 선호한다.",
            "8. 나는 감각적인 정보(사실, 데이터)를 신뢰하는 편이다.",
            "9. 창의적이고 상상력을 발휘하는 일이 좋다.",
            "10. 나는 실용적인 것이 중요하다고 생각한다."
        ],
        "T-F": [
            "11. 나는 의사 결정을 내릴 때 논리적이고 객관적인 근거를 중요하게 여긴다.",
            "12. 나는 다른 사람들의 감정을 고려하며 결정을 내리는 편이다.",
            "13. 나는 감정보다는 이성을 더 중요하게 생각한다.",
            "14. 나는 다른 사람의 감정을 쉽게 공감하는 편이다.",
            "15. 나는 사실과 데이터에 기반하여 판단하는 것이 중요하다고 생각한다."
        ],
        "J-P": [
            "16. 나는 계획적으로 일을 처리하는 것을 좋아한다.",
            "17. 나는 즉흥적으로 유연하게 대응하는 것을 좋아한다.",
            "18. 나는 체계적으로 정리된 계획을 세우는 것을 선호한다.",
            "19. 나는 변화에 잘 적응하는 편이다.",
            "20. 나는 미리 계획을 세우는 것이 중요하다고 생각한다."
        ]
    }

    # 점수 저장
    scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}

    # 각 질문에 대한 슬라이드바 생성
    for category, question_list in questions.items():
        st.subheader(f"{category} 문항")
        for question in question_list:
            score = st.slider(question, 0, 5, 2, 1, key=question)
            if category == "E-I":
                scores["E"] += score
                scores["I"] += (5 - score)
            elif category == "S-N":
                scores["S"] += score
                scores["N"] += (5 - score)
            elif category == "T-F":
                scores["T"] += score
                scores["F"] += (5 - score)
            elif category == "J-P":
                scores["J"] += score
                scores["P"] += (5 - score)

    # 결과 확인 버튼
    if st.button("결과 확인"):
        mbti_type = (
            "E" if scores["E"] > scores["I"] else "I") + \
            ("S" if scores["S"] > scores["N"] else "N") + \
            ("T" if scores["T"] > scores["F"] else "F") + \
            ("J" if scores["J"] > scores["P"] else "P")

        st.subheader(f"당신의 MBTI 유형: **{mbti_type}**")
        st.write("### MBTI 성격 유형 설명:")
        if mbti_type == "ISTJ":
            st.write("📌 **ISTJ (세상의 소금형)** - 신뢰할 수 있으며 조직적입니다.")
        elif mbti_type == "ISFJ":
            st.write("📌 **ISFJ (임무 수행형)** - 책임감이 강하고 타인을 배려하는 성격입니다.")
        elif mbti_type == "INFJ":
            st.write("📌 **INFJ (예언자형)** - 깊은 통찰력을 가진 이상주의자입니다.")
        elif mbti_type == "INTJ":
            st.write("📌 **INTJ (전략가형)** - 논리적이며 계획적인 성향을 가집니다.")
        elif mbti_type == "ISTP":
            st.write("📌 **ISTP (백과사전형)** - 분석적이며 현실적인 문제 해결자입니다.")
        elif mbti_type == "ISFP":
            st.write("📌 **ISFP (예술가형)** - 감성적이며 예술적인 감각이 뛰어납니다.")
        elif mbti_type == "INFP":
            st.write("📌 **INFP (중재자형)** - 창의적이고 이상적인 가치를 중시합니다.")
        elif mbti_type == "INTP":
            st.write("📌 **INTP (논리적 사색가형)** - 분석적이며 지적인 탐구를 즐깁니다.")
        elif mbti_type == "ESTP":
            st.write("📌 **ESTP (모험가형)** - 활동적이고 즉흥적인 성향을 가집니다.")
        elif mbti_type == "ESFP":
            st.write("📌 **ESFP (자유로운 영혼형)** - 친절하고 사교적인 성격입니다.")
        elif mbti_type == "ENFP":
            st.write("📌 **ENFP (활동가형)** - 열정적이며 창의적인 성향이 강합니다.")
        elif mbti_type == "ENTP":
            st.write("📌 **ENTP (논쟁가형)** - 도전적이며 창의적인 사고를 가집니다.")
        elif mbti_type == "ESTJ":
            st.write("📌 **ESTJ (엄격한 관리자형)** - 현실적이며 체계적인 성향입니다.")
        elif mbti_type == "ESFJ":
            st.write("📌 **ESFJ (사교적인 외교관형)** - 친절하고 타인과 협력하는 것을 좋아합니다.")
        elif mbti_type == "ENFJ":
            st.write("📌 **ENFJ (주도적인 지도자형)** - 따뜻하고 영향력이 강한 리더 유형입니다.")
        elif mbti_type == "ENTJ":
            st.write("📌 **ENTJ (대담한 통솔자형)** - 강한 카리스마를 지닌 지도자형입니다.")

        st.success("🔎 더 많은 정보를 원하면 MBTI 관련 리소스를 참고하세요!")
