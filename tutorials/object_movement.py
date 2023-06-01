import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Smooth Object Movement")

# Set up the object
object_width = 50
object_height = 50
object_x = (window_width - object_width) // 2
object_y = (window_height - object_height) // 2
object_speed = 300  # pixels per second

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate delta time
    dt = clock.tick(60) / 1000.0  # Limit frame rate to 60 FPS

    # Move the object
    object_x += object_speed * dt

    # Clear the screen
    window.fill((0, 0, 0))

    # Draw the object
    pygame.draw.rect(window, (255, 0, 0), (object_x, object_y, object_width, object_height))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
