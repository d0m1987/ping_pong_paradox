from typing import List

import pygame

from ping_pong_paradox import (
    Paddle,
    Ball
)


def paddle_movement(pressed_keys, paddles: List[Paddle]):
    assert len(paddles) == 2
    f"Currently only 2 paddles are supported. The given list of paddles has size {len(paddles)}"

    left_paddle = paddles[0]
    right_paddle = paddles[1]

    # Handle left paddle movement with W & S keys
    if pressed_keys[pygame.K_w]:
        left_paddle.up()
    if pressed_keys[pygame.K_s]:
        left_paddle.down()

    # Handle right paddle movement with I & K keys
    if pressed_keys[pygame.K_i]:
        right_paddle.up()
    if pressed_keys[pygame.K_k]:
        right_paddle.down()


def collision(window: pygame.Surface, ball: Ball, paddles: List[Paddle]):
    assert len(paddles) == 2
    f"Currently only 2 paddles are supported. The given list of paddles has size {len(paddles)}"

    left_paddle = paddles[0]
    right_paddle = paddles[1]

    # Top of screen
    if ball.y - ball.radius < 0:
        ball.y_velocity *= -1
    # Bottom of screen
    if ball.y + ball.radius > window.get_height():
        ball.y_velocity *= -1

    # Left paddle
    left_paddle.try_to_hit_the_ball(ball=ball)

    # Right paddle
    right_paddle.try_to_hit_the_ball(ball=ball)

    # If the ball goes out of the screen, reset it to the initial starting point
    if ball.x - ball.radius <= 0 or ball.x + ball.radius >= window.get_width():
        ball.reset()
