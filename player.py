import balls, umpire

def main():

    user_ball = []
    computer_ball = []

    b = balls.Pitcher()
    u = umpire.Umpire()

    ball_count = 0
    strike_count = 0

    computer_ball = b.throw()

    print("숫자 게임에 오신 것을 환영합니다.")

    while strike_count != 3:
        user_ball = []

        for i in range(0, 3):
            print(i + 1, "번째 숫자를 입력해 주세요.")
            user_ball.append(int(input()))

        ball_count = u.ball_count(user_ball, computer_ball)
        strike_count = u.strike_count(user_ball, computer_ball)

        print(ball_count, "B ", strike_count, "S!")

    print("You Win!")


main()

