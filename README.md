# ECG Signal Filter
A Python script to simulate and filter noise from an electrocardiogram (ECG) signal using a Butterworth low-pass filter. This project demonstrates signal processing for biomedical engineering applications, cleaning up noisy heart data to reveal the true signal.

## Features
- Generates a synthetic ECG signal with a heart rate of ~72 beats per minute (1.2 Hz).
- Adds random white noise to mimic real-world sensor interference.
- Applies a 4th-order Butterworth filter (20 Hz cutoff) to remove high-frequency noise.
- Plots three graphs: clean signal, noisy signal, and filtered signal.

## Prerequisites
- Python 3.x
- Required libraries:  
  ```bash
  pip install -r requirements.txt
