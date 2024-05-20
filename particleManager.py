import pygame
import math
from particle import Particle


class ParticleManager:
    def __init__(self, display_width, display_height, surface, num_particles=7):
        self.display_width = display_width
        self.display_height = display_height
        self.surface = surface
        self.num_particles = num_particles
        self.particle_group = pygame.sprite.Group()
        self.colors = {"RED": (255, 0, 0)}
        self.history = []  # This should be set to the data history you want to visualize

        self._initialize_particles()

    def _initialize_particles(self):
        center = (self.display_width // 2, self.display_height // 2)
        for i in range(self.num_particles):
            particle = Particle()
            particle.angle = math.radians((i + 0.5) * (360 / self.num_particles))
            particle.rect.center = center
            self.particle_group.add(particle)

    def update_particles(self):
        self.particle_group.update()

    def draw_particles(self):
        self.particle_group.draw(self.surface)

    def set_particle_positions(self, positions):
        for i, particle in enumerate(self.particle_group):
            if i < len(positions):
                particle.set_anchor(positions[i] * 50)  # Assuming the scale factor of 50 as in previous examples
