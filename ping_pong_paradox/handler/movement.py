from typing import List

import pygame

from ping_pong_paradox import Paddle, Ball


def paddle(pressed_keys, paddles: List[Paddle]):
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

def ball(ball:Ball):
    ball.move()
