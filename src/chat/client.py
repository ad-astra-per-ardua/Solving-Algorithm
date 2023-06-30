import requests

while True:
    print("1: 채팅 보내기, 2: 채팅 가져오기, 3: 채팅 삭제하기")
    menu = int(input("선택: "))
    if menu == 1:
        user = input("사용자 이름: ")
        message = input("보낼 메시지: ")
        response = requests.post(
            "http://localhost:8000/chat",
            json={
                "user": user,
                "message": message,
            },
        )
        print(response.json())
    elif menu == 2:
        response = requests.get("http://localhost:8000/chat")
        print(response.json())
    elif menu == 3:
        response = requests.delete("http://localhost:8000/chat")
        print(response.json())
