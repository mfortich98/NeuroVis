import pygame
import sys
import random
import numpy as np
import os

# Initialize Pygame
pygame.init()

os.environ['SDL_Video_Centered'] = '1'
info = pygame.display.Info()


# Set up the display
width, height = info.current_w, info.current_h
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Coherence Visualization")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Constants
num_dots = 1
dot_radius = 5
circle_radius = 100
circle_center = (width // 2, height // 2)
max_movement = 2
coherence_values = [1.0]*7 # Initially all coherence values are set to 1

# Function to draw the circle of around 0.7 coherence
def draw_circle():
    pygame.draw.circle(screen, BLACK, circle_center, circle_radius, 2)

# Function to draw inner circle of around 0.9 coherence
def draw_circle2():
    pygame.draw.circle(screen, GREEN, circle_center, 40, 100)

# Function to draw the dots
def draw_dots():
    for i, coherence in enumerate(coherence_values):
        angle = (i * (2 * np.pi / len(coherence_values))) - (np.pi/2)
        x = circle_center[0] + int(300 * (1-coherence) * np.cos(angle))
        y = circle_center[1] + int(300 * (1-coherence) * np.sin(angle))
        for _ in range(num_dots):
            dot_x = x + random.randint(-max_movement, max_movement)
            dot_y = y + random.randint(-max_movement, max_movement)
            pygame.draw.circle(screen, (0, 0, int(255 * coherence)), (dot_x, dot_y), dot_radius)

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Update coherence values (You need to replace this with your actual coherence value update mechanism)
    coherence_values = [random.uniform(0.001, 1.0) for _ in range(7)]

    # Draw
    draw_circle()
    draw_circle2()
    draw_dots()

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
