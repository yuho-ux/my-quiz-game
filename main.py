def main():
    class Quiz:
        def __init__(self, question, choices, answer):
            """
            question: 문제 내용 (문자열)
            choices: 4개의 보기 (리스트)
            answer: 정답 번호 (1~4 사이 정수)
            """
            self.question = question
            self.choices = choices
            self.answer = answer

        def display_quiz(self):
            """문제를 화면에 출력합니다."""
            print(f"\nQ. {self.question}")
            for i, choice in enumerate(self.choices, 1):
                print(f"{i}) {choice}")

        def is_correct(self, user_answer):
            """사용자가 입력한 번호가 정답인지 확인합니다."""
            return str(self.answer) == user_answer
        
    quizzes = [
        Quiz("도커에서 실행 중인 컨테이너 목록을 확인하는 명령어는?", ["docker run", "docker ps", "docker images", "docker build"], 2),
        Quiz("Git에서 변경 사항을 스냅샷으로 기록하는 명령어는?", ["git add", "git push", "git commit", "git pull"], 3),
        Quiz("Dockerfile에서 베이스 이미지를 지정하는 명령어는?", ["FROM", "COPY", "RUN", "CMD"], 1),
        Quiz("Python에서 무한 반복을 만들기 위해 사용하는 문구는?", ["if True", "while True", "for True", "repeat"], 2),
        Quiz("GitHub에 내 코드를 전송하는 명령어는?", ["git commit", "git push", "git pull", "git init"], 2)
    ]

    while True:
        print("\n=== 유호의 퀴즈 게임 ===")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록 보기")
        print("4. 최고 점수 확인")
        print("0. 종료")

        choice = input("원하는 메뉴 번호를 입력하세요: ")
        
        if choice == "1":
            if not quizzes:
                print("\n[알림] 등록된 퀴즈가 없습니다.")
                continue
            
            score = 0
            print(f"\n--- 퀴즈를 시작합니다! (총 {len(quizzes)}문제) ---")
            
            for quiz in quizzes:
                quiz.display_quiz() # 문제 출력
                user_input = input("정답 번호를 입력하세요: ")
                
                if quiz.is_correct(user_input):
                    print("⭕ 정답입니다!")
                    score += 1
                else:
                    print(f"❌ 틀렸습니다! 정답은 {quiz.answer}번입니다.")
            
            print(f"\n--- 게임 종료! 당신의 점수는 {score}/{len(quizzes)}입니다. ---")
            
        elif choice == "2":
            print("\n[알림] 퀴즈 추가 기능을 준비 중입니다.")
        elif choice == "3":
            print("\n[알림] 퀴즈 목록 보기 기능을 준비 중입니다.")
        elif choice == "4":
            print("\n[알림] 최고 점수 확인 기능을 준비 중입니다.")
        elif choice == "0":
            print("\n게임을 종료합니다. 다음에 또 봐요!")
            break  # while 반복문을 빠져나와 프로그램을 종료합니다.
        else:
            print("\n[경고] 잘못된 입력입니다. 0~4 사이의 숫자를 입력해주세요.")

if __name__ == "__main__":
    main()
