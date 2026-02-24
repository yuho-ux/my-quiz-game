import json # 파일 맨 윗줄에 추가하세요!
import random # 맨 윗줄에 추가!
from datetime import datetime # 추가!

class Quiz:
    def __init__(self, question, choices, answer, hint="힌트가 등록되어 있지 않습니다."):
        """
        question: 문제 내용 (문자열)
        choices: 4개의 보기 (리스트)
        answer: 정답 번호 (1~4 사이 정수)
        self.hint = hint # 힌트 속성 추가
        """
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint # 힌트 속성 추가

    def display_quiz(self):
        """문제를 화면에 출력합니다."""
        print(f"\nQ. {self.question}")
        for i, choice in enumerate(self.choices, 1):
            print(f"{i}) {choice}")
        print("💡 힌트를 보려면 'h'를 입력하세요. (점수 0.5점 차감)")

    def is_correct(self, user_answer):
        """사용자가 입력한 번호가 정답인지 확인합니다."""
        return str(self.answer) == user_answer

class QuizGame:
    def __init__(self, quizzes):
        self.quizzes = quizzes  # 퀴즈 객체들이 담긴 리스트
        self.top_score = 0      # 최고 점수 변수
        self.history = []  # 게임 기록을 담을 리스트 추가


    def show_menu(self):
        print("\n=== 💡 스마트 퀴즈 관리자 ===")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록 보기")
        print("4. 최고 점수 확인")
        print("5. 퀴즈 삭제")
        print("6. 전체 게임 기록 보기") # 추가
        print("0. 종료")

    def solve_quiz(self):
        if not self.quizzes:
            print("\n[알림] 등록된 퀴즈가 없습니다.")
            return
        
        # 1. 랜덤 섞기 (보너스 과제)
        temp_quizzes = list(self.quizzes)
        random.shuffle(temp_quizzes)
        
        # 2. 문제 수 선택 (보너스 과제)
        print(f"\n현재 총 {len(temp_quizzes)}개의 문제가 있습니다.")
        try:
            limit_input = input(f"몇 문제를 풀고 싶나요? (1~{len(temp_quizzes)} / 전체는 Enter): ")
            if limit_input == "":
                limit = len(temp_quizzes)
            else:
                limit = int(limit_input)
                limit = max(1, min(limit, len(temp_quizzes)))
        except ValueError:
            limit = len(temp_quizzes)
            
        score = 0.0 # 힌트 차감을 위해 실수형(float)으로 변경
        print(f"\n--- 퀴즈 시작! ({limit}문제를 출제합니다) ---")
        
        for i in range(limit):
            quiz = temp_quizzes[i]
            quiz.display_quiz()
            
            user_input = input("정답 번호 (힌트는 'h'): ").lower()
            
            # 3. 힌트 기능 (보너스 과제)
            if user_input == 'h':
                print(f"🔍 [힌트] {quiz.hint}")
                score -= 0.5
                user_input = input("정답 번호: ")
                
            if quiz.is_correct(user_input):
                print("⭕ 정답입니다!")
                score += 1
            else:
                print(f"❌ 오답입니다! 정답은 {quiz.answer}번입니다.")
        
        print(f"\n--- 게임 종료! 최종 점수: {score}/{limit} ---")
        
        if score > self.top_score:
            self.top_score = score
            print("✨ 최고 점수를 경신했습니다!")
            self.save_data()

        # 히스토리 기록 생성
        play_info = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_questions": limit,
            "final_score": score
        }
        self.history.append(play_info) # 기록 추가
        self.save_data()

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
        self.save_data()  # <--- 이 줄을 추가해서 파일에 즉시 저장

    def delete_quiz(self):
        self.list_quizzes()
        if not self.quizzes:
            return
            
        try:
            idx = int(input("\n삭제할 퀴즈 번호를 입력하세요 (취소는 0): "))
            if idx == 0:
                return
            if 1 <= idx <= len(self.quizzes):
                removed = self.quizzes.pop(idx - 1)
                print(f"[알림] '{removed.question}' 퀴즈를 삭제했습니다.")
                self.save_data() # 삭제 후 즉시 파일 반영
            else:
                print("[오류] 올바른 번호를 입력하세요.")
        except ValueError:
            print("[오류] 숫자만 입력 가능합니다.")

    def list_quizzes(self):
        if not self.quizzes:
            print("\n[알림] 등록된 퀴즈가 없습니다.")
            return
        print("\n--- 📜 현재 등록된 퀴즈 목록 ---")
        for i, quiz in enumerate(self.quizzes, 1):
            print(f"{i}. {quiz.question}")

    def save_data(self):
        """퀴즈 목록과 최고 점수를 JSON 파일로 저장합니다."""
        data = {
            "top_score": self.top_score,
            "history": self.history, # 히스토리 추가
            "quizzes": []
        }
        for q in self.quizzes:
            data["quizzes"].append({
                "question": q.question,
                "choices": q.choices,
                "answer": q.answer,
                "hint": q.hint # 힌트 저장 추가
            })
        
        with open("quiz_data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("[시스템] 데이터가 안전하게 저장되었습니다.")

    def load_data(self):
        """JSON 파일에서 데이터를 불러옵니다. 파일이 없으면 에러 처리를 합니다."""
        try:
            with open("quiz_data.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                self.top_score = data.get("top_score", 0)
                # JSON 텍스트 데이터를 다시 Quiz 객체 리스트로 변환
                self.history = data.get("history", []) # 히스토리 불러오기
                self.quizzes = []
                for item in data["quizzes"]:
                    self.quizzes.append(Quiz(item["question"], item["choices"], item["answer"], item.get("hint", "힌트가 없습니다.")))
                print("[시스템] 데이터를 성공적으로 불러왔습니다.")
        except FileNotFoundError:
            print("[시스템] 저장된 파일이 없어 기본 데이터를 사용합니다.")

    def show_history(self):
        print("\n--- 📊 최근 게임 기록 ---")
        if not self.history:
            print("아직 게임 기록이 없습니다.")
            return
        
        for record in self.history[-5:]: # 최근 5경기만 출력
            print(f"[{record['date']}] 풀은 문제: {record['total_questions']}개, 점수: {record['final_score']}점")
       
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
    game.load_data()  # 저장된 파일이 있으면 불러오고, 없으면 기본 데이터 사용

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
        
        elif choice == "5":
            game.delete_quiz()

        elif choice == "6":
            game.show_history()
            
        elif choice == "0":
            print("\n게임을 종료합니다. 다음에 또 봐요!")
            break 
            
        else:
            print("\n[경고] 잘못된 입력입니다. 0~4 사이의 숫자를 입력해주세요.")

if __name__ == "__main__":
    main()
