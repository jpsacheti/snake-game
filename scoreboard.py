from turtle import Turtle

FONT_STYLE = ('Arial', 12, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 270)
        self.display_score()

    def increment_score(self):
        self.score += 1

    def update(self):
        self.clear()
        self.increment_score()
        self.display_score()

    def display_score(self):
        self.write(f'Score: {self.score}', align='center', font=FONT_STYLE, move=False)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=FONT_STYLE)
