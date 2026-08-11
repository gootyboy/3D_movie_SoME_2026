from manim import *

def chaotic_wave_func(t, frequencies = [12.0, 24.0, 36.0, 48.0], amplitudes = [0.12, 0.06, 0.04, 0.02], phases = [0.0, 1.2, 2.8, 4.5]):
    y_val = 3.0 * t
    x_val = sum(a * np.sin(f * y_val + p) for f, a, p in zip(frequencies, amplitudes, phases))
    z_val = sum(a * np.cos(f * y_val + p) for f, a, p in zip(frequencies, amplitudes, phases)) 
    return np.array([x_val, y_val, z_val])

def linear_wave_func(t, frequencies = [12.0, 24.0, 36.0, 48.0], amplitudes = [0.12, 0.06, 0.04, 0.02], phases = [0.0, 1.2, 2.8, 4.5]):
    y_val = 3.0 * t
    x_val = sum(a * np.sin(f * y_val + p) for f, a, p in zip(frequencies, amplitudes, phases))
    z_val = 0
    return np.array([x_val, y_val, z_val])

def left_circular_polarized(t):
    return np.array([0.4 * np.cos(7 * 3.0 * t), 3.0 * t, 0.4 * np.sin(7 * 3.0 * t)])

def right_circular_polarized(t):
    return np.array([0.4 * np.cos(7 * 3.0 * t), 3.0 * t, -0.4 * np.sin(7 * 3.0 * t)])
