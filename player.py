import balls, umpire

def main():

    user_ball = []
    computer_ball = []
    attempt_count = 1

    b = balls.Pitcher()
    u = umpire.Umpire()

    ball_count = 0
    strike_count = 0

    computer_ball = b.throw()

    print("숫자 게임에 오신 것을 환영합니다.")

    while strike_count != 3:
        user_ball = []
        print(attempt_count, "번째 시도입니다.")

        for i in range(0, 3):
            print(i + 1, "번째 숫자를 입력해 주세요.")
            input_number = input()
            while input_number == "":
                print("잘못된 입력입니다. 다시 한 번 입력하여 주십시오.", i + 1, "번째 숫자를 입력하고 있습니다.")
                input_number = input()

            user_ball.append(int(input_number))

        ball_count = u.ball_count(user_ball, computer_ball)
        strike_count = u.strike_count(user_ball, computer_ball)

        print(ball_count, "B ", strike_count, "S!")
        attempt_count += 1

    print("You Win!")


main()

