import sys
import time

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event, log_state
from particle import Particle
from player import Player
from shot import Shot


def main():
    # Pygame init
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while not pygame.display.get_active():
        print("booting...")
    pygame.display.set_caption("Asteroids")

    # All groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    particles = pygame.sprite.Group()

    # All containers
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Player.containers = (updatable, drawable)
    Particle.containers = (particles, updatable, drawable)

    # Variables to init
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    time_since_game_over = 0.0

    # Game loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                player.explode(screen)
                time_since_game_over = 0.1

            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()

        # Draw
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)

        if time_since_game_over > 0:
            time_since_game_over += dt
            blit_centered_text(screen, "GAME OVER", bg="black")
        if time_since_game_over > 1:
            print("Game over!")
            pygame.time.wait(3 * 1000)
            sys.exit()
        pygame.display.flip()

        dt = clock.tick(60) / 1000


def blit_centered_text(
    surface: pygame.Surface,
    text: str,
    size: int = 100,
    color: tuple = (255, 255, 255),
    bg=None,
):
    font = pygame.font.SysFont(None, size)
    text_surf = font.render(text, True, color, bg)
    rect = text_surf.get_rect(center=surface.get_rect().center)
    surface.blit(text_surf, rect)


if __name__ == "__main__":
    main()
