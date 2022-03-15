import pygame

from ping_pong_paradox import Paddle


class Player:
    def __init__(self, window: pygame.Surface, paddle: Paddle, score: int = 0) -> None:
        self.window = window
        self.paddle = paddle or Paddle()
        self.score = score
    
