import pygame

pygame.init()
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("2D Reflections with Labels")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)

font = pygame.font.SysFont(None, 16)
scale = 40
points = [[0, 0, 1], [4, 0, 1], [4, 2, 1], [0, 2, 1]]

# Reflection matrices
matrices = [
    [[-1, 0, 0], [0, 1, 0], [0, 0, 1]],   # Y-axis
    [[1, 0, 0], [0, -1, 0], [0, 0, 1]],   # X-axis
    [[-1, 0, 0], [0, -1, 0], [0, 0, 1]]   # Origin (x and y)
]

# Reflection labels and their positions (screen coordinates)
reflection_labels = [
    ("Y-axis Reflection", (100, 80)),   # Moved up to avoid overlap
    ("X-axis Reflection", (400, 300)),  # Bottom-right, unchanged
    ("Origin Reflection", (100, 300))   # Bottom-left, unchanged
]

def reflect_point(p, matrix):
    x = matrix[0][0] * p[0] + matrix[0][1] * p[1] + matrix[0][2] * p[2]
    y = matrix[1][0] * p[0] + matrix[1][1] * p[1] + matrix[1][2] * p[2]
    return [x, y, 1]

def to_screen_coords(p):
    return (int(width // 2 + p[0] * scale), int(height // 2 - p[1] * scale))

def draw_grid():
    for x in range(0, width, scale):
        pygame.draw.line(screen, GRAY, (x, 0), (x, height))
        screen.blit(font.render(str((x - width // 2) // scale), True, BLACK), (x, height // 2 + 5))
    for y in range(0, height, scale):
        pygame.draw.line(screen, GRAY, (0, y), (width, y))
        screen.blit(font.render(str((height // 2 - y) // scale), True, BLACK), (width // 2 + 5, y))
    pygame.draw.line(screen, BLACK, (0, height // 2), (width, height // 2), 2)
    pygame.draw.line(screen, BLACK, (width // 2, 0), (width // 2, height), 2)

def draw_polygon(points, color, label=None, label_pos=None):
    screen_points = [to_screen_coords(p) for p in points]
    pygame.draw.polygon(screen, color, screen_points, 2)
    for p in points:
        x, y = to_screen_coords(p)
        if 0 <= x <= width and 0 <= y <= height:
            pygame.draw.circle(screen, color, (x, y), 5)
            screen.blit(font.render(f"({p[0]:.1f}, {p[1]:.1f})", True, color), (x + 5, y - 20))
    if label and label_pos:
        screen.blit(font.render(label, True, GREEN), label_pos)

running = True
while running:
    # Compute three sets of reflected points
    y_axis_points = [reflect_point(p, matrices[0]) for p in points]  # Y-axis
    x_axis_points = [reflect_point(p, matrices[1]) for p in points]  # X-axis
    origin_points = [reflect_point(p, matrices[2]) for p in points]  # Origin

    screen.fill(WHITE)
    draw_grid()
    draw_polygon(points, BLUE)  # Original
    draw_polygon(y_axis_points, GREEN, reflection_labels[0][0], reflection_labels[0][1])  # Y-axis reflection
    draw_polygon(x_axis_points, GREEN, reflection_labels[1][0], reflection_labels[1][1])  # X-axis reflection
    draw_polygon(origin_points, GREEN, reflection_labels[2][0], reflection_labels[2][1])  # Origin reflection

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()