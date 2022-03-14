import pygame

from ping_pong_paradox import Ball
from ping_pong_paradox.config import WHITE


class Paddle:
    COLOR = WHITE
    BORDER_DISTANCE = 10
    WIDTH = 10
    # The name MAX_VELOCITY is used since in the future it is planned to in-/decrease
    # paddle movement speed dynamically
    MAX_VELOCITY = 15

    def __init__(
            self,
            window: pygame.Surface,
            height: int = 100,
            is_right_paddle: bool = False,
            velocity: int = None) -> None:

        self.window = window
        self.height = height
        self.is_right_paddle = is_right_paddle
        # If it is the right paddle, calculate the paddle upper left corner x coordinate.
        # For the left paddle, just set the distance between left border and paddle.
        self.x = self.window.get_width() - Paddle.WIDTH - \
            Paddle.BORDER_DISTANCE if is_right_paddle else Paddle.BORDER_DISTANCE
        self.y = self.centered_y_value()
        self.velocity = velocity or Paddle.MAX_VELOCITY // 2

    def centered_y_value(self):
        '''
        Calculate the needed y value, such that the paddle is centered in screen height.
        '''
        return self.window.get_height() // 2 - self.height // 2

    def draw(self):
        pygame.draw.rect(
            surface=self.window,
            color=self.COLOR,
            rect=(self.x, self.y, Paddle.WIDTH, self.height)
        )

    def up(self):
        if (self.y - self.velocity) > 0:
            self.y -= self.velocity
        else:
            self.y = 0

    def down(self):
        if (self.y + self.height + self.velocity) < self.window.get_height():
            self.y += self.velocity
        else:
            self.y = self.window.get_height() - self.height

    def try_to_hit_the_ball(self, ball: Ball):
        if self.y <= ball.y <= self.y + self.height:
            if not self.is_right_paddle and (ball.x - ball.radius <= self.x + self.WIDTH):
                ball.x_velocity *= -1

                middle_y = self.y + self.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (self.height / 2) / ball.MAX_VELOCITY
                y_vel = difference_in_y / reduction_factor
                ball.y_velocity = -1 * y_vel

            if self.is_right_paddle and (ball.x + ball.radius >= self.x):
                ball.x_velocity *= -1

                middle_y = self.y + self.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (self.height / 2) / ball.MAX_VELOCITY
                y_vel = difference_in_y / reduction_factor
                ball.y_velocity = -1 * y_vel
