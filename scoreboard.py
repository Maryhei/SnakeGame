from turtle import Turtle
SCORE = 0
high_score = 0


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.penup()
        self.pencolor("white")
        self.hideturtle()
        self.score_counting()



    def score_counting(self):
        self.setposition(x=30, y=255)
        self.write(f"Score: {SCORE} High Score: {high_score}", align="right", font=('Arial', 30, 'normal'))

    def reset(self):
        if SCORE > high_score:
            high_score = SCORE
