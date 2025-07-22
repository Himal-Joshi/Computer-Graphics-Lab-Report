import pygame
import sys

# Initialize Pygame
pygame.init()

# Set screen dimensions and create a window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Midpoint Ellipse Drawing Algorithm")

# Set white background
screen.fill((255, 255, 255))  # background to white

# Define colors for each quadrant
RED    = (255, 0, 0)       # Quadrant I
GREEN  = (0, 255, 0)       # Quadrant II
BLUE   = (0, 0, 255)       # Quadrant IV
PURPLE = (128, 0, 128)     # Quadrant III

def plot_ellipse_points(xc, yc, x, y):
    # Quadrant I (x+, y+)
    screen.set_at((xc + x, yc - y), RED)
    # Quadrant II (x−, y+)
    screen.set_at((xc - x, yc - y), GREEN)
    # Quadrant III (x−, y−)
    screen.set_at((xc - x, yc + y), PURPLE)
    # Quadrant IV (x+, y−)
    screen.set_at((xc + x, yc + y), BLUE)



def midpoint_ellipse(rx, ry, xc, yc):
    x = 0
    y = ry

    # Decision parameter for region 1
    p1 = ry**2 - (rx**2 * ry) + (0.25 * rx**2)
    dx = 2 * ry**2 * x
    dy = 2 * rx**2 * y

    # Region 1
    while dx < dy:
        plot_ellipse_points(xc, yc, x, y)
        x += 1
        dx = 2 * ry**2 * x
        if p1 < 0:
            p1 += dx + ry**2
        else:
            y -= 1
            dy = 2 * rx**2 * y
            p1 += dx - dy + ry**2

    # Decision parameter for region 2
    p2 = (ry**2) * ((x + 0.5)**2) + (rx**2) * ((y - 1)**2) - (rx**2 * ry**2)

    # Region 2
    while y >= 0:
        plot_ellipse_points(xc, yc, x, y)
        y -= 1
        dy = 2 * rx**2 * y
        if p2 > 0:
            p2 -= dy + rx**2
        else:
            x += 1
            dx = 2 * ry**2 * x
            p2 += dx - dy + rx**2

# Ellipse parameters
rx = 200  # Horizontal radius
ry = 100  # Vertical radius
xc = width // 2  # X-center
yc = height // 2  # Y-center

# Draw the ellipse
midpoint_ellipse(rx, ry, xc, yc)

# Display the result
pygame.display.flip()

# Wait until window is closed
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
