from ping_pong_paradox.config import (
    WIDTH,
    HEIGHT,
    BLACK,
    FPS
)
from ping_pong_paradox import (
    Ball,
    Paddle,
    Net,
    handler
)
from typing import List

import pygame
pygame.init()


WINDOW = pygame.display.set_mode(size=(WIDTH, HEIGHT))


def draw(
        window: pygame.Surface,
        paddles: List[Paddle],
        net: Net,
        ball: Ball):
    window.fill(color=BLACK)
    [paddle.draw() for paddle in paddles]
    net.draw()
    ball.move()
    ball.draw()
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()

    paddles = [Paddle(WINDOW), Paddle(WINDOW, is_right_paddle=True)]
    net = Net(WINDOW)
    net.calculate_net(20)
    ball = Ball(WINDOW, x_velocity=5, y_velocity=5)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        pressed_keys = pygame.key.get_pressed()
        handler.paddle_movement(pressed_keys=pressed_keys, paddles=paddles)
        handler.collision(window=WINDOW, ball=ball, paddles=paddles)
        draw(WINDOW, paddles=paddles, net=net, ball=ball)

    pygame.quit()


if __name__ == '__main__':
    main()
