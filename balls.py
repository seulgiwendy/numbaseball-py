import random

class Pitcher():

    def throw(self):

        balls_array = []
        for _ in range(1, 4):
            random_int = random.randrange(1, 10)

            while balls_array.__contains__(random_int):
                random_int = random.randrange(1, 10)

            balls_array.append(random_int)

        balls_array.sort()

        print(balls_array)
        return balls_array
