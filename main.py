import math
import random
import socket
import struct
import threading
import pygame
import sys
import time
import mockNeuroPype
from particle import Particle

class VisualizationManager:
    def __init__(self):
        # Start up PyGame instance
        pygame.init()

        # Create time-related attributes
        self.clock = pygame.time.Clock()
        self.time = time.time()
        self.dt = 0

        # Create display-related attributes
        self.display_width = 800
        self.display_height = 800
        self.display = pygame.display.set_mode((self.display_width, self.display_height), flags=pygame.SCALED, vsync=1)
        self.surface = pygame.Surface((self.display_width, self.display_height))
        pygame.display.set_caption('Neuropype Visualization')
        self.fps = 60
        self.center = (self.display_width // 2, self.display_height // 2)
        self.radius = min(self.display_width, self.display_height) // 3

        # Define the colors
        self.colors = {
            "WHITE": (255, 255, 255),
            "BLACK": (0, 0, 0),
            "RED": (255, 0, 0)
        }

        # Define the data array
        self.history = [[0] * 7]

        # Create the particle group
        self.num_particles = 7
        self.particle_group = pygame.sprite.Group()
        self._initialize_particles()

    def _initialize_particles(self):
        for i in range(self.num_particles):
            angle = math.radians((i + 0.5) * (360 / self.num_particles))
            Particle(angle, self.particle_group)

    # Function to draw circle divided into sections like slices of a pie
    def _draw_circle_sections(self):
        num_sections = 7
        section_angle = 360 / num_sections

        pygame.draw.circle(self.surface, self.colors["BLACK"], self.center, self.radius, 2)

        for i in range(num_sections):
            end_angle = math.radians((i + 1) * section_angle)

            # Draw line from center to arc
            line_start = (self.center[0], self.center[1])
            line_end = (int(self.center[0] + self.radius * math.cos(end_angle)), int(self.center[1] + self.radius * math.sin(end_angle)))
            pygame.draw.line(self.surface, self.colors["BLACK"], line_start, line_end, 2)

    def update_particles(self):
        self.particle_group.update()

    def draw_particles(self):
        self.particle_group.draw(self.surface)

    def set_anchor_positions(self):
        for i, particle in enumerate(self.particle_group):
            if i < len(positions):
                particle.set_anchor(positions[i] * 50)

    # Function to draw dot within a section
    def _draw_data_dot(self, pos, section):
        center = (self.display_width // 2, self.display_height // 2)
        radius = min(self.display_width, self.display_height) // 3
        num_sections = 7
        section_angle = 360 / num_sections
        midpoint_angle = math.radians((section + 0.5) * section_angle)

        # Calculate position of dot based on value
        dot_radius = 5
        dot_distance = pos * radius
        x = center[0] + int(dot_distance * math.cos(midpoint_angle))
        y = center[1] + int(dot_distance * math.sin(midpoint_angle))

        pygame.draw.circle(self.surface, self.colors["RED"], (x, y), dot_radius)

    def _draw_all_data_dots(self):
        for section, position in enumerate(self.history[-1]):
            self._draw_data_dot(position, section)

    # Function to handle input from NeuroPype
    def handle_neuropype_input(self, data):
        # Save history of inputs received
        self.history.append(data)
        self.set_anchor_positions()

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
        # Receive new data from NeuroPype
        pass

    def _check_events(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif e.type == NEUROPYPE_EVENT:
                self.history.append(e.data)

    def _update_screen(self):
        self.surface.fill(self.colors["WHITE"])
        self._draw_circle_sections()
        self._draw_all_data_dots()

        # Scale display to full size
        scaled_surface = pygame.transform.scale(self.surface, (self.display_width, self.display_height))

        # Blit to screen surface
        self.display.blit(scaled_surface, (0, 0))

        # Update the surface
        pygame.display.flip()

        # Update clock by fps
        self.clock.tick(self.fps)


# Function to listen for data from NeuroPype
def neuropype_listener(visManager):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    print("Connected to NeuroPype")

    try:
        while True:
            data = client_socket.recv(28)  # 7 floats * 4 bytes each = 28 bytes
            if data:
                data_array = struct.unpack('7f', data)
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
    neuro_thread = threading.Thread(target=mockNeuroPype.neuropype_simulator)
    neuro_thread.daemon = True
    neuro_thread.start()

    # Initialize Visualization Manager
    vis = VisualizationManager()

    # Start the NeuroPype listener in a separate thread
    listener_thread = threading.Thread(target=neuropype_listener, args=(vis,))
    listener_thread.daemon = True  # Daemonize the thread to exit when the main program exits
    listener_thread.start()

    # Begin Visualization
    vis.run_visualization()
