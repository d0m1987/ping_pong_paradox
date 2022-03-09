"""Main module."""
from typing import List

import pygame
pygame.init()

#########################
# General game settings #
#########################
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode(size=(WIDTH, HEIGHT))
FPS = 60
pygame.display.set_caption('Ping Pong Paradox')

##########
# Colors #
##########
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Paddle:
    COLOR = WHITE
    BORDER_DISTANCE = 10
    WIDTH = 10

    def __init__(
            self,
            window: pygame.Surface,
            height: int = 100,
            is_right_paddle: bool = False) -> None:

        self.window = window
        self.height = height
        # If it is the right paddle, calculate the paddle upper left corner x coordinate.
        # For the left paddle, just set the distance between left border and paddle.
        self.x = self.window.get_width() - Paddle.WIDTH - \
            Paddle.BORDER_DISTANCE if is_right_paddle else Paddle.BORDER_DISTANCE
        self.y = self.centered_y_value()

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


class Net:
    COLOR = WHITE
    WIDTH = 10

    def __init__(self, window: pygame.Surface) -> None:
        self.window = window
        self.rectangles = []

    def calculate_net(self, number_of_net_parts: int = 20):
        self.rectangles = []
        # Iterate from top border (y=0) to bottom border (y=self.window.get_height()) in equal distance
        for net_part_index, net_y in enumerate(range(0, self.window.get_height(), self.window.get_height() // number_of_net_parts)):
            # Skip every second net part
            if net_part_index % 2 == 1:
                continue

            # Save rectangles as dictionary, such that it can be unpacked for drawing
            self.rectangles.append(
                {
                    "surface": self.window,
                    "color": Net.COLOR,
                    "rect": (
                        self.window.get_width() // 2 - Net.WIDTH // 2,
                        net_y,
                        Net.WIDTH,
                        self.window.get_height() / number_of_net_parts
                    )
                }
            )

    def draw(self):
        [pygame.draw.rect(**rectangle) for rectangle in self.rectangles]


class Ball:
    MAX_RADIUS = 25
    COLOR = WHITE

    def __init__(
        self,
        window: pygame.Surface,
        x: int = None,
        y: int = None,
        radius: int = None,
    ) -> None:

        self.window = window
        self.x = x or (window.get_width() * 0.4)
        self.y = y or (window.get_height() // 2)
        self.radius = radius or Ball.MAX_RADIUS // 2

    def draw(self):
        pygame.draw.circle(
            surface=self.window,
            color=self.COLOR,
            center=(self.x, self.y),
            radius=self.radius
        )


def draw(
        window: pygame.Surface,
        paddles: List[Paddle],
        net: Net,
        ball: Ball):
    window.fill(color=BLACK)
    [paddle.draw() for paddle in paddles]
    net.draw()
    ball.draw()
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()

    paddles = [Paddle(WINDOW), Paddle(WINDOW, is_right_paddle=True)]
    net = Net(WINDOW)
    net.calculate_net(20)
    ball = Ball(WINDOW)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw(WINDOW, paddles=paddles, net=net, ball=ball)

    pygame.quit()


if __name__ == '__main__':
    main()
