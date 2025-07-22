import pygame

# Initialize Pygame
pygame.init()

# Window size and display
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("2D Transformations")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (128, 0, 128)
YELLOW = (255, 255, 0)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)

# Font and scale
font = pygame.font.SysFont(None, 16)
scale = 40
points = [[0, 0, 1], [4, 0, 1], [4, 2, 1], [0, 2, 1]]

# Transformation parameters
tx, ty = 3, 2  # Translation
sx, sy = 1.5, 1.5  # Scaling
shx, shy = 0.5, 0.5  # Shearing
cos_theta = 0.7071  # Precomputed cos(45°)
sin_theta = 0.7071  # Precomputed sin(45°)

# Reflection matrix (Y-axis reflection for simplicity)
reflection_matrix = [[-1, 0, 0], [0, 1, 0], [0, 0, 1]]  # Y-axis reflection

# Labels and positions for transformations
labels = [
    ("Original", (10, 10), BLUE),
    ("Translation", (10, 30), GREEN),
    ("Scaling", (10, 50), RED),
    ("Shearing", (10, 70), PURPLE),
    ("Y-axis Reflection", (10, 90), YELLOW),
    ("45° Rotation", (10, 110), BLACK)
]

# Transformation functions
def translate_point(p, tx, ty):
    return [p[0] + tx, p[1] + ty, 1]

def scale_point(p, sx, sy):
    return [p[0] * sx, p[1] * sy, 1]

def shear_point(p, shx, shy):
    x = p[0] + shx * p[1]
    y = p[1] + shy * p[0]
    return [x, y, 1]

def reflect_point(p, matrix):
    x = matrix[0][0] * p[0] + matrix[0][1] * p[1] + matrix[0][2] * p[2]
    y = matrix[1][0] * p[0] + matrix[1][1] * p[1] + matrix[1][2] * p[2]
    return [x, y, 1]

def rotate_point(p, cos_theta, sin_theta):
    x = p[0] * cos_theta - p[1] * sin_theta
    y = p[0] * sin_theta + p[1] * cos_theta
    return [x, y, 1]

# Coordinate conversion
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
    pygame.draw.line(screen, BLACK, (0, height // 2), (width, height // 2), 2)
    pygame.draw.line(screen, BLACK, (width // 2, 0), (width // 2, height), 2)

# Draw polygon
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

    # Original shape
    draw_polygon(points, BLUE, labels[0][0], labels[0][1])

    # Translation transformation
    translated_points = [translate_point(p, tx, ty) for p in points]
    draw_polygon(translated_points, GREEN, labels[1][0], labels[1][1])

    # Scaling transformation
    scaled_points = [scale_point(p, sx, sy) for p in points]
    draw_polygon(scaled_points, RED, labels[2][0], labels[2][1])

    # Shearing transformation
    sheared_points = [shear_point(p, shx, shy) for p in points]
    draw_polygon(sheared_points, PURPLE, labels[3][0], labels[3][1])

    # Reflection transformation
    reflected_points = [reflect_point(p, reflection_matrix) for p in points]
    draw_polygon(reflected_points, YELLOW, labels[4][0], labels[4][1])

    # Rotation transformation
    rotated_points = [rotate_point(p, cos_theta, sin_theta) for p in points]
    draw_polygon(rotated_points, BLACK, labels[5][0], labels[5][1])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()