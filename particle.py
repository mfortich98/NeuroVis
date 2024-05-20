import math
import pygame


class Particle(pygame.sprite.Sprite):
    def __init__(self, center, radius, angle, *groups):
        super().__init__(*groups)
        self.angle = angle
        self.center = center
        self.radius = radius
        self.speed = 0.1
        self.vector = pygame.math.Vector2(self.speed, 0).rotate_rad(angle)
        self.anchor = self.radius
        self.tether = 0.5
        self.image = pygame.image.load('images/particle.png').convert_alpha()
        self.rect = self.image.get_rect(center=center)

    def update(self):
        # If the particle exceeds max distance, it reverses direction
            # In the center
            if
            # Outside the border
            # Under Anchor
            # Over Anchor
        if self.vector < self.center or self.vector < self.anchor.scale_to_length() < (self.anchor - self.tether):
            self.vector *= -1

        # Update radius (distance from center)
        self.vector.scale_to_length(self.anchor + self.speed)

        # Update the sprite's rect position
        self.rect.center += self.vector
        print(f'{self.angle}: pos({self.rect.center})')

    def set_anchor(self, anchor):
        self.anchor = pygame.math.Vector2(anchor, 0).rotate_rad(self.angle)




