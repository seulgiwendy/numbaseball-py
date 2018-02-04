import balls, umpire

def main():

    user_ball = []
    b = balls.Pitcher()
    u = umpire.Umpire()

    print("숫자 게임에 오신 것을 환영합니다.")

    for i in range(0, 3):
        print(i + 1, "번째 숫자를 입력해 주세요.")
        user_ball.append(input())

    print(user_ball)

main()