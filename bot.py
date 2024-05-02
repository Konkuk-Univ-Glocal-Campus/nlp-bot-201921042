import random

# 랜덤 응답 리스트
random_responses = ["흥미로운 이야기네요. 더 자세히 이야기해주세요.",
                    "그렇군요. 계속 이야기해 주세요.",
                    "왜 그런 말을 하시나요?",
                    "요즘 날씨가 정말 이상하죠, 그렇죠?",
                    "다른 주제로 넘어가볼까요?",
                    "어제 경기 보셨나요?"]

print("안녕하세요, 저는 Marvin이라고 합니다. 간단한 챗봇입니다.")
print("'bye'를 입력하여 언제든 대화를 마칠 수 있습니다.")
print("각 대답을 입력한 후 'enter'를 눌러주세요.")
print("오늘은 어떻게 지내세요?")

while True:
    user_input = input("> ")
    if user_input.lower() == "bye":
        break
    else:
        response = random.choice(random_responses)
    print(response)

print("대화해 주셔서 감사합니다. 안녕히 가세요!")