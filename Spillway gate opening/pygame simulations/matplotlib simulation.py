import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Parameters
total_frames = 100
gate_heights = [9.5] * 8  # Initial gate heights for 8 gates
opening_speed = 0.2
thresholds = [438, 438.5, 439, 440]  # Water level thresholds for gate opening
gate_level = [0.7,2.5, 4.7, 9.5]

# Function to update the plot in each frame
def update(frame):
    global gate_heights
    water_height = 439.5  # Initial water level

    # Clear the previous frame
    plt.clf()

    # Plot the dam
    plt.plot([0, 10, 10, 0, 0], [0, 0, 5, 5, 0], 'k-', lw=2)

    # Plot the water
    plt.fill_between([0, 10], [water_height, water_height], color='blue', alpha=0.5)

    level = 9.5

    # Determine which gates should open based on water level
    for i, threshold in enumerate(thresholds, start=1):
        if water_height > threshold:
            gate_heights[(8-(i+4))%8] = max(level- gate_level[i-1], gate_heights[(8-(i+4))%8] - opening_speed)
            gate_heights[(8-(i+4))%8] = min(level, gate_heights[(8-(i+4))%8])

            gate_heights[(i+3)%8] = max(level- gate_level[i-1], gate_heights[(i+3)%8] - opening_speed)
            gate_heights[(i+3)%8] = min(level, gate_heights[(i+3)%8])

    level = 9.5 - gate_level[i-1]

    # Plot the spillway gates
    for i, gate_height in enumerate(gate_heights):
        plt.fill_between([i + 1 - 0.4, i + 1 + 0.4], [gate_height, gate_height], color='red', alpha=0.7)

    # Set plot limits and labels
    plt.xlim(0, 10)
    plt.ylim(0, 40)
    plt.title('Dam Spillway Gate Opening Simulation')

# Create a figure and animate
fig = plt.figure()
ani = animation.FuncAnimation(fig, update, frames=total_frames, interval=100)
plt.show()
