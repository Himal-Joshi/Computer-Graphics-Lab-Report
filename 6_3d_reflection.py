import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Define cube vertices in homogeneous coordinates
cube_vertices = np.array([
    [0, 0, 0, 1],  # 1
    [1, 0, 0, 1],  # 2
    [0, 1, 0, 1],  # 3
    [1, 1, 0, 1],  # 4
    [0, 0, 1, 1],  # 5
    [1, 0, 1, 1],  # 6
    [0, 1, 1, 1],  # 7
    [1, 1, 1, 1]   # 8
])

# Define cube faces using vertex indices
face_points = np.array([
    [0, 1, 3, 2],  # bottom
    [4, 5, 7, 6],  # top
    [0, 1, 5, 4],  # front
    [2, 3, 7, 6],  # back
    [0, 2, 6, 4],  # left
    [1, 3, 7, 5]   # right
])

# Define reflection matrix (reflect across XY-plane, i.e., negate z-coordinate)
reflection_matrix = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, -1, 0],
    [0, 0, 0, 1]
])

# Apply reflection to cube vertices
reflected_vertices = np.dot(cube_vertices, reflection_matrix.T)

# Create a 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Function to draw cube from given vertices
def draw_cube(vertices, color='red', alpha=0.5):
    for f in face_points:
        x = [vertices[i][0] for i in f]
        y = [vertices[i][1] for i in f]
        z = [vertices[i][2] for i in f]
        verts = [list(zip(x, y, z))]
        ax.add_collection3d(Poly3DCollection(verts, facecolors=color, edgecolors='black', alpha=alpha))

# Draw original cube in red
draw_cube(cube_vertices, color='red', alpha=0.5)

# Draw reflected cube in blue
draw_cube(reflected_vertices, color='blue', alpha=0.5)

# Add arrows for X, Y, Z axes
ax.quiver(0, 0, 0, 1.5, 0, 0, color='r', arrow_length_ratio=0.1)
ax.text(1.6, 0, 0, 'X', color='r')
ax.quiver(0, 0, 0, 0, 1.5, 0, color='g', arrow_length_ratio=0.1)
ax.text(0, 1.6, 0, 'Y', color='g')
ax.quiver(0, 0, 0, 0, 0, 1.5, color='b', arrow_length_ratio=0.1)
ax.text(0, 0, 1.6, 'Z', color='b')

# Draw XY-plane (z=0) as a semi-transparent plane for reference
xx, yy = np.meshgrid(np.linspace(-0.5, 1.5, 2), np.linspace(-0.5, 1.5, 2))
zz = np.zeros_like(xx)
ax.plot_surface(xx, yy, zz, color='gray', alpha=0.2)

# Set axis limits to accommodate both cubes
ax.set_xlim(-0.5, 1.5)
ax.set_ylim(-0.5, 1.5)
ax.set_zlim(-1.5, 1.5)

# Set labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Original and Reflected Cube (Across XY-plane)')

# Set a nice view angle
ax.view_init(30, 45)

# Show plot
plt.show()