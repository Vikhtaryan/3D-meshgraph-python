import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
sns.set(style="darkgrid")

def plot_mesh_graph(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(x, y, z, cmap='viridis', edgecolor='none')
    ax.set_title('3D Mesh Graph')
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')

    m = plt.cm.ScalarMappable(cmap='viridis')
    m.set_array(z)
    plt.colorbar(m, ax=ax, shrink=0.5, aspect=5)
    plt.savefig('mesh_plot.png')
print("Plot saved as mesh_plot.png")


# Example data
x = np.random.rand(100)
y = np.random.rand(100)
z = np.sin(x*10) + np.cos(y*10)

plot_mesh_graph(x, y, z)

