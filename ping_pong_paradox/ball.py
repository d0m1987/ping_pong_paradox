import pygame

from ping_pong_paradox.config import WHITE


class Ball:
    MAX_RADIUS = 15
    COLOR = WHITE
    MAX_VELOCITY = 15

    def __init__(
        self,
        window: pygame.Surface,
        x: int = None,
        y: int = None,
        radius: int = None,
        x_velocity: int = None,
        y_velocity: int = None
    ) -> None:

        self.window = window
        self.x = self.x_original = x or (window.get_width() * 0.4)
        self.y = self.y_original = y or (window.get_height() // 2)
        self.radius = radius or Ball.MAX_RADIUS
        self.x_velocity = x_velocity or Ball.MAX_VELOCITY
        self.y_velocity = y_velocity or Ball.MAX_VELOCITY

    def draw(self):
        pygame.draw.circle(
            surface=self.window,
            color=self.COLOR,
            center=(self.x, self.y),
            radius=self.radius
        )

    def move(self):
        self.x += self.x_velocity
        self.y += self.y_velocity

    def reset(self):
        self.x = self.x_original
        self.y = self.y_original
