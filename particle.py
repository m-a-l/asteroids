import random

import pygame

from circleshape import CircleShape
from constants import SHOT_RADIUS


class Particle(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        self.radius = SHOT_RADIUS
        self.color = "red"
        super().__init__(x, y, self.radius)
        rotation = random.uniform(-180, 180)
        self.velocity = pygame.Vector2(0, 1)
        self.velocity = self.velocity.rotate(rotation) * 300

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, self.color, self.position, self.radius, 0)

    def update(self, dt: float) -> None:
        self.position += dt * self.velocity
