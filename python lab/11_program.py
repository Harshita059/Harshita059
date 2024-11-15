import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the screen
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Elliptical Orbit Simulation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SUN_COLOR = (255, 255, 0)
PLANET_COLOR = (0, 0, 255)

# Constants for the elliptical orbit
center_x, center_y = width // 2, height // 2  # Center of the orbit (focus point)
a = 200  # Semi-major axis (horizontal stretch)
b = 120  # Semi-minor axis (vertical stretch)
speed = 0.02  # Speed of the orbit

# Planet parameters
planet_radius = 10

# Clock
clock = pygame.time.Clock()

# Orbit simulation loop
angle = 0  # Start angle

running = True
while running:
    screen.fill(BLACK)  # Fill the screen with black
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate the position of the planet based on the parametric equation
    x = center_x + a * math.cos(angle)
    y = center_y + b * math.sin(angle)

    # Draw the Sun at the center
    pygame.draw.circle(screen, SUN_COLOR, (center_x, center_y), 30)

    # Draw the Planet at the calculated position
    pygame.draw.circle(screen, PLANET_COLOR, (int(x), int(y)), planet_radius)

    # Update the angle to simulate orbit
    angle += speed

    # Refresh the screen
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
