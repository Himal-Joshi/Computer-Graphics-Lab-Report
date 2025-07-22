import pygame

pygame.init()
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("2D Scaling")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)

font = pygame.font.SysFont(None, 16)
scale = 40
points = [[0, 0, 1], [4, 0, 1], [4, 2, 1], [0, 2, 1]]
sx, sy = 1.5, 1.5  # Initial scaling factors

def scale_point(p, sx, sy):
    return [p[0] * sx, p[1] * sy, 1]

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

def draw_polygon(points, color):
    screen_points = [to_screen_coords(p) for p in points]
    pygame.draw.polygon(screen, color, screen_points, 2)
    for p in points:
        x, y = to_screen_coords(p)
        if 0 <= x <= width and 0 <= y <= height:
            pygame.draw.circle(screen, color, (x, y), 5)
            screen.blit(font.render(f"({p[0]:.1f}, {p[1]:.1f})", True, color), (x + 5, y - 20))

running = True
while running:
    scaled_points = [scale_point(p, sx, sy) for p in points]
    screen.fill(WHITE)
    draw_grid()
    draw_polygon(points, BLUE)
    draw_polygon(scaled_points, GREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and sx > 0.5:  # Min scale 0.5
                sx -= 0.1
            elif event.key == pygame.K_RIGHT and sx < 2.0:  # Max scale 2.0
                sx += 0.1
            elif event.key == pygame.K_UP and sy < 2.0:  # Max scale 2.0
                sy += 0.1
            elif event.key == pygame.K_DOWN and sy > 0.5:  # Min scale 0.5
                sy -= 0.1

    pygame.display.update()

pygame.quit()