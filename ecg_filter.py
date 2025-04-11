```python
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Sampling frequency (Hz) - samples per second
fs = 1000  
# Time vector for 1 second of data
t = np.arange(0, 1, 1/fs)  
# Heart signal frequency (~72 beats per minute)
f_heart = 1.2  
# Amplitude of random white noise
noise_amplitude = 0.5  

# Generate clean ECG signal (simple sine wave)
ecg_clean = np.sin(2 * np.pi * f_heart * t)  
# Add random white noise to simulate real-world interference
noise = noise_amplitude * np.random.normal(0, 1, len(t))  
ecg_noisy = ecg_clean + noise  

# Design Butterworth low-pass filter (cuts off noise above 20 Hz)
cutoff = 20  # Cutoff frequency (Hz)
order = 4  # Filter order
nyquist = fs / 2  # Nyquist frequency
normal_cutoff = cutoff / nyquist
b, a = signal.butter(order, normal_cutoff, btype='low', analog=False)

# Apply filter to noisy signal
ecg_filtered = signal.filtfilt(b, a, ecg_noisy)

# Plot results
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t, ecg_clean, 'b', label='Clean Signal')
plt.title('Clean ECG Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(t, ecg_noisy, 'r', label='Noisy Signal')
plt.title('Noisy ECG Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(t, ecg_filtered, 'g', label='Filtered Signal')
plt.title('Filtered ECG Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()

plt.tight_layout()
plt.show()
