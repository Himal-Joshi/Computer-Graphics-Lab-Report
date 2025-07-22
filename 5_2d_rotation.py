import pygame
import math

# Initialize Pygame
pygame.init()

# Window size and display
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("45 Degree Rotation")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)

# Font
font = pygame.font.SysFont(None, 16)

# Scale and points
scale = 40
points = [[0, 0, 1], [4, 0, 1], [4, 2, 1], [0, 2, 1]]
theta = math.radians(45)  # 45 degree fixed rotation

# Label for rotated shape
rotation_label = "45 Degree Rotation"
label_position = (width // 2 + 80, height // 2 - 120)

# Rotate a single point
def rotate_point(p, theta):
    x = p[0] * math.cos(theta) - p[1] * math.sin(theta)
    y = p[0] * math.sin(theta) + p[1] * math.cos(theta)
    return [x, y, 1]

# Convert to screen coordinates
def to_screen_coords(p):
    return (int(width // 2 + p[0] * scale), int(height // 2 - p[1] * scale))

# Draw grid
def draw_grid():
    for x in range(0, width, scale):
        pygame.draw.line(screen, GRAY, (x, 0), (x, height))
        screen.blit(font.render(str((x - width // 2) // scale), True, BLACK), (x, height // 2 + 5))
    for y in range(0, height, scale):
        pygame.draw.line(screen, GRAY, (0, y), (width, y))
        screen.blit(font.render(str((height // 2 - y) // scale), True, BLACK), (width // 2 + 5, y))
    pygame.draw.line(screen, BLACK, (0, height // 2), (width, height // 2), 2)  # X-axis
    pygame.draw.line(screen, BLACK, (width // 2, 0), (width // 2, height), 2)  # Y-axis

# Draw polygon with optional label
def draw_polygon(points, color, label=None, label_pos=None):
    screen_points = [to_screen_coords(p) for p in points]
    pygame.draw.polygon(screen, color, screen_points, 2)
    for p in points:
        x, y = to_screen_coords(p)
        if 0 <= x <= width and 0 <= y <= height:
            pygame.draw.circle(screen, color, (x, y), 5)
            screen.blit(font.render(f"({p[0]:.1f}, {p[1]:.1f})", True, color), (x + 5, y - 20))
    if label and label_pos:
        screen.blit(font.render(label, True, color), label_pos)

# Main loop
running = True
while running:
    screen.fill(WHITE)
    draw_grid()

    # Calculate 45° rotated shape
    rotated_points = [rotate_point(p, theta) for p in points]

    # Draw original in BLUE
    draw_polygon(points, BLUE)

    # Draw rotated in RED with label
    draw_polygon(rotated_points, RED, rotation_label, label_position)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
