def main():
    while True:
        print("\n=== 유호의 퀴즈 게임 ===")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록 보기")
        print("4. 최고 점수 확인")
        print("0. 종료")

        choice = input("원하는 메뉴 번호를 입력하세요: ")
        
        if choice == "1":
            print("\n[알림] 퀴즈 풀기 기능을 준비 중입니다.")
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
