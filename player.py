import balls, umpire

def main():

    user_ball = []
    computer_ball = []
    attempt_count = 1
    max_count = 5

    b = balls.Pitcher()
    u = umpire.Umpire()

    ball_count = 0
    strike_count = 0

    computer_ball = b.throw()

    if attempt_count >= max_count:
        print("게임 오버!")
        return

    print("숫자 게임에 오신 것을 환영합니다.")

    while strike_count != 3 and attempt_count - 1 < max_count:
        user_ball = []
        attempt_remaining = max_count - attempt_count

        if attempt_remaining == 0:
            print("마지막 기회입니다!")
        else:
            print(attempt_count, "번째 시도입니다.", attempt_remaining, "번의 기회가 남아있습니다.")

        for i in range(0, 3):
            print(i + 1, "번째 숫자를 입력해 주세요.")
            input_number = input()
            while input_number == "" or user_ball.__contains__(int(input_number)):
                print("잘못된 입력입니다. 다시 한 번 입력하여 주십시오.", i + 1, "번째 숫자를 입력하고 있습니다.")
                input_number = input()

            user_ball.append(int(input_number))

        ball_count = u.ball_count(user_ball, computer_ball)
        strike_count = u.strike_count(user_ball, computer_ball)

        print(ball_count, "B ", strike_count, "S!")
        attempt_count += 1


    if attempt_count - 1 >= max_count:
        print("기회를 모두 날렸습니다. 다음엔 꼭 성공하세요.")
        return

    print("You Win!")


main()

