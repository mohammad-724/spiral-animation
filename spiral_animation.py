import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import warnings

# Suppress minor matplotlib warnings for clean execution
warnings.filterwarnings("ignore")

# 1. System Parameters for the Lorenz Attractor
sigma = 10.0
beta = 8.0 / 3.0
rho = 28.0

# 2. Define the differential equations
def lorenz_deriv(r):
    """
    Calculates the spatial derivatives for the 3D Lorenz system.
    Expects r of shape (3, N) where N is the number of particles.
    """
    x, y, z = r[0], r[1], r[2]
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return np.array([dx, dy, dz])

# 3. 4th-Order Runge-Kutta Integration
def rk4_step(r, dt):
    """
    High-precision numerical integration to solve the differential equations.
    """
    k1 = lorenz_deriv(r)
    k2 = lorenz_deriv(r + 0.5 * dt * k1)
    k3 = lorenz_deriv(r + 0.5 * dt * k2)
    k4 = lorenz_deriv(r + dt * k3)
    return r + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)

# 4. Initialize Particle Swarm
N_particles = 1000
dt = 0.015  # Time step

# All particles start at exactly [1.0, 1.0, 20.0] but with microscopic quantum noise (1e-4)
# Chaos theory states these microscopic differences will eventually cause massive divergence.
r0 = np.array([1.0, 1.0, 20.0])
particles = r0 + np.random.randn(N_particles, 3) * 1e-4

# 5. Configure the 3D Rendering Engine
fig = plt.figure(figsize=(10, 8), facecolor='black')
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor('black')

# Remove grid lines and axes for a cinematic, floating effect
ax.grid(False)
ax.axis('off')
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

# Set rigid boundaries to prevent camera jumping
ax.set_xlim((-25, 25))
ax.set_ylim((-35, 35))
ax.set_zlim((5, 55))

# Map a rainbow color gradient across the particle indices
colors = plt.cm.hsv(np.linspace(0, 1, N_particles))

# Render initial scatter plot
scatter = ax.scatter(particles[:, 0], particles[:, 1], particles[:, 2], 
                     c=colors, s=1.5, alpha=0.8, edgecolors='none')

# 6. Animation Loop
def update(frame):
    global particles
    
    # Calculate the next micro-step in 3D space for all 1,000 particles simultaneously
    # Transpose is used because our rk4_step expects shape (3, N)
    particles = rk4_step(particles.T, dt).T
    
    # Update scatter plot positions
    scatter._offsets3d = (particles[:, 0], particles[:, 1], particles[:, 2])
    
    # Slowly rotate the 3D camera
    ax.view_init(elev=20 + np.sin(frame * 0.02) * 10, azim=frame * 0.5)
    
    return scatter,

# 7. Execute Animation
# blit=False allows the 3D axes to dynamically update frame by frame
ani = FuncAnimation(fig, update, frames=2000, interval=20, blit=False)

# Display the render window
plt.show()