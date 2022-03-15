from typing import List

import pygame

from ping_pong_paradox import (
    Paddle,
    Ball
)


def paddle_with_ball(ball: Ball, paddles: List[Paddle]):
    assert len(paddles) == 2
    f"Currently only 2 paddles are supported. The given list of paddles has size {len(paddles)}"

    left_paddle = paddles[0]
    right_paddle = paddles[1]

    # Left paddle
    left_paddle.try_to_hit_the_ball(ball=ball)

    # Right paddle
    right_paddle.try_to_hit_the_ball(ball=ball)


def screen_border(window: pygame.Surface, ball: Ball):

    # Top of screen
    if ball.y - ball.radius < 0:
        ball.y_velocity *= -1
    # Bottom of screen
    if ball.y + ball.radius > window.get_height():
        ball.y_velocity *= -1

    # If the ball goes out of the screen, reset it to the initial starting point
    if ball.x - ball.radius <= 0 or ball.x + ball.radius >= window.get_width():
        ball.reset()
