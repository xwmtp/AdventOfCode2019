
class AI:

    def __init__(self, game):
        self.game = game
        self.ball = game.ball
        self.prev_ball = None
        self.paddle = game.paddle


    def play(self):
        self.prev_ball = self.ball

        while True:

            hold = self.decide_joystick()
            self.move(hold)

            if self.game_over():
                return self.game.score

    def move(self, hold):
        self.prev_ball = self.ball
        self.game.play(hold)
        self.ball, self.paddle = self.game.ball, self.game.paddle

    def game_over(self):
        return self.ball == self.prev_ball

    def decide_joystick(self):
        ball_x, ball_y = self.ball
        prev_x, prev_y = self.prev_ball
        paddle_x, paddle_y = self.paddle

        diff = paddle_x - ball_x
        moving_downwards = prev_y < ball_y

        if moving_downwards:
            ball_dir = ball_x > prev_x
            offset = 0 if ball_dir else -2

            if diff <= 0 + offset:
                return 'right'
            if diff >= 2 + offset:
                return 'left'
        else:
            if diff > 0:
                return 'left'
            if diff < 0:
                return 'right'
        return 'neutral'

