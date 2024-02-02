import numpy as np
import matplotlib.pyplot as plt

# Define the number of data points and the time step
num_samples = 1000
time_step = 0.01  # 10 ms

# Define initial roll, yaw, and pitch values in radians
initial_roll = 0.0
initial_yaw = 0.0
initial_pitch = 0.0

# Create arrays to store the generated data with noise
roll_values = np.zeros(num_samples)
yaw_values = np.zeros(num_samples)
pitch_values = np.zeros(num_samples)

# Create arrays to store the original (noiseless) data
original_roll_values = np.zeros(num_samples)
original_yaw_values = np.zeros(num_samples)
original_pitch_values = np.zeros(num_samples)

# Create noise parameters (adjust as needed)
white_noise_stddev = 0.1  # Standard deviation of white noise

# Generate synthetic IMU data with white noise
for i in range(num_samples):
    # Generate random white noise
    noise_roll = np.random.normal(0, white_noise_stddev)
    noise_yaw = np.random.normal(0, white_noise_stddev)
    noise_pitch = np.random.normal(0, white_noise_stddev)

    # Update roll, yaw, and pitch with noise
    roll = initial_roll + noise_roll
    yaw = initial_yaw + noise_yaw
    pitch = initial_pitch + noise_pitch

    # Store the values with noise
    roll_values[i] = roll
    yaw_values[i] = yaw
    pitch_values[i] = pitch


    # Update initial values for the next iteration (e.g., to simulate motion)
    initial_roll = roll
    initial_yaw = yaw
    initial_pitch = pitch

# Create time values
time_values = np.arange(0, num_samples * time_step, time_step)

# Plot the roll, yaw, and pitch data with and without noise
plt.figure(figsize=(12, 6))
plt.subplot(3, 1, 1)
plt.plot(time_values, original_roll_values, label='Original Roll (noiseless)', color='green')
plt.plot(time_values, roll_values, label='Roll with Noise (rad)', color='blue')
plt.title('IMU Roll')
plt.grid(True)
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(time_values, original_yaw_values, label='Original Yaw (noiseless)', color='green')
plt.plot(time_values, yaw_values, label='Yaw with Noise (rad)', color='blue')
plt.title('IMU Yaw')
plt.grid(True)
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(time_values, original_pitch_values, label='Original Pitch (noiseless)', color='green')
plt.plot(time_values, pitch_values, label='Pitch with Noise (rad)', color='blue')
plt.title('IMU Pitch')
plt.xlabel('Time (s)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
