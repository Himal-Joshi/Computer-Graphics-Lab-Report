import matplotlib.pyplot as plt


def dda_line_plot(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))
    x_increment = dx / steps
    y_increment = dy / steps
    x = x1
    y = y1
    x_points = []
    y_points = []
    for _ in range(steps + 1):
        x_points.append(round(x))
        y_points.append(round(y))
        x += x_increment
        y += y_increment

    plt.figure(figsize=(6, 6))
    plt.plot(x_points, y_points, marker='s', color='blue', linestyle='-') # ← blue line
    plt.title("DDA Line Drawing Algorithm")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.gca().invert_yaxis()
    plt.show()


# Get user input
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
dda_line_plot(x1, y1, x2, y2)