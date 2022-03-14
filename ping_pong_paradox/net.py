import pygame

from ping_pong_paradox.config import WHITE


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
