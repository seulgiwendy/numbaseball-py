class Umpire():

    def ball_count(self, player_list, answer_list):

        counted_ball = 0

        for i in range(len(player_list)):
            user_ball = player_list[i]

            if user_ball in answer_list and user_ball != answer_list[i]:
                counted_ball += 1

        return counted_ball

    def strike_count(self, player_list, answer_list):

        counted_strike = 0

        for i in range(len(player_list)):
            if player_list[i] == answer_list[i]:
                counted_strike += 1

        return counted_strike

