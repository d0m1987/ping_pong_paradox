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
    # The name MAX_VELOCITY is used since in the future it is planned to in-/decrease 
    # paddle movement speed dynamically
    MAX_VELOCITY = 5 

    def __init__(
            self,
            window: pygame.Surface,
            height: int = 100,
            is_right_paddle: bool = False,
            velocity:int = None) -> None:

        self.window = window
        self.height = height
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
    MAX_VELOCITY = 25

    def __init__(
        self,
        window: pygame.Surface,
        x: int = None,
        y: int = None,
        radius: int = None,
        x_velocity:int = None,
        y_velocity:int = None
    ) -> None:

        self.window = window
        self.x = self.x_original = x or (window.get_width() * 0.4)
        self.y = self.y_original = y or (window.get_height() // 2)
        self.radius = radius or Ball.MAX_RADIUS // 2
        self.x_velocity = x_velocity or Ball.MAX_VELOCITY // 2
        self.y_velocity = y_velocity or Ball.MAX_VELOCITY // 2

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

def paddle_movement_handler(pressed_keys, paddles:List[Paddle]):
    assert len(paddles) == 2; f"Currently only 2 paddles are supported. The given list of paddles has size {len(paddles)}"

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

def collision_handler(window:pygame.Surface ,ball:Ball, paddles:List[Paddle]):
    assert len(paddles) == 2; f"Currently only 2 paddles are supported. The given list of paddles has size {len(paddles)}"

    left_paddle = paddles[0]
    right_paddle = paddles[1]

    # Top of screen
    if ball.y - ball.radius < 0:
        ball.y_velocity *= -1
    # Bottom of screen
    if ball.y + ball.radius > window.get_height():
        ball.y_velocity *= -1
    
    # Left paddle
    if left_paddle.y <= ball.y <= left_paddle.y + left_paddle.height:
        if ball.x - ball.radius <= left_paddle.x + left_paddle.WIDTH:
            ball.x_velocity *= -1

    # Right paddle
    if right_paddle.y <= ball.y <= right_paddle.y + right_paddle.height:
        if ball.x + ball.radius >= right_paddle.x:
            ball.x_velocity *= -1
    
    # If the ball goes out of the screen, reset it to the initial starting point
    if ball.x - ball.radius <= 0 or ball.x + ball.radius >= window.get_width():
        ball.reset()
    
def main():
    run = True
    clock = pygame.time.Clock()

    paddles = [Paddle(WINDOW), Paddle(WINDOW, is_right_paddle=True)]
    net = Net(WINDOW)
    net.calculate_net(20)
    ball = Ball(WINDOW, x_velocity=1, y_velocity=1)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        pressed_keys = pygame.key.get_pressed()
        paddle_movement_handler(pressed_keys=pressed_keys, paddles=paddles)
        collision_handler(window=WINDOW, ball=ball, paddles=paddles)
        draw(WINDOW, paddles=paddles, net=net, ball=ball)

    pygame.quit()


if __name__ == '__main__':
    main()
