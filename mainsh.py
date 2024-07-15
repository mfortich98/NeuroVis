import math
import random
import socket
import struct
import threading
import pygame
import sys
import time
import mockNeuroPype
import os
from label import Label
from particle import Particle
from settings import settings

pygame.init()

os.environ['IBS Program'] = '1'
info = pygame.display.Info()
width, height = info.current_w, info.current_h


class VisualizationManager:
    def __init__(self, chosen_settings):
        # Start up PyGame instance
        pygame.init()

        # Create time-related attributes
        self.clock = pygame.time.Clock()
        self.time = time.time()
        self.dt = 0

        # Create display-related attributes
        self.display_width = width  #chosen_settings.display_size
        self.display_height = height
        self.display = pygame.display.set_mode((self.display_width, self.display_height), flags=pygame.SCALED, vsync=1)
        self.surface = pygame.Surface((self.display_width, self.display_height))
        pygame.display.set_caption('IBS Program')
        self.fps = 60
        self.center = (self.display_width // 2, self.display_height // 2)
        self.radius = min(self.display_width, self.display_height) // 2.5
        self.label = Label(self.surface)

        # Define the colors
        self.colors = {
            "WHITE": (255, 255, 255),
            "BLACK": (0, 0, 0),
            "RED": (255, 0, 0),
            "GREEN": (0, 255, 0)
        }

        # Define the data array
        self.history = [[0] * 1]

        # Create the particle variables
        self.num_particles = chosen_settings.num_particles
        self.particle_ms = chosen_settings.particle_speed
        self.particle_tether_range = chosen_settings.particle_tether_range
        self.anchor_assignment = chosen_settings.anchor_assignment
        self.num_synch_values = 1
        self.particle_group = pygame.sprite.Group()
        self._initialize_particles()

    def run_visualization(self):
        while True:
            # Framerate independence calculation
            now = time.time()
            self.dt = now - self.time
            self.time = now

            self._resolve_actions()
            self._check_events()
            self._update_screen()

    def _resolve_actions(self):
        self.update_particles()
        self.update_labels()

    def _check_events(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif e.type == NEUROPYPE_EVENT:
                self.history.append(e.data)
                self.set_anchor_positions()

    def _update_screen(self):
        self.surface.fill(self.colors["WHITE"])
        self._draw_circle()
        self.draw_particles()
        if settings.label_on:
            self.label.draw()

        # Scale display to full size
        # scaled_surface = pygame.transform.scale(self.surface, (self.display_width, self.display_height))

        # Blit to screen surface
        self.display.blit(self.surface, (0, 0))

        # Update the surface
        pygame.display.flip()

        # Update clock by fps
        self.clock.tick(self.fps)

    def update_particles(self):
        self.particle_group.update()

    def update_labels(self):
        self.label.update(self.history[-1])

    def _initialize_particles(self):
        for i in range(self.num_particles):
            angle = math.radians(i * (360 / self.num_particles))
            Particle(self.particle_ms, self.particle_tether_range, self.center, self.radius, angle, self.particle_group)

    # Function to draw circle divided into sections like slices of a pie
    def _draw_circle(self):
        # section_angle = 360 / self.num_particles

        pygame.draw.circle(self.surface, self.colors["BLACK"], self.center, self.radius * 1.06, 2)
        pygame.draw.circle(self.surface, self.colors["BLACK"], self.center, self.radius * 0.57, 1)  #at 0.5 coherence
        pygame.draw.circle(self.surface, self.colors["GREEN"], self.center, self.radius * 0.27, 100)  #at 0.8 coherence

        # for i in range(self.num_particles):
        #     end_angle = math.radians(i * section_angle)
        #
        #     # Draw line from center to arc
        #     line_start = (self.center[0], self.center[1])
        #     line_end = (int(self.center[0] + self.radius * math.cos(end_angle)),
        #                 int(self.center[1] + self.radius * math.sin(end_angle)))
        #     pygame.draw.line(self.surface, self.colors["BLACK"], line_start, line_end, 2)

    def draw_particles(self):
        self.particle_group.draw(self.surface)

    def set_anchor_positions(self):
        if self.anchor_assignment == "random":
            for particle in self.particle_group:
                random_assign = random.choice((0, 1))
                if random_assign == 0:
                    particle.set_anchor(self.history[-1][0])
                else:
                    particle.set_anchor(self.history[-1][0])  #used to be 1 for the second value

        elif self.anchor_assignment == "halves":
            half = self.num_particles // self.num_synch_values
            for i, particle in enumerate(self.particle_group):
                if i < half:
                    particle.set_anchor(self.history[-1][0])
                else:
                    particle.set_anchor(self.history[-1][1])

        elif self.anchor_assignment == "even_odd":
            for i, particle in enumerate(self.particle_group):
                if i % 2 == 0:
                    particle.set_anchor(self.history[-1][0])
                else:
                    particle.set_anchor(self.history[-1][1])

    # Function to handle input from NeuroPype
    def handle_neuropype_input(self, data):
        # Save history of inputs received
        self.history.append(data)
        self.set_anchor_positions()


# Function to listen for data from NeuroPype
def neuropype_listener():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    print("Connected to NeuroPype")

    try:
        while True:
            data = client_socket.recv(4)  # 1 floats * 4 bytes each = 4 bytes
            if data:
                data_array = struct.unpack('1f', data)
                # Create a custom event with NeuroPype data
                event = pygame.event.Event(NEUROPYPE_EVENT, data=data_array)
                # Post the event to the Pygame event queue
                pygame.event.post(event)
    finally:
        client_socket.close()


# Run Visualization
if __name__ == '__main__':
    # Define a custom event type
    NEUROPYPE_EVENT = pygame.USEREVENT + 1

    # Initialize Fake NeuroPype
    neuro_thread = threading.Thread(target=mockNeuroPype.neuropype_simulator, args=(settings.mock_update_rate, settings.mock_value_range))
    neuro_thread.daemon = True
    neuro_thread.start()

    # Initialize Visualization Manager
    vis = VisualizationManager(settings)

    # Start the NeuroPype listener in a separate thread
    listener_thread = threading.Thread(target=neuropype_listener)
    listener_thread.daemon = True  # Daemonize the thread to exit when the main program exits
    listener_thread.start()

    # Begin Visualization
    vis.run_visualization()
