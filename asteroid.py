import random
import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        # The original asteroid is always destroyed.
        self.kill()

        # The smallest asteroid disappears without creating more asteroids.
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        # Generate an angle between 20 and 50 degrees.
        angle = random.uniform(20, 50)

        # Create two new movement directions.
        velocity_1 = self.velocity.rotate(angle)
        velocity_2 = self.velocity.rotate(-angle)

        # Each new asteroid is one size smaller.
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_1 = Asteroid(
            self.position.x,
            self.position.y,
            new_radius,
        )
        asteroid_2 = Asteroid(
            self.position.x,
            self.position.y,
            new_radius,
        )

        # Smaller asteroids move 20% faster.
        asteroid_1.velocity = velocity_1 * 1.2
        asteroid_2.velocity = velocity_2 * 1.2