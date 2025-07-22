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


# Draw original cube in blue
draw_cube(cube_vertices, color='red', alpha=0.5)




# Set labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Cube')

# Show plot
plt.show()
