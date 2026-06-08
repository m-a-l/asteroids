import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_ACCELERATION, ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        log_event("asteroid_split")
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        rotation = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = self.velocity.rotate(rotation) * ASTEROID_ACCELERATION
        asteroid2.velocity = self.velocity.rotate(-rotation) * ASTEROID_ACCELERATION
