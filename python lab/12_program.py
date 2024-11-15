import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Ball")

# Ball parameters
x, y = width // 2, height // 2  # Starting position
radius = 20  # Ball radius
color = (255, 0, 0)  # Red color
dx, dy = 4, 4  # Speed of the ball

# Clock
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    screen.fill((0, 0, 0))  # Black background

    # Check for close window event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the ball
    x += dx
    y += dy

    # Bounce off the walls
    if x - radius <= 0 or x + radius >= width:
        dx = -dx  # Reverse horizontal direction
    if y - radius <= 0 or y + radius >= height:
        dy = -dy  # Reverse vertical direction

    # Draw the ball
    pygame.draw.circle(screen, color, (x, y), radius)

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
