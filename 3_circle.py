import pygame
import sys

# Initialize Pygame
pygame.init()

# Set screen dimensions and create a window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Midpoint Circle Drawing Algorithm")

# Set white background
screen.fill((255, 255, 255))  # background to white

# Define colors for each quadrant
RED    = (255, 0, 0)       # Quadrant I
GREEN  = (0, 255, 0)       # Quadrant II
PURPLE = (128, 0, 128)     # Quadrant III
BLUE   = (0, 0, 255)       # Quadrant IV

# Plot symmetric points in 4 quadrants
def plot_circle_points(xc, yc, x, y):
    # Quadrant I (+x, -y)
    screen.set_at((xc + x, yc - y), RED)
    # Quadrant II (-x, -y)
    screen.set_at((xc - x, yc - y), GREEN)
    # Quadrant III (-x, +y)
    screen.set_at((xc - x, yc + y), PURPLE)
    # Quadrant IV (+x, +y)
    screen.set_at((xc + x, yc + y), BLUE)

    # Also plot the diagonal octants (optional or reuse quadrant colors)
    screen.set_at((xc + y, yc - x), RED)      # Quadrant I
    screen.set_at((xc - y, yc - x), GREEN)    # Quadrant II
    screen.set_at((xc - y, yc + x), PURPLE)   # Quadrant III
    screen.set_at((xc + y, yc + x), BLUE)     # Quadrant IV

# Midpoint circle drawing function
def midpoint_circle(radius, xc, yc):
    x = 0
    y = radius
    p = 1 - radius

    plot_circle_points(xc, yc, x, y)

    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        plot_circle_points(xc, yc, x, y)

# Circle parameters
radius = 150
xc = width // 2
yc = height // 2

# Draw the circle
midpoint_circle(radius, xc, yc)

# Display the result
pygame.display.flip()

# Wait until window is closed
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
