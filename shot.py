import pygame

from circleshape import CircleShape
from constants import SHOT_RADIUS, SHOT_WIDTH


class Shot(CircleShape):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, SHOT_WIDTH)

    def update(self, dt: float) -> None:
        self.position += dt * self.velocity
