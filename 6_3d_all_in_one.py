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

# Define translation matrix (translate by tx=2, ty=1, tz=1)
translation_vector = np.array([2, 1, 1])
translation_matrix = np.array([
    [1, 0, 0, translation_vector[0]],
    [0, 1, 0, translation_vector[1]],
    [0, 0, 1, translation_vector[2]],
    [0, 0, 0, 1]
])

# Define scaling matrix (scale by sx=1.5, sy=1.5, sz=1.5)
scaling_factors = np.array([1.5, 1.5, 1.5])
scaling_matrix = np.array([
    [scaling_factors[0], 0, 0, 0],
    [0, scaling_factors[1], 0, 0],
    [0, 0, scaling_factors[2], 0],
    [0, 0, 0, 1]
])

# Define rotation matrix (rotate 45 degrees around Z-axis)
theta = np.radians(45)
cos_theta = np.cos(theta)
sin_theta = np.sin(theta)
rotation_matrix = np.array([
    [cos_theta, -sin_theta, 0, 0],
    [sin_theta, cos_theta, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])

# Apply transformations to cube vertices
translated_vertices = np.dot(cube_vertices, translation_matrix.T)
scaled_vertices = np.dot(cube_vertices, scaling_matrix.T)
rotated_vertices = np.dot(cube_vertices, rotation_matrix.T)

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

# Draw translated cube in blue
draw_cube(translated_vertices, color='blue', alpha=0.5)

# Draw scaled cube in green
draw_cube(scaled_vertices, color='green', alpha=0.5)

# Draw rotated cube in yellow
draw_cube(rotated_vertices, color='yellow', alpha=0.5)

# Add arrows for X, Y, Z axes
ax.quiver(0, 0, 0, 3, 0, 0, color='r', arrow_length_ratio=0.1)
ax.text(3.1, 0, 0, 'X', color='r')
ax.quiver(0, 0, 0, 0, 3, 0, color='g', arrow_length_ratio=0.1)
ax.text(0, 3.1, 0, 'Y', color='g')
ax.quiver(0, 0, 0, 0, 0, 3, color='b', arrow_length_ratio=0.1)
ax.text(0, 0, 3.1, 'Z', color='b')

# Set axis limits to accommodate all cubes
ax.set_xlim(-0.5, 3.5)
ax.set_ylim(-0.5, 2.5)
ax.set_zlim(-0.5, 2.5)

# Set labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Original, Translated, Scaled, and Rotated Cubes')

# Set a nice view angle
ax.view_init(30, 45)

# Show plot
plt.show()