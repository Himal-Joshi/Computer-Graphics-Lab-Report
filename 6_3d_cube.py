import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Define the vertices of the unit cube
vertices = np.array([[0,0,0], [1,0,0], [0,1,0], [1,1,0], [0,0,1], [1,0,1], [0,1,1], [1,1,1]])

# Define the faces of the cube using vertex indices
faces = [
    [0,1,3,2],  # bottom
    [4,5,7,6],  # top
    [0,1,5,4],  # front
    [2,3,7,6],  # back
    [0,2,6,4],  # left
    [1,3,7,5]   # right
]

# Define colors for each face
colors = ['r', 'g', 'b', 'y', 'c', 'm']

# Define the edges of the cube
edges = [
    (0,1), (1,3), (3,2), (2,0),  # bottom
    (4,5), (5,7), (7,6), (6,4),  # top
    (0,4), (1,5), (2,6), (3,7)   # vertical edges
]

# Create a figure and a 3D axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot each face with its corresponding color
for i, face in enumerate(faces):
    poly = Poly3DCollection([vertices[face]], facecolors=colors[i], alpha=0.5, edgecolors='none')
    ax.add_collection3d(poly)

# Plot each edge in black
for edge in edges:
    ax.plot3D(*vertices[[edge[0], edge[1]]].T, color='k')

# Add arrows for X, Y, Z axes
# X-axis (red)
ax.quiver(0, 0, 0, 1.2, 0, 0, color='r', arrow_length_ratio=0.1)
ax.text(1.3, 0, 0, 'X', color='r')

# Y-axis (green)
ax.quiver(0, 0, 0, 0, 1.2, 0, color='g', arrow_length_ratio=0.1)
ax.text(0, 1.3, 0, 'Y', color='g')

# Z-axis (blue)
ax.quiver(0, 0, 0, 0, 0, 1.2, color='b', arrow_length_ratio=0.1)
ax.text(0, 0, 1.3, 'Z', color='b')

# Set the limits for the axes
ax.set_xlim(-0.2, 1.2)
ax.set_ylim(-0.2, 1.2)
ax.set_zlim(-0.2, 1.2)

# Remove default axis labels
ax.set_xlabel('')
ax.set_ylabel('')
ax.set_zlabel('')

# Set a nice view angle
ax.view_init(30, 45)

# Show the plot
plt.show()