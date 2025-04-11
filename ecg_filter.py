import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Parameters
fs = 1000  # Sampling frequency (Hz)
t = np.arange(0, 1, 1/fs)  # Time vector (1 second)
f_heart = 1.2  # Heart rate frequency (~72 beats per minute)
noise_amplitude = 0.5  # Noise intensity

# Create synthetic ECG signal (simple sine wave + noise)
ecg_clean = np.sin(2 * np.pi * f_heart * t)  # Clean signal
noise = noise_amplitude * np.random.normal(0, 1, len(t))  # White noise
ecg_noisy = ecg_clean + noise  # Signal with noise

# Design Butterworth filter (low-pass)
cutoff = 20  # Cutoff frequency (Hz) - removes noise above 20Hz
order = 4  # Filter order
nyquist = fs / 2  # Nyquist frequency
normal_cutoff = cutoff / nyquist
b, a = signal.butter(order, normal_cutoff, btype='low', analog=False)

# Apply filter to the signal
ecg_filtered = signal.filtfilt(b, a, ecg_noisy)

# Plot results
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t, ecg_clean, 'b', label='Clean Signal')
plt.title('Clean ECG Signal')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(t, ecg_noisy, 'r', label='Noisy Signal')
plt.title('ECG Signal with Noise')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(t, ecg_filtered, 'g', label='Filtered Signal')
plt.title('Filtered ECG Signal')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.legend()

plt.tight_layout()
plt.show()
