import matplotlib.pyplot as plt

def Bresenham(x1, y1, x2, y2):
    x, y = x1, y1
    dx = x2 - x1
    dy = y2 - y1
    p = 2 * dy - dx

    x_coordinates = []
    y_coordinates = []

    for i in range(dx + 1):
        x_coordinates.append(x)
        y_coordinates.append(y)
        x = x + 1
        if p < 0:
            p = p + 2 * dy
        else:
            y = y + 1
            p = p + 2 * (dy - dx)

    return x_coordinates, y_coordinates

if __name__ == "__main__":
    # Ask user for coordinates
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))

    # Function call
    a, b = Bresenham(x1, y1, x2, y2)

    print("X coordinates:", a)
    print("Y coordinates:", b)

    # Plot the line
    plt.plot(a, b, marker="o", markersize=4, markerfacecolor="green")
    plt.title("BRESENHAM LINE DRAWING")
    plt.xlabel("X-AXIS")
    plt.ylabel("Y-AXIS")
    plt.grid(True)
    plt.show()
