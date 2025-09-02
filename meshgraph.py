import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Enable seaborn style
sns.set(style="darkgrid")

def plot_mesh_graph(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(x, y, z, cmap='viridis', edgecolor='none')
    
    ax.set_title('3D Mesh Graph', pad=20)
    ax.set_xlabel('X axis', labelpad=15)
    ax.set_ylabel('Y axis', labelpad=15)
    ax.set_zlabel('Z axis', labelpad=15)
    
    # Add color bar
    m = plt.cm.ScalarMappable(cmap='viridis')
    m.set_array(z)
    plt.colorbar(m, ax=ax, shrink=0.5, aspect=5)
    
    plt.show()
