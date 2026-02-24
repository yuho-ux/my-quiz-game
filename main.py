
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
class QuizGame:
    def __init__(self, quizzes):
        self.quizzes = quizzes  # 퀴즈 객체들이 담긴 리스트
        self.top_score = 0      # 최고 점수 변수

    def show_menu(self):
        print("\n=== 💡 스마트 퀴즈 관리자 ===")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록 보기")
        print("4. 최고 점수 확인")
        print("0. 종료")

    def solve_quiz(self):
        if not self.quizzes:
            print("\n[알림] 등록된 퀴즈가 없습니다.")
            return
        
        score = 0
        print(f"\n--- 퀴즈 시작! (총 {len(self.quizzes)}문제) ---")
        for quiz in self.quizzes:
            quiz.display_quiz()
            ans = input("정답 번호: ")
            if quiz.is_correct(ans):
                print("⭕ 정답입니다!")
                score += 1
            else:
                print(f"❌ 오답입니다! 정답은 {quiz.answer}번입니다.")
        
        print(f"\n게임 종료! 점수: {score}/{len(self.quizzes)}")
        # 최고 점수 갱신 로직
        if score > self.top_score:
            self.top_score = score
            print("✨ 최고 점수를 경신했습니다!")

    def add_quiz(self):
        print("\n--- 새로운 퀴즈 추가 ---")
        question = input("문제 내용: ")
        choices = [input(f"보기 {i}번: ") for i in range(1, 5)]
        while True:
            answer = input("정답 번호 (1-4): ")
            if answer in ["1", "2", "3", "4"]:
                break
            print("[오류] 1~4 사이의 숫자만 입력하세요.")
        
        self.quizzes.append(Quiz(question, choices, int(answer)))
        print("[알림] 퀴즈가 추가되었습니다!")

    def list_quizzes(self):
        if not self.quizzes:
            print("\n[알림] 등록된 퀴즈가 없습니다.")
            return
        print("\n--- 📜 현재 등록된 퀴즈 목록 ---")
        for i, quiz in enumerate(self.quizzes, 1):
            print(f"{i}. {quiz.question}")
       
def main():        
    # 1. 초기 퀴즈 데이터 생성
    quizzes = [
        Quiz("도커에서 실행 중인 컨테이너 목록을 확인하는 명령어는?", ["docker run", "docker ps", "docker images", "docker build"], 2),
        Quiz("Git에서 변경 사항을 스냅샷으로 기록하는 명령어는?", ["git add", "git push", "git commit", "git pull"], 3),
        Quiz("Dockerfile에서 베이스 이미지를 지정하는 명령어는?", ["FROM", "COPY", "RUN", "CMD"], 1),
        Quiz("Python에서 무한 반복을 만들기 위해 사용하는 문구는?", ["if True", "while True", "for True", "repeat"], 2),
        Quiz("GitHub에 내 코드를 전송하는 명령어는?", ["git commit", "git push", "git pull", "git init"], 2)
    ]

    # 2. 매니저(QuizGame 객체) 고용!
    # 이제부터 모든 복잡한 일은 game이 알아서 할 겁니다.
    game = QuizGame(quizzes)

    while True:
        # 3. 매니저에게 메뉴판 보여달라고 하기
        game.show_menu()

        choice = input("원하는 메뉴 번호를 입력하세요: ")
        
        if choice == "1":
            # 매니저야, 퀴즈 좀 풀어줘!
            game.solve_quiz()
            
        elif choice == "2":
            # 매니저야, 퀴즈 좀 추가해줘!
            game.add_quiz()
            
        elif choice == "3":
            # 매니저야, 목록 좀 보여줘!
            game.list_quizzes()
            
        elif choice == "4":
            # 매니저에게 저장된 최고 점수 물어보기
            print(f"\n현재 최고 점수는 {game.top_score}점입니다.")
            
        elif choice == "0":
            print("\n게임을 종료합니다. 다음에 또 봐요!")
            break 
            
        else:
            print("\n[경고] 잘못된 입력입니다. 0~4 사이의 숫자를 입력해주세요.")

if __name__ == "__main__":
    main()
